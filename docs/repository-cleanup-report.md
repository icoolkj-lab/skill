# 仓库清理与去重报告

## 1. 审计范围

- 仓库：`icoolkj/skill`
- 基准分支：`main`
- 基准提交：`8957ece68690fe1755862cdb01fd6fc23f6dfacb`
- 工作分支：`chore/skill-repository-cleanup`
- 原则：所有修改只发生在工作分支；不直接修改或合并 `main`。

## 2. 已执行的清理

### 2.1 完全重复的 Skill 入口

删除以下两份完全相同的嵌套 `SKILL.md`，保留规范入口：

- 删除：`skills/awesome-jev/awesome-jev/skills/awesome-jev/SKILL.md`
- 保留：`skills/awesome-jev/awesome-jev/SKILL.md`
- 删除：`skills/native-subtitle-quote-image/native-subtitle-quote-image/skills/native-subtitle-quote-image/SKILL.md`
- 保留：`skills/native-subtitle-quote-image/native-subtitle-quote-image/SKILL.md`

删除前通过 Git Blob SHA 确认内容完全一致。

### 2.2 清理字幕 Skill 的重复嵌套包

删除目录：

`skills/native-subtitle-quote-image/native-subtitle-quote-image/skills/native-subtitle-quote-image/`

该目录中的 10 个配套文件与外层规范 Skill 包中的对应文件逐项 SHA 一致。连同上面单独列出的重复 `SKILL.md`，共清理 11 个重复文件。完整保留的 Skill 包位于：

`skills/native-subtitle-quote-image/native-subtitle-quote-image/`

### 2.3 清理 InfiniteTalk 重复包

核对发现：

- `skills/infinitetalk/SKILL.md` 与 `skills/infinitetalk/infinitetalk/SKILL.md` 的能力正文相同，仅描述文案不同。
- 两套目录的 4 个配套文件（3 份 references、1 个推理脚本）内容完全相同。
- 仓库的双层目录结构已有统一惯例，内层目录包含完整的可安装包。

因此删除外层 5 个文件（外层 `SKILL.md`、3 份 references、1 个脚本），统一保留：

`skills/infinitetalk/infinitetalk/`

### 2.4 清理 macOS 压缩包元数据

删除 19 个 AppleDouble 元数据文件（`._*`），它们位于 `__MACOSX` 目录中，不属于技能源码。

同时在根目录 `.gitignore` 增加：

```gitignore
__MACOSX/
._*
```

原有 `.DS_Store`、`Thumbs.db` 忽略规则保留。

## 3. 最新扫描统计

工作分支最新已核验快照：

| 指标 | 数量 |
|---|---:|
| Git Tree 条目 | 5,174 |
| 文件 Blob | 4,318 |
| 全仓 `SKILL.md` 文件 | 133 |
| 内容完全重复的 `SKILL.md` 组 | 0 |
| 全仓相同内容 Blob 组 | 112 |
| macOS 元数据残留 | 0 |
| `skills/` 一级目录 | 92 |
| 其中包含 `SKILL.md` 的一级目录 | 91 |

`skills/hospital_agent_upgrade/` 没有 `SKILL.md`，但包含完整工程型 Agent 代码，应作为项目资产登记，而不是标准 Skill。

**注意：133 份 `SKILL.md` 不等于 133 个独立 Skill 产品。** 其中包含集合入口、子 Skill、模板、工程项目入口及仓库根目录的 Skill；需要结合 frontmatter、能力和父子关系建立真实目录。

## 4. 为什么没有删除其他相同文件

对全仓文件进行 SHA 比较后，仍有 112 组相同内容（涉及路径可能跨项目、技能包或资源目录）。相同 SHA 只证明文件字节一致，不代表删除其中一份是安全的。代表性情况：

