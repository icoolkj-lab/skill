#!/usr/bin/env python3
"""Build a provisional registry from SKILL.md files. No network; no mutation of skill assets."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from datetime import date

CATEGORY_MAP = {
    "content-creation":"content-creation", "video-production":"video-production",
    "image-design":"image-design", "office-productivity":"office-productivity",
    "software-development":"software-development", "ai-agents":"ai-agents",
    "data-analysis":"data-analysis", "marketing-commerce":"marketing-commerce",
    "knowledge-management":"knowledge-management", "automation-integration":"automation-integration",
    "professional-domains":"professional-domains", "skill-development":"skill-development"
}
def read_frontmatter(text):
    m=re.match(r"^---\s*\n([\s\S]*?)\n---(?:\s*\n|$)",text)
    if not m: return {}
    result={}
    for line in m.group(1).splitlines():
        match=re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$",line)
        if match:
            result[match.group(1)]=match.group(2).strip().strip('"').strip("'")
    return result
def asset_id(name,path):
    """Readable, deterministic IDs; path digest prevents same-name collisions."""
    candidate=(name or Path(path).parent.name).lower()
    slug=re.sub(r"[^a-z0-9]+","-",candidate).strip("-") or "unnamed-skill"
    digest=hashlib.sha256(path.encode("utf-8")).hexdigest()[:8]
    return f"{slug}-{digest}"
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out",type=Path,default=Path("catalog/registry.json"))
    args=parser.parse_args()
    root=args.root.resolve()
    records=[]
    for file in sorted(root.rglob("SKILL.md")):
        if any(p in {".git","node_modules",".venv","venv","__pycache__"} for p in file.parts): continue
        rel=file.relative_to(root).as_posix()
        try: text=file.read_text(encoding="utf-8")
        except UnicodeDecodeError: text=file.read_text(encoding="utf-8",errors="replace")
        fm=read_frontmatter(text)
        parts=Path(rel).parts
        category=parts[1] if len(parts)>2 and parts[0]=="skills" and parts[1] in CATEGORY_MAP else "uncategorized"
        name=fm.get("name") or Path(rel).parent.name
        asset_type = "template" if rel.startswith("templates/") else ("project" if rel.startswith("projects/") else "skill")
        if asset_type == "template":
            category = "skill-development"
        records.append({
            "id":asset_id(name,rel),"asset_type":asset_type,"name":name,
            "description":fm.get("description",""),"path":rel,"category":category,
            "tags":[],"parent_id":None,"child_ids":[],
            "source":{"repository":None,"url":None,"commit_or_version":None,"collected_at":None,"author":None,"collection_method":None,"notes":"Provisional record; source metadata requires manual verification."},
            "license":{"spdx_id":None,"evidence_path":None,"commercial_use":"unknown","redistribution":"unknown","modification":"unknown","review_notes":"Not yet reviewed; unknown does not grant permission."},
            "compatibility":[],"dependencies":[],"entrypoint":rel,
            "lifecycle_status":"triage","quality_grade":"unrated",
            "review":{"status":"pending","reviewed_at":None,"reviewer":None,"findings":["Provisional record generated from SKILL.md path and frontmatter."]},
            "verification":{"status":"not_tested","tested_at":None,"environment":"","test_notes":""},
            "hashes":{"sha256":None},"created_at":None,"updated_at":date.today().isoformat(),"notes":"Generated automatically; review and enrich before publishing."
        })
    out=args.out if args.out.is_absolute() else root/args.out
    out.parent.mkdir(parents=True,exist_ok=True)
    payload={"schema_version":1,"generated_at":date.today().isoformat(),"repository":"https://github.com/icoolkj/skill","assets":records}
    out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Generated {len(records)} provisional records: {out}")
    print("WARNING: records are provisional; source/license/quality/verification require review.")
if __name__=="__main__": main()
