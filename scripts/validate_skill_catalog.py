#!/usr/bin/env python3
"""Dependency-free checks for catalog registry integrity and local Skill entrypoints."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument("--registry",type=Path,default=Path("catalog/registry.json"))
    args=p.parse_args()
    root=args.root.resolve()
    registry=args.registry if args.registry.is_absolute() else root/args.registry
    errors=[]; warnings=[]
    try: data=json.loads(registry.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: cannot read registry: {e}"); return 2
    assets=data.get("assets")
    if not isinstance(assets,list): errors.append("registry.assets must be an array"); assets=[]
    seen_ids=set(); seen_paths=set()
    for i,a in enumerate(assets):
        prefix=f"assets[{i}]"
        aid=a.get("id")
        path=a.get("path")
        if not aid: errors.append(f"{prefix}: missing id")
        elif aid in seen_ids: errors.append(f"{prefix}: duplicate id {aid}")
        seen_ids.add(aid)
        if not path: errors.append(f"{prefix}: missing path")
        elif path in seen_paths: errors.append(f"{prefix}: duplicate path {path}")
        seen_paths.add(path)
        if path:
            target=(root/path).resolve()
            if not target.is_relative_to(root): errors.append(f"{prefix}: path escapes repository: {path}")
            elif not target.exists(): errors.append(f"{prefix}: path does not exist: {path}")
            elif target.name=="SKILL.md":
                text=target.read_text(encoding="utf-8",errors="replace")
                fm=re.match(r"^---\\s*\\n([\\s\\S]*?)\\n---(?:\\s*\\n|$)",text)
                if not fm: warnings.append(f"{path}: no parseable frontmatter")
                else:
                    keys={m.group(1) for line in fm.group(1).splitlines() if (m:=re.match(r"^([A-Za-z0-9_-]+):",line))}
                    if "name" not in keys: warnings.append(f"{path}: frontmatter missing name")
                    if "description" not in keys: warnings.append(f"{path}: frontmatter missing description")
    print(f"Registry assets: {len(assets)}")
    for w in warnings: print("WARN:",w)
    for e in errors: print("ERROR:",e)
    if errors: return 1
    print("Registry integrity checks passed.")
    return 0
if __name__=="__main__": raise SystemExit(main())
