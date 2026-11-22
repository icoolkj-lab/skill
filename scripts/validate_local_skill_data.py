#!/usr/bin/env python3
"""Validate curated local-skill data and the README's generated section."""
from __future__ import annotations
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA_PATHS = (ROOT / "data/local_skills.json", ROOT / "public/data/local_skills.json")
CATALOG = ROOT / "docs/catalog/local-skills.md"
START, END = "<!-- LOCAL-SKILLS-START -->", "<!-- LOCAL-SKILLS-END -->"

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)

def main() -> int:
    try:
        data = [json.loads(p.read_text(encoding="utf-8")) for p in DATA_PATHS]
    except Exception as exc:
        fail(f"unable to load curated skill JSON: {exc}")
        return 1
    if data[0] != data[1]:
        fail("data/local_skills.json and public/data/local_skills.json are not synchronized")
        return 1

    catalog = data[0]
    categories = catalog.get("categories", {})
    names = set()
    assignments = 0
    for category, record in categories.items():
        skills = record.get("skills", [])
        if record.get("count") != len(skills):
            fail(f"{category}: count={record.get('count')} but skills array has {len(skills)}")
        if any(not isinstance(name, str) or not name.strip() for name in skills):
            fail(f"{category}: invalid/empty skill name")
        names.update(skills)
        assignments += len(skills)
    expected_total = len(names)
    if catalog.get("metadata", {}).get("total_skills") != expected_total:
        fail(f"metadata.total_skills must equal unique skill count ({expected_total})")
        return 1

    catalog_page = CATALOG.read_text(encoding="utf-8")
    stat = re.search(r"共\s*\*\*(\d+)\*\*\s*个精选技能", catalog_page)
    if not stat or int(stat.group(1)) != expected_total:
        fail(f"local catalog page count must be {expected_total}")
        return 1
    if START not in catalog_page or END not in catalog_page:
        fail("local catalog page is missing section markers")
        return 1
    section = catalog_page.split(START, 1)[1].split(END, 1)[0]
    rendered = {}
    current = None
    for line in section.splitlines():
        heading = re.match(r"^###\s+(.+?)（(\d+)个）\s*$", line)
        if heading:
            current = heading.group(1)
            rendered[current] = []
            if int(heading.group(2)) != len(categories.get(current, {}).get("skills", [])):
                fail(f"local catalog category count mismatch: {current}")
            continue
        bullet = re.match(r"^-\s+\*\*(.+?)\*\*", line)
        if bullet and current is not None:
            rendered[current].append(bullet.group(1))
    if set(rendered) != set(categories):
        fail("local catalog category headings do not match JSON category keys")
    for category, record in categories.items():
        if rendered.get(category, []) != record.get("skills", []):
            fail(f"local catalog skill list mismatch in category: {category}")
    if expected_total != assignments:
        print(f"INFO: {expected_total} unique skills across {assignments} category assignments (multi-category entries allowed)")
    if expected_total == assignments:
        print(f"Validated {expected_total} curated skills across {len(categories)} categories.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
