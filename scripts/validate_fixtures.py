#!/usr/bin/env python3
"""Parse JSON fixtures and template files; this is not protocol conformance."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted((ROOT / "fixtures").rglob("*.json")) + sorted((ROOT / "docs").glob("fixture-template.json"))

errors = []
for path in FILES:
    try:
        with path.open(encoding="utf-8") as stream:
            json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")

if errors:
    print("Fixture JSON validation failed:")
    print("\n".join(errors))
    sys.exit(1)

print(f"Validated JSON syntax in {len(FILES)} file(s).")
print("Note: JSON parsing does not establish protocol compatibility.")
