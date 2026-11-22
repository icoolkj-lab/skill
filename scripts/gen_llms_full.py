#!/usr/bin/env python3
"""Generate public/llms-full.txt from source registry and local curated catalog."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES_JSON = ROOT / "data" / "sources" / "SKILL_SOURCES.json"
LOCAL_DATA = ROOT / "data" / "local_skills.json"
LOCAL_CATALOG = ROOT / "docs" / "catalog" / "local-skills.md"
OUT = ROOT / "public" / "llms-full.txt"

sources_doc = json.loads(SOURCES_JSON.read_text(encoding="utf-8"))
local_data = json.loads(LOCAL_DATA.read_text(encoding="utf-8"))
sources = sources_doc.get("sources", {})
local_count = local_data.get("metadata", {}).get("total_skills", 0)
catalog_text = LOCAL_CATALOG.read_text(encoding="utf-8")
start, end = "<!-- LOCAL-SKILLS-START -->", "<!-- LOCAL-SKILLS-END -->"
local_block = catalog_text.split(start, 1)[1].split(end, 1)[0].strip() if start in catalog_text and end in catalog_text else ""

buckets = {}
for repo_path, meta in sources.items():
    owner = repo_path.split("/", 1)[0]
    buckets.setdefault(owner, []).append((repo_path, meta))

lines = []
add = lines.append
add("# llms-full.txt — AI Agent Skill Library")
add("")
add("> Compact, machine-readable directory of upstream skill repositories and local curated Skills.")
add("> Listing is discovery metadata only; it is not a security, quality, license, or commercial-use review.")
add("")
add("## Repository")
add("")
add("- GitHub: https://github.com/icoolkj/skill")
add("- Online search: https://skill.miyucaicai.cn/skills.html")
add("- Local skill index: https://github.com/icoolkj/skill/blob/main/skills/INDEX.md")
add("- Curated catalog: https://github.com/icoolkj/skill/blob/main/docs/catalog/local-skills.md")
add("- Upstream catalog: https://github.com/icoolkj/skill/blob/main/docs/catalog/upstream-skills.md")
add("- ClawHub catalog: https://github.com/icoolkj/skill/blob/main/docs/catalog/clawhub.md")
add("")
add("## Data")
add("")
add("- Upstream source registry: https://github.com/icoolkj/skill/blob/main/data/sources/SKILL_SOURCES.json")
add("- Last updated: " + str(sources_doc.get("last_updated", "unknown")))
add("- Upstream repository entries: " + str(sources_doc.get("total_count", len(sources))))
add("- Local curated Skills: " + str(local_count))
add("")
add("## Upstream repositories")
add("")
for owner in sorted(buckets, key=lambda x: (-len(buckets[x]), x.lower())):
    items = buckets[owner]
    add(f"### {owner} ({len(items)})")
    add("")
    for repo_path, meta in sorted(items):
        url = f"https://github.com/{repo_path}"
        add(f"- [{repo_path}]({url}) — {meta.get('upstream_source', 'source unknown')} — {meta.get('discovered_at', '')[:10]}")
    add("")
add(f"## Local curated Skills ({local_count})")
add("")
if local_block:
    body = re.sub(r"^##\s+💾\s*本地技能库.*$", "", local_block, flags=re.MULTILINE).strip()
    body = re.sub(r"^### ", "#### ", body, flags=re.MULTILINE)
    add(body)
else:
    add("- See the local curated catalog page.")
add("")
add("## Usage and licensing")
add("")
add("- Review each Skill's SKILL.md, scripts, dependencies, network access, source, and license before use.")
add("- Collection does not grant redistribution or commercial rights.")
add("- Cite the library source: https://github.com/icoolkj/skill")
add("")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, {len(lines)} lines)")