- **根目录与 `projects/companion-simple/`**：存在大量相同文件，但至少 13 个对应文件内容不同，说明两边已分叉；暂不删除任一项目副本。
- **Agent Teams 与独立 Skill**：`antinet-agentteams/skills/` 与 `skills/antinet-*/` 有相同执行脚本，可能分别服务于工程集成和独立安装。
- **内容创作套件**：`article-illustrator` 与 `content-creation-publisher` 共享参考资料；微信/X 发布子技能共享剪贴板脚本，保留自包含安装结构。
- **多个独立 Skill 项目**：`cy-carousel-skill` 与 `native-subtitle-quote-image` 共享 GitHub Issue/Workflow 自动化模板，各自目录都需要这些工作流。
- **图片、字体和示例素材**：相同素材可能分别被不同构建入口引用，暂不抽取公共目录。
- **占位文件**：`.gitkeep`、`.keep`、`.nojekyll` 等零字节文件可能影响目录保留或静态站点发布，不能按重复内容删除。

## 5. 同名不同内容版本的处理决定

### `x-article-publisher`

两份 `SKILL.md` 的 frontmatter `name` 相同，正文各 267 行，仅 4 行有差异（描述及浏览器显示/无头模式示例）。对应项目目录有 16/18 个文件路径可配对，其中 9 个完全相同、7 个内容不同，内层另有 `CONTRIBUTING.md` 和 `README_FULL.md`。

**决定：保留两套。** 它们可能是同一 Skill 的不同版本或分支资产；在版本号、来源和功能差异核实前不合并、不删除。

### `qiaomu-x-article-publisher`

外层与内层项目包含不同的 README、CHANGELOG、LICENSE、metadata 和部分发布脚本。属于需要进一步核验的版本/项目关系，不视为完全重复。

**决定：保留两套，后续核对版本与来源。**

## 6. 本地技能登记数据问题

`data/local_skills.json` 当前数据：

- 18 个分类；
- 分类条目 90 条，唯一技能名称 89 个；
- `srt-whiteboard-animation` 同时出现在“数字人与视频配音”和“收录开源技能”两个分类中，属于跨分类展示，应保留；
- `last_updated` 为 2026-11-12；
- `repository` 字段仍指向上游 `anbeime/skill`；
- `core_skills + sub_skills + system_builtin = 62`，与 `total_skills = 89` 不一致，另有 27 项未被这三个统计字段解释。

登记的 89 个唯一名称与实际 133 份 `SKILL.md` 文件不是同一统计口径。本轮没有擅自重写登记数据，避免误把别名、父级集合、子 Skill 和工程项目合并。

## 7. 本轮新增维护资产

- `docs/repository-structure.md`：解释仓库一级目录及 Skill / 项目 / 数据的边界。
- `docs/skill-repository-maintenance.md`：说明只读审计和安全去重流程。
- `scripts/audit_skill_repository.py`：只读扫描全仓文件、Skill frontmatter 和重复内容；不会删除或移动文件。
- 根目录 `README.md`：增加上述文档入口。

审计脚本支持：

```bash
python scripts/audit_skill_repository.py
python scripts/audit_skill_repository.py --json-out docs/reports/skill-inventory.json
```

## 8. 后续整理顺序

1. 读取剩余 `SKILL.md` 的 `name`、`description` 和正文，建立全量 Skill 目录。
2. 区分独立 Skill、父级集合、子 Skill、模板、系统内置项、工程型 Agent 和普通项目。
3. 逐项核对别名、同名版本和登记缺失项。
4. 明确根目录与 `projects/companion-simple/` 的正式项目归属。
5. 研究 `data/local_skills.json`、`public/data/local_skills.json` 和同步脚本的主从关系，再统一登记数据。
6. 完成路径引用扫描、Skill Validator 和各项目测试后，再决定是否迁移目录或合并项目。

## 9. 验收原则

- 只删除内容完全一致且确认属于冗余副本的文件，或明确的操作系统元数据。
- 不按名称相同直接删除不同版本。
- 不删除独立子 Skill、独立项目、运行依赖或有意义的资源副本。
- 所有整理继续在工作分支完成，最终由仓库维护者审核 PR 后决定是否合并。
