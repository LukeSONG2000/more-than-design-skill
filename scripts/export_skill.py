#!/usr/bin/env python3
"""Export this skill recursively without platform conversion or installation."""

import argparse
from pathlib import Path
import shutil


SOURCE = Path(__file__).resolve().parents[1]
FILES = ("SKILL.md", "README.md", "LICENSE")
DIRECTORIES = ("agents", "references", "scripts")
EXCLUDED = {
    ".git", ".agents", ".claude", ".codex", "__pycache__", ".DS_Store",
    ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv",
    "venv", "node_modules",
}


def export(output, include_fonts=False):
    requested = Path(output).expanduser()
    if requested.exists() or requested.is_symlink():
        raise ValueError(f"Output already exists (including symlinks): {requested}")
    destination = requested.resolve()
    if destination == SOURCE or SOURCE in destination.parents:
        raise ValueError(f"Output must be outside the source: {destination}")

    entries = []

    def collect(relative):
        item = SOURCE / relative
        if item.name in EXCLUDED or item.suffix in (".pyc", ".pyo"):
            return
        # Reject source links rather than copying external data or retaining loops.
        if item.is_symlink():
            raise ValueError(f"Source symlink is not supported: {relative}")
        if item.is_dir():
            entries.append((relative, True))
            for child in sorted(item.iterdir()):
                collect(child.relative_to(SOURCE))
        elif item.is_file():
            entries.append((relative, False))
        else:
            raise ValueError(f"Missing or unsupported source entry: {relative}")

    for name in FILES:
        if not (SOURCE / name).is_file():
            raise ValueError(f"Required source file is missing: {name}")
        collect(Path(name))
    for name in DIRECTORIES + (("assets/fonts",) if include_fonts else ()):
        if not (SOURCE / name).is_dir():
            raise ValueError(f"Required source directory is missing: {name}")
        collect(Path(name))

    # Reserve a new directory; never merge into a caller's existing output.
    destination.mkdir(parents=True, exist_ok=False)
    try:
        for relative, is_directory in entries:
            target = destination / relative
            if is_directory:
                target.mkdir(parents=True, exist_ok=True)
            else:
                shutil.copy2(SOURCE / relative, target)
    except Exception:
        shutil.rmtree(destination)
        raise
    return destination, sum(not is_directory for _, is_directory in entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="New directory outside this source")
    parser.add_argument("--include-fonts", action="store_true", help="Include assets/fonts")
    args = parser.parse_args()
    try:
        destination, count = export(args.output, args.include_fonts)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Export failed: {error}\n")
    print(f"Exported {count} files to {destination} ({'full' if args.include_fonts else 'light'})")


if __name__ == "__main__":
    main()
