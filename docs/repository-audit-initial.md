# Repository Governance Audit — Initial Snapshot

Audit target: `icoolkj/skill`, branch `main`.
Snapshot after governance commit: `91ff63597215e137a4ca5d2969830d99d822d32c`.

## Inventory

- Git tree entries: 5,198
- File blobs: 4,332
- `SKILL.md` entrypoints: 133
- Total tracked size estimated from Git tree blob sizes: approximately 523 MB.
- `skills/`: 3,850 files; approximately 288 MB.
- `projects/`: 215 files; approximately 235 MB.
- `docs/`: 18 files; about 170 KB.
- No obvious tracked cache artifacts detected by path-pattern scan (`node_modules`, `__pycache__`, `.pyc`, `.DS_Store`, `__MACOSX`, etc.). This does not replace content-level inspection.

## Main structural findings

1. **Collection library and product/application repository are mixed.** Root includes a number of standalone application files, a large `projects/` directory, deployment/config docs, web UI assets and crawler/scheduler implementation. These are not Skill assets. They may be necessary for the repository's skill-store website or synchronization service, so they must be assessed by function before relocation.
2. **Skill path conventions are inconsistent.** Examples include flat entries, nested upstream package roots, category/subskill suites, and parent suite entrypoints. Avoid bulk flattening.
3. **133 entrypoints do not mean 133 unique installable skills.** Some are suites, subskills, templates, application projects, and nested imported packages.
4. **Large files require purpose review, not automatic deletion.** Examples include project demo videos/archives and bundled fonts or demos inside Skills. The latter may be runtime dependencies or intentional examples.
5. **Catalog and local collection metadata diverge.** The local JSON inventory and physical Skill tree have different counts and scopes. Treat them as distinct data sources until a reconciliation process is designed.
6. **Third-party licensing needs item-level evidence.** Existing license summary is a useful starting point but must be checked against current paths, upstream files, and redistributed content.

## Safe remediation priorities

### P0 — Management foundations
- Establish catalog schema, category vocabulary, relation tracking and governance workflow.
- Add provisional catalog builder; generated entries are triage-only and must not claim provenance, license or test status.
- Preserve all assets while classifying asset type and source.

### P1 — Reconciliation and quality
- Generate catalog and reconcile 133 entrypoints with existing `data/local_skills.json`, `public/data/skills.json`, source list and README indexes.
- Identify invalid/missing frontmatter, duplicate IDs/names, suite/subskill relationships, missing source/license evidence.
- Build tests for paths and references.

### P2 — Directory cleanup
- Review root-level non-Skill files and `projects/` by functionality and ownership.
- Remove only confirmed junk, duplicates, abandoned artifacts, or redundant backups.
- Avoid moving the web app/crawler/scheduler into Skill folders unless they are actually a reusable Skill.

### P3 — Usability
- Generate category indexes and searchable catalog from registry.
- Provide collection intake and install/use quick guides.
- Add CI checks for frontmatter, references, IDs, and secret patterns.

## High-volume / large asset review

The largest items include project demo videos and ZIPs, large bundled font files, GIF demos, and image assets. These need usage checks and licensing/redistribution checks. Do not delete them based on size alone.

## Scope caveat

This snapshot is a Git tree/path/size audit. It is not yet a complete semantic review of every Skill, script, license, dependency, binary, or runtime behavior. The next audit stage must examine Skill frontmatter and package contents systematically, then produce per-asset review records.
