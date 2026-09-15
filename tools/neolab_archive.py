#!/usr/bin/env python3
"""Create a privacy-preserving inventory of NeoLab recovery files.

The program reads files only. It never extracts archives, modifies input,
uploads data, or sends network requests.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def archive_entries(path: Path) -> dict[str, object] | None:
    """Return ZIP names only; do not extract or inspect file contents."""
    if not zipfile.is_zipfile(path):
        return None
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
        return {"format": "zip", "entry_count": len(names), "entries": names}
    except (OSError, zipfile.BadZipFile) as error:
        return {"format": "zip", "error": str(error)}


def record(path: Path) -> dict[str, object]:
    details = path.stat()
    result: dict[str, object] = {
        "relative_path": str(path),
        "size_bytes": details.st_size,
        "modified_at": datetime.fromtimestamp(details.st_mtime, timezone.utc).isoformat(),
        "extension": path.suffix.lower(),
        "sha256": sha256(path),
    }
    contents = archive_entries(path)
    if contents is not None:
        result["container"] = contents
    return result


def input_files(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    if source.is_dir():
        return sorted(path for path in source.rglob("*") if path.is_file())
    raise FileNotFoundError(f"Input path does not exist: {source}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only recovery-file inventory")
    parser.add_argument("source", type=Path, help="A source file or directory")
    parser.add_argument("--output", type=Path, required=True, help="Local JSON manifest path")
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()
    if output == source or output.is_relative_to(source):
        parser.error("Output must be outside the source file/directory.")

    files = input_files(source)
    manifest = {
        "schema_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source": str(source),
        "file_count": len(files),
        "files": [record(path) for path in files],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Inventoried {len(files)} file(s): {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
