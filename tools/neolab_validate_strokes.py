#!/usr/bin/env python3
"""Validate a NeoLab raw-ink session without changing it or sending data anywhere."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

DOT_TYPES = {"down", "move", "up", "hover", "info", "error"}
PAGE_FIELDS = ("section", "owner", "book", "page")


def fail(message: str) -> None:
    raise ValueError(message)


def number(value: object, field: str, index: int) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
        fail(f"event {index}: {field} must be a finite number")
    return float(value)


def validate(session: object) -> dict[str, int]:
    if not isinstance(session, dict):
        fail("session must be a JSON object")
    if session.get("schema_version") != "0.1":
        fail("schema_version must be '0.1'")

    page = session.get("page")
    if not isinstance(page, dict):
        fail("page must be an object")
    for field in PAGE_FIELDS:
        value = page.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            fail(f"page.{field} must be a non-negative integer")

    capture = session.get("capture")
    if not isinstance(capture, dict) or not isinstance(capture.get("source_artifact_sha256"), str):
        fail("capture.source_artifact_sha256 is required")
    source_hash = capture["source_artifact_sha256"]
    if len(source_hash) != 64 or any(char not in "0123456789abcdef" for char in source_hash.lower()):
        fail("capture.source_artifact_sha256 must be a SHA-256 hex digest")

    events = session.get("events")
    if not isinstance(events, list) or not events:
        fail("events must be a non-empty list")

    last_timestamp = -1
    pen_down = False
    strokes = 0
    for index, event in enumerate(events):
        if not isinstance(event, dict):
            fail(f"event {index}: must be an object")
        dot_type = event.get("dot_type")
        if dot_type not in DOT_TYPES:
            fail(f"event {index}: invalid dot_type")
        number(event.get("x"), "x", index)
        number(event.get("y"), "y", index)
        pressure = number(event.get("pressure"), "pressure", index)
        if pressure < 0:
            fail(f"event {index}: pressure cannot be negative")
        timestamp = event.get("timestamp_ms")
        if not isinstance(timestamp, int) or isinstance(timestamp, bool) or timestamp < 0:
            fail(f"event {index}: timestamp_ms must be a non-negative integer")
        if timestamp < last_timestamp:
            fail(f"event {index}: timestamp_ms must be non-decreasing")
        last_timestamp = timestamp

        if dot_type == "down":
            if pen_down:
                fail(f"event {index}: received down while a stroke is active")
            pen_down = True
            strokes += 1
        elif dot_type in {"move", "up"} and not pen_down:
            fail(f"event {index}: received {dot_type} before down")
        elif dot_type == "up":
            pen_down = False

    if pen_down:
        fail("session ends with an incomplete stroke")
    return {"events": len(events), "strokes": strokes, "duration_ms": last_timestamp - events[0]["timestamp_ms"]}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a NeoLab raw-ink session")
    parser.add_argument("session", type=Path, help="JSON session file to validate")
    args = parser.parse_args()
    try:
        session = json.loads(args.session.read_text(encoding="utf-8"))
        summary = validate(session)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Invalid: {error}", file=sys.stderr)
        return 1
    print("Valid raw-ink session: " + json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
