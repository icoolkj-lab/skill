# Skill Asset Catalog

This catalog is the authoritative management layer for the collected Skill assets in this repository.

- `registry.json`: machine-readable records for each managed asset.
- `schema/skill-record.schema.json`: JSON Schema for registry records.
- `categories.json`: controlled category vocabulary.
- `tags.json`: tag vocabulary and guidance.
- `relations.json`: optional links between suites, sub-skills, dependencies, and alternatives.

## Lifecycle

`incoming → triage → reviewed → verified → published → archived`

Not every collected asset is an executable Skill. Use `asset_type` to distinguish skills, skill suites, tools, projects, templates, datasets, and reference material.

Registry entries must not invent provenance, author, license, version, compatibility, or verification claims. Use `unknown` / `not_checked` where evidence is absent.

The registry is intended to be generated and validated by maintenance tools. Avoid hand-maintaining derived statistics.
