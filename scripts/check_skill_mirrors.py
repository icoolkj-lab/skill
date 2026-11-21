#!/usr/bin/env python3
"""Verify packaged Antinet standalone skill script mirrors stay in sync."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    ("antinet-agentteams/skills/doc-parse/scripts/run_doc_parse.py",
     "skills/antinet-doc-parse/scripts/run_doc_parse.py"),
    ("antinet-agentteams/skills/four-color-cards/scripts/run_four_color_cards.py",
     "skills/antinet-four-color-cards/scripts/run_four_color_cards.py"),
    ("antinet-agentteams/skills/provenance/scripts/run_provenance.py",
     "skills/antinet-provenance/scripts/run_provenance.py"),
    ("antinet-agentteams/skills/security-scan/scripts/run_security_scan.py",
     "skills/antinet-security-scan/scripts/run_security_scan.py"),
)

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    failures = []
    for source, packaged in PAIRS:
        a, b = ROOT / source, ROOT / packaged
        if not a.is_file() or not b.is_file():
            failures.append(f"missing mirror: {source} or {packaged}")
            continue
        if digest(a) != digest(b):
            failures.append(f"out of sync: {source} != {packaged}")
        else:
            print(f"OK mirror: {packaged}")
    if failures:
        for item in failures:
            print(f"ERROR: {item}", file=sys.stderr)
        return 1
    print(f"Validated {len(PAIRS)} packaged script mirrors.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
