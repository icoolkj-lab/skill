#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""只读扫描 Skill 仓库：统计 SKILL.md、frontmatter、重复文件和 macOS 元数据。

本工具只生成报告，不移动、覆盖或删除任何仓库文件。
用法：
  python scripts/audit_skill_repository.py
  python scripts/audit_skill_repository.py --json-out docs/reports/skill-inventory.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if field:
            value = field.group(2).strip().strip("\"'")
            result[field.group(1)] = value
    return result


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-out", type=Path, help="可选：将完整 JSON 报告写入指定路径")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"仓库目录不存在：{root}")

    files = list(iter_files(root))
    skill_docs = []
    hashes: dict[str, list[str]] = defaultdict(list)
    apple_metadata = []

    for path in files:
        relative = path.relative_to(root).as_posix()
        digest = sha256(path)
        hashes[digest].append(relative)

        if "__MACOSX" in path.parts or path.name.startswith("._") or path.name == ".DS_Store":
            apple_metadata.append(relative)

        if path.name == "SKILL.md":
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                content = path.read_text(encoding="utf-8", errors="replace")
            meta = frontmatter(content)
            skill_docs.append({
                "path": relative,
                "name": meta.get("name", ""),
                "description": meta.get("description", ""),
                "has_frontmatter": bool(meta),
                "sha256": digest,
            })

    duplicate_groups = [
        {"sha256": digest, "paths": sorted(paths)}
        for digest, paths in hashes.items()
        if len(paths) > 1
    ]
    duplicate_skill_docs = [
        group for group in duplicate_groups
        if sum(path.endswith("/SKILL.md") or path == "SKILL.md" for path in group["paths"]) > 1
    ]

    report: dict[str, Any] = {
        "repository_root": str(root),
        "summary": {
            "files_scanned": len(files),
            "skill_md_count": len(skill_docs),
            "skill_docs_without_frontmatter": sum(not item["has_frontmatter"] for item in skill_docs),
            "duplicate_blob_groups": len(duplicate_groups),
            "duplicate_skill_doc_groups": len(duplicate_skill_docs),
            "macos_metadata_files": len(apple_metadata),
        },
        "skills": sorted(skill_docs, key=lambda item: item["path"]),
        "duplicate_blob_groups": sorted(duplicate_groups, key=lambda item: item["paths"][0]),
        "duplicate_skill_doc_groups": duplicate_skill_docs,
        "macos_metadata_files": sorted(apple_metadata),
        "safety_note": "只读扫描；不会自动删除或修改任何文件。相同 SHA 仅表示内容相同，不代表可以安全删除。",
    }

    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    if args.json_out:
        output = args.json_out if args.json_out.is_absolute() else root / args.json_out
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"完整报告已写入：{output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
