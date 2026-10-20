#!/usr/bin/env python3
"""校验完整源码仓库的本地文档、锚点、平台路由与 CSS 资源，不访问外网。"""

from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    from markdown_it import MarkdownIt
except ImportError:
    sys.exit('需要 markdown-it-py：python3 -m pip install markdown-it-py')

ROOT = Path(__file__).resolve().parents[1]
PARSER = MarkdownIt('commonmark').enable('table')


def headings(tokens):
    """匹配当前文档使用的 GitHub 标题锚点（含重复标题后缀）。"""
    result = set()
    seen = Counter()
    for i, token in enumerate(tokens):
        if token.type != 'heading_open':
            continue
        children = tokens[i + 1].children or []
        label = ''.join(t.content for t in children if t.type in ('text', 'code_inline'))
        slug = re.sub(r'[^\w\- ]', '', label.lower()).replace(' ', '-')
        result.add(slug if not seen[slug] else f'{slug}-{seen[slug]}')
        seen[slug] += 1
    return result


def validate(root=ROOT):
    docs = {p.resolve(): p.read_text() for p in root.rglob('*.md') if '.git' not in p.parts}
    parsed = {p: PARSER.parse(s) for p, s in docs.items()}
    anchors = {p: headings(ts) for p, ts in parsed.items()}
    graph = {p: set() for p in docs}
    errors = []
    links = 0

    def check(source, target):
        nonlocal links
        url = urlsplit(target)
        if url.scheme or url.netloc:
            return
        links += 1
        dest = (source.parent / unquote(url.path)).resolve() if url.path else source
        label = f'{source.relative_to(root)} -> {target}'
        if not dest.is_relative_to(root):
            errors.append(f'超出仓库: {label}')
        elif not dest.exists():
            errors.append(f'目标不存在: {label}')
        elif dest in docs:
            graph[source].add(dest)
            if url.fragment and unquote(url.fragment) not in anchors[dest]:
                errors.append(f'锚点不存在: {label}')

    for p, tokens in parsed.items():
        errors.extend(f'裸编号文档引用: {p.relative_to(root)}:{line}' for line in numeric_references(tokens))
        if re.search(r'\b\d{2}-[a-z][\w-]*\.md\b', docs[p]):
            errors.append(f'旧编号路径: {p.relative_to(root)}')
        for token in tokens:
            for child in token.children or []:
                if child.type == 'link_open':
                    check(p, child.attrGet('href'))
                elif child.type == 'image':
                    check(p, child.attrGet('src'))
                elif child.type == 'code_inline' and re.fullmatch(r'[\w./-]+\.md(?:#[\w-]+)?', child.content):
                    check(p, child.content)
    for p in root.rglob('*.css'):
        if '.git' in p.parts:
            continue
        for target in re.findall(r'url\([\'"]?([^\'"\s)]+)', p.read_text()):
            check(p, target)

    entry = root / 'SKILL.md'
    for platform in ('cross-platform', 'apple', 'android', 'windows', 'web'):
        index = root / 'references' / platform / 'index.md'
        if index not in graph.get(entry, set()):
            errors.append(f'入口未链接平台索引: {platform}')
    required = {
        'apple/index.md': ('apple/motion.md', 'apple/liquid-glass/index.md'),
        'apple/liquid-glass/index.md': ('apple/liquid-glass/motion.md',),
        'android/index.md': ('android/material-motion.md',),
        'windows/index.md': ('windows/microsoft-motion.md',),
        'web/index.md': ('web/apple-style-motion.md', 'web/apple-style-motion-templates.md'),
    }
    for origin, targets in required.items():
        for target in targets:
            if root / 'references' / target not in graph.get(root / 'references' / origin, set()):
                errors.append(f'缺失独立动效路由: {origin} -> {target}')
    visited = set()
    pending = [entry]
    while pending:
        p = pending.pop()
        if p not in visited:
            visited.add(p)
            pending.extend(graph.get(p, ()))
    references = set((root / 'references').rglob('*.md'))
    for p in sorted(references - visited):
        errors.append(f'入口不可达资料: {p.relative_to(root)}')
    return errors, len(docs), len(references), links


def numeric_references(tokens):
    """仅检查路由表的引用列和明确的参见语句；忽略代码块与数值列。"""
    number = r'(?:0\d|[12]\d|3[0-3])'
    cue = re.compile(r'(?:参见|详见|参考|见|route\s+to|style\s+tokens\s+stay\s+in)\s*'
                     + r'`?' + number + r'`?(?=$|[\s,，、/;；。|]| or )', re.I)
    routing_header = re.compile(r'local\s+refs?|covered\s+locally|^route$|^(?:(?:local|document)\s+)?references?$|本地.*(?:引用|资料)|参考(?:资料|文档)|引用', re.I)
    bare_list = re.compile(r'^\s*`?' + number + r'`?(?:\s*[,，、/]\s*`?' + number + r'`?)*\s*$')
    columns = set()
    column = -1
    in_header = False
    in_cell = False
    found = []
    for token in tokens:
        if token.type == 'table_open':
            columns = set()
        elif token.type == 'tr_open':
            column = -1
        elif token.type in ('th_open', 'td_open'):
            column += 1
            in_header = token.type == 'th_open'
            in_cell = True
        elif token.type in ('th_close', 'td_close', 'table_close'):
            in_cell = False
        elif token.type == 'inline':
            if in_header and in_cell:
                if routing_header.search(token.content):
                    columns.add(column)
                continue
            children = token.children or []
            # 链接显示文字不属于裸引用，避免把有效链接中的数字误报。
            plain = []
            depth = 0
            for child in children:
                if child.type == 'link_open':
                    depth += 1
                elif child.type == 'link_close':
                    depth -= 1
                elif not depth and child.type in ('text', 'code_inline'):
                    plain.append(('`' + child.content + '`') if child.type == 'code_inline' else child.content)
            text = ''.join(plain)
            routed = in_cell and column in columns and (
                any(c.type == 'code_inline' and re.fullmatch(number, c.content) for c in children)
                or bare_list.fullmatch(text))
            if routed or cue.search(text):
                found.append((token.map or [0])[0] + 1)
    return found


if __name__ == '__main__':
    errors, docs, refs, links = validate()
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print(f'PASS: {docs} Markdown files, {refs} reachable references, {links} local links/resources; platform and motion routes valid.')
