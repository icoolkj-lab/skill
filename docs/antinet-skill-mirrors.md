# Antinet Skill 镜像说明

四个 Antinet Worker 的独立包与 AgentTeams 套件中保留了对应脚本副本：

| AgentTeams 源路径 | 独立发行包 |
|---|---|
| `antinet-agentteams/skills/doc-parse` | `skills/antinet-doc-parse` |
| `antinet-agentteams/skills/four-color-cards` | `skills/antinet-four-color-cards` |
| `antinet-agentteams/skills/provenance` | `skills/antinet-provenance` |
| `antinet-agentteams/skills/security-scan` | `skills/antinet-security-scan` |

这不是可随意删除的重复文件：套件内路径供 AgentTeams 项目使用，`skills/` 下的包用于独立安装/分发，且发行包包含各自的许可证文件。为避免维护漂移，脚本必须保持字节级一致。

运行检查：

```bash
python scripts/check_skill_mirrors.py
```

该检查已纳入 Skill Catalog Validation 工作流。
