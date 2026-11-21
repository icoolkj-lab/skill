# Skill 仓库结构说明

本仓库以 **Skill 资产** 为核心。所有技能均按照应用场景归类，目录不再设置“独立项目”分类。

## 一级目录

| 路径 | 用途 |
|---|---|
| `skills/` | 全部 Skill 源码、技能集合与子 Skill，按应用场景分类 |
| `data/` | 技能登记数据、搜索索引和同步数据 |
| `public/` | 技能商店前端及公开数据 |
| `scripts/` | 索引同步、整理、维护及自动化脚本 |
| `tools/` | Skill 验证、开发辅助工具 |
| `docs/` | Skill 使用规范、场景清单、审计和维护文档 |
| `templates/` | Skill 创建模板及通用模板资源 |
| `images/` | 文档与仓库展示所需图片 |
| `.github/` | 仓库工作流、自动化配置及贡献模板 |

## Skill 场景分类

`skills/` 采用以下场景分类：

- `content-creation/`：内容创作
- `video-production/`：视频创作
- `image-design/`：图片与视觉设计
- `office-productivity/`：办公与文档
- `software-development/`：软件开发
- `ai-agents/`：AI Agent 与协作
- `data-analysis/`：数据分析与研究
- `marketing-commerce/`：营销与商业
- `knowledge-management/`：知识管理
- `automation-integration/`：自动化与集成
- `professional-domains/`：专业行业应用
- `skill-development/`：Skill 开发与管理

## Skill 资产组织规则

1. 每项 Skill 归入最适合其主要应用场景的分类。
2. 独立 Skill 保留自己的入口 `SKILL.md` 与必要脚本、references、assets、examples。
3. Skill 集合及多子技能结构保留父级入口和内部子技能，不强行扁平化。
4. 完整代码、工具或素材如果是 Skill 的运行依赖，放在该 Skill 包内。
5. 无法合理归属于 Skill 的非技能内容，需审查其用途；不为其建立“项目”分类。
6. 同名不同版本或重复文件，先核实内容、来源、引用和安装关系再决定合并或删除。

## 迁移约定

- 迁移按场景分批进行，保留 Skill 内部相对结构。
- 同步更新 README、登记数据、脚本、工作流、安装说明和路径引用。
- 分类目录 README 提供场景介绍和技能导航。
- 全量迁移及引用验证完成后，统一整理主分支目录结构。
