# 仓库清理与去重报告

## 本轮范围

- 仓库：`icoolkj/skill`
- 基准分支：`main`
- 基准提交：`8957ece68690fe1755862cdb01fd6fc23f6dfacb`
- 工作分支：`chore/skill-repository-cleanup`
- 原则：只在工作分支修改；不直接修改或合并 `main`。

## 已完成清理

### 1. 完全重复的 Skill 入口

删除以下嵌套副本，保留外层规范入口：

- `skills/awesome-jev/awesome-jev/skills/awesome-jev/SKILL.md`
- `skills/native-subtitle-quote-image/native-subtitle-quote-image/skills/native-subtitle-quote-image/SKILL.md`

这两份文件与各自外层 `SKILL.md` 的 Git Blob SHA 完全一致。

### 2. 重复打包的字幕 Skill 子目录

删除 `skills/native-subtitle-quote-image/native-subtitle-quote-image/skills/native-subtitle-quote-image/` 下 10 个文件。逐项核对后，这 10 个文件都与外层规范 Skill 目录中的对应文件 SHA 完全一致。

保留的规范目录为：

`skills/native-subtitle-quote-image/native-subtitle-quote-image/`

### 3. macOS 压缩包元数据

删除 19 个 `__MACOSX` 目录中的 AppleDouble 元数据文件（`._*`），包括 `anything-to-notebooklm` 和 `chrome-automation` 目录下的系统元数据。这些不是 Skill 功能文件。

## 当前扫描结果

清理后在工作分支重新扫描：

- Git Tree 条目：5,179（包含本报告和仓库结构说明两份新增文档）
- `SKILL.md` 文件：134
- `SKILL.md` 内容完全重复组：0
- `skills/` 一级目录：92
- 其中包含 `SKILL.md` 的一级目录：91
- 当前无 `SKILL.md` 的一级目录：`hospital_agent_upgrade`（它是工程型 Agent 项目，不是标准 Skill）
- `__MACOSX` / AppleDouble 元数据残留：0

134 份 `SKILL.md` 不等于 134 个独立产品：其中包含模板、父级集合入口、嵌套子 Skill、工程项目入口和其他目录中的 Skill。下一步必须基于 frontmatter、功能和父子关系建立规范目录，不能只按文件数计数。

## 有意保留的相同文件

全仓还存在其他 SHA 相同的文件。它们不应自动删除，原因包括：

- `projects/companion-simple/` 与根目录存在大量相同文件，但也有 13 个对应文件内容不同，说明两边已经分叉，不能把整个项目目录当成纯副本删除。
- `antinet-agentteams/skills/` 与 `skills/antinet-*/` 中存在相同执行脚本，可能分别服务于 Agent Teams 工程和独立 Skill 分发。
- `content-creation-publisher` 与独立 `article-illustrator` 之间存在相同参考文件，可能是独立安装包的自包含副本。
- 多个视频创作 Skill 共享脚本和参考资料，可能是套件间复用或打包依赖。
- `infinitetalk`、`qiaomu-x-article-publisher` 等目录存在镜像/嵌套结构，需结合版本、入口和引用进一步判断。

这些文件目前只记录为“待核验重复资源”，不做删除。

## 登记数据问题（未擅自改写）

`data/local_skills.json` 当前登记：

- 18 个分类
- 分类条目 90 条
- 去重后的名称 89 个
- `srt-whiteboard-animation` 重复登记 1 次
- `last_updated` 为 2026-11-12
- `repository` 字段仍指向上游 `anbeime/skill`
- `core_skills + sub_skills + system_builtin = 62`，与 `total_skills = 89` 不一致，另有 27 项未在这三个统计字段中解释

登记的 89 个名称与实际 134 份 Skill 文档不是同一统计口径。当前没有直接重写登记表，以免把别名、父级集合、子 Skill 和工程项目误合并。

## 下一阶段建议

1. 逐份读取剩余 `SKILL.md` 的 `name`、`description` 和正文能力，生成真实目录。
2. 识别集合入口、独立子 Skill、模板、Agent 项目、系统内置项和非 Skill 工程。
3. 对同名不同内容的版本做逐项比较，不按文件名删除。
4. 建立规范化目录索引、别名表、父子关系表和重复资源清单。
5. 根据引用扫描结果，再决定是否迁移根目录历史文档、镜像项目或资源文件。
6. 修正 `local_skills.json`、README 和前端索引，并验证自动同步脚本。

## 验收原则

- 所有被删除文件都有完全相同的保留副本，或明确属于操作系统元数据。
- 不删除独立子 Skill、独立项目、运行依赖或不同版本。
- 不在本轮合并主分支。
