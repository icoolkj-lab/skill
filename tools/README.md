# Tools

## Skill validator

Validate Skill metadata and instructions:

- `python tools/skill_validator.py validate`
- `python tools/skill_validator.py validate skills/<skill-folder>`
- `python tools/skill_validator.py read-properties skills/<skill-folder>`

## Legacy collection updater

The early standalone crawler/updater has been moved to [tools/skill-collection-updater/](skill-collection-updater/). It is separate from current GitHub Actions workflows and is retained for manual use.

## Examples

Optional examples are stored in [tools/examples/](examples/).

## Structure

~~~text
tools/
├── README.md
├── skill_validator.py
├── skill_validator/
├── skill-collection-updater/
└── examples/
~~~
