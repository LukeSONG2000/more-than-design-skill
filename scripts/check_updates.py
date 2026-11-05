#!/usr/bin/env python3
"""Daily, read-only update checks shared by all local skill installations."""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = '@lukesong2000/more-than-design-skill'
PUBLIC = 'https://github.com/LukeSONG2000/more-than-design-skill.git'
ENTERPRISE = 'https://github.com/ciqtek-aitea/more-than-design-skill.git'


def run(args, cwd=None):
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    return subprocess.run(args, cwd=cwd, env=env, capture_output=True,
                          text=True, timeout=20, check=True).stdout.strip()


def version(text):
    match = re.search(r'^version:\s*[\"\']?([0-9]+\.[0-9]+\.[0-9]+)\s*$', text, re.M)
    if not match:
        raise ValueError('Missing supported stable version')
    return match.group(1)


def source(root):
    # Only an installation's own Git metadata counts, not its parent project.
    if (root / '.git').exists():
        remote = run(['git', 'remote', 'get-url', 'origin'], root)
        normalized = remote.replace('git@github.com:', 'https://github.com/').removesuffix('.git')
        for allowed in (PUBLIC, ENTERPRISE):
            if normalized.lower() == allowed.removesuffix('.git').lower():
                return 'git', allowed
        raise ValueError('Unrecognized origin; automatic remote access disabled')
    return 'registry', REFERENCE


def query(channel, address):
    if channel == 'git':
        line = run(['git', 'ls-remote', address, 'refs/heads/main'])
        commit = line.split()[0] if line else ''
        if not re.fullmatch(r'[0-9a-f]{40,64}', commit):
            raise ValueError('Missing remote main')
        return {'commit': commit}
    cli = shutil.which('skill-home')
    if cli is None:
        candidate = Path.home() / '.local/bin/skill-home'
        cli = str(candidate) if candidate.is_file() else None
    if cli is None:
        raise ValueError('skill-home is unavailable; registry check deferred')
    data = json.loads(run([cli, 'info', address, '--format', 'json']))
    latest = data.get('latest_version', '')
    if not re.fullmatch(r'\d+\.\d+\.\d+', latest):
        raise ValueError('Unsupported registry version response')
    return {'version': latest}


def daily(db_path, key, probe, now=None):
    now = now or datetime.now().astimezone()
    day = now.date().isoformat()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path, timeout=3) as db:
        db.execute('CREATE TABLE IF NOT EXISTS checks '
                   '(source TEXT PRIMARY KEY, day TEXT, checked_at TEXT, result TEXT)')
        db.execute('BEGIN IMMEDIATE')
        row = db.execute('SELECT day, checked_at, result FROM checks WHERE source=?', (key,)).fetchone()
        if row and row[0] == day:
            return json.loads(row[2]), True, row[1]
        stamp = now.isoformat()
        # Reserve before network access: concurrent chats and crashed processes
        # cannot repeatedly access a channel during the same calendar day.
        pending = json.dumps({'status': 'pending_or_interrupted'})
        db.execute('INSERT OR REPLACE INTO checks VALUES (?, ?, ?, ?)', (key, day, stamp, pending))
        db.commit()
        try:
            result = {'status': 'ok', 'remote': probe()}
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            # Avoid persisting credentials or raw subprocess/server output.
            result = {'status': 'unavailable', 'error_type': type(error).__name__}
        db.execute('UPDATE checks SET result=? WHERE source=? AND checked_at=?',
                   (json.dumps(result), key, stamp))
        db.commit()
        return result, False, stamp


def check(root, state):
    channel, address = source(root)
    result, cached, stamp = daily(state, channel + ':' + address, lambda: query(channel, address))
    output = {'channel': channel, 'source': address, 'cached': cached,
              'checked_at': stamp, 'state_file': str(state), **result}
    output['notify'] = False
    if result['status'] == 'ok':
        if channel == 'git':
            local = run(['git', 'rev-parse', 'HEAD'], root)
            different = local != result['remote']['commit']
            output.update(local_commit=local,
                          comparison='remote_differs' if different else 'same_commit',
                          dirty=bool(run(['git', 'status', '--porcelain'], root)))
        else:
            local = version((root / 'SKILL.md').read_text())
            different = tuple(map(int, result['remote']['version'].split('.'))) > tuple(map(int, local.split('.')))
            output.update(local_version=local, comparison='newer_version' if different else 'not_newer')
        output['notify'] = different and not cached
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state-dir', type=Path, help='Override shared state directory (testing/administration)')
    args = parser.parse_args()
    base = args.state_dir or Path(os.environ.get('XDG_STATE_HOME', str(Path.home() / '.local/state'))) / 'more-than-design-skill'
    try:
        result = check(ROOT, base.expanduser() / 'update-checks.sqlite3')
    except (OSError, ValueError, sqlite3.Error, subprocess.SubprocessError) as error:
        result = {'status': 'local_error', 'error_type': type(error).__name__, 'notify': False}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
