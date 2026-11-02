#!/usr/bin/env python3
"""Validate fixture JSON and required metadata; not protocol conformance."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = sorted((ROOT / "fixtures").rglob("*.json"))
TEMPLATE = ROOT / "docs" / "fixture-template.json"
ALLOWED_STATUS = {"draft", "reviewed", "validated"}
ALLOWED_OUTCOMES = {
    "direct", "transformed", "partial", "lossy", "ambiguous",
    "unsupported", "not-tested", "not tested",
}
REQUIRED = {"fixture_id", "title", "status", "purpose", "sources", "input", "expected", "limitations"}

errors = []
seen_ids = {}
files = FIXTURES + ([TEMPLATE] if TEMPLATE.exists() else [])
for path in files:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        continue

    if path == TEMPLATE:
        # Template placeholders are intentionally not treated as a complete fixture.
        continue
    if not isinstance(data, dict):
        errors.append(f"{path.relative_to(ROOT)}: root must be an object")
        continue

    missing = REQUIRED - data.keys()
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing fields: {', '.join(sorted(missing))}")
    fixture_id = data.get("fixture_id")
    if not isinstance(fixture_id, str) or not fixture_id.strip():
        errors.append(f"{path.relative_to(ROOT)}: fixture_id must be a non-empty string")
    elif fixture_id in seen_ids:
        errors.append(
            f"{path.relative_to(ROOT)}: duplicate fixture_id {fixture_id!r} "
            f"(also in {seen_ids[fixture_id].relative_to(ROOT)})"
        )
    else:
        seen_ids[fixture_id] = path

    for field in ("title", "purpose"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"{path.relative_to(ROOT)}: {field} must be a non-empty string")
    if not isinstance(data.get("input"), dict):
        errors.append(f"{path.relative_to(ROOT)}: input must be an object")
    if data.get("status") not in ALLOWED_STATUS:
        errors.append(f"{path.relative_to(ROOT)}: status must be one of {sorted(ALLOWED_STATUS)}")
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append(f"{path.relative_to(ROOT)}: sources must be a non-empty list")
    else:
        for i, source in enumerate(sources):
            if not isinstance(source, dict) or not all(source.get(k) for k in ("protocol", "version", "url")):
                errors.append(f"{path.relative_to(ROOT)}: source[{i}] needs protocol, version, and url")
    expected = data.get("expected")
    if not isinstance(expected, dict) or expected.get("outcome") not in ALLOWED_OUTCOMES:
        errors.append(f"{path.relative_to(ROOT)}: expected.outcome must be one of {sorted(ALLOWED_OUTCOMES)}")
    elif not isinstance(expected.get("description"), str) or not expected["description"].strip():
        errors.append(f"{path.relative_to(ROOT)}: expected.description must be a non-empty string")
    if not isinstance(data.get("limitations"), list) or not data.get("limitations"):
        errors.append(f"{path.relative_to(ROOT)}: limitations must be a non-empty list")

if errors:
    print("Fixture validation failed:")
    print("\n".join(errors))
    sys.exit(1)

print(f"Validated JSON syntax and metadata for {len(FIXTURES)} fixture(s).")
print("Note: this does not establish protocol conformance or mapping correctness.")
