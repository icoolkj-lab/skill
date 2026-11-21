# Skills 目录规范

本目录存放可独立调用、安装或复用的 Skill 资产。当前以保留上游包结构为主，逐步补齐场景分类与元数据；不会为了统一目录而破坏套件、项目或资源依赖。Skill 创建模板统一存放于仓库根目录 `templates/skill-template/`。

## 目标

- 用户能按业务场景快速找到 Skill。
- 每个独立 Skill 有明确、稳定的目录入口和 `SKILL.md`。
- 集合型 Skill、子 Skill、项目和资源包边界清晰。
- 保留来源、版本、依赖和许可证信息，避免整理时丢失上游资产信息。
- 目录迁移同步更新注册表、文档、脚本、工作流和相对路径。

## 场景分类体系

| 分类 ID | 中文名称 | 范围与典型场景 |
|---|---|---|
| `content-creation` | 内容创作 | 写作、选题、文章、社媒文案、内容策划与发布 |
| `video-production` | 视频创作 | 视频策划、脚本、分镜、生成、剪辑、字幕与复刻 |
| `image-design` | 图片与视觉设计 | 生图、海报、封面、插画、品牌视觉、图表 |
| `office-productivity` | 办公与文档 | Word、PDF、PPT、表格、文档转换与处理 |
| `software-development` | 软件开发 | 编程、代码审查、测试、调试、开发工具与工程流程 |
| `ai-agents` | AI Agent 与协作 | Agent构建、编排、多智能体协作、角色团队 |
| `data-analysis` | 数据分析与研究 | 数据处理、分析、可视化、研究、报告 |
| `marketing-commerce` | 营销与商业 | 电商、营销、销售、产品推广、客户运营 |
| `knowledge-management` | 知识管理 | 知识库、笔记、信息检索、知识整理与沉淀 |
| `automation-integration` | 自动化与集成 | 浏览器、平台操作、工作流、API及工具集成 |
| `professional-domains` | 专业行业应用 | 法律、金融、医疗、教育及其他垂直业务 |
| `skill-development` | Skill 开发与管理 | Skill创建、规范、测试、验证、管理与迁移 |

## 单个 Skill 目录规范

建议新开发的独立 Skill 使用：

```text
<category>/<skill-id>/
├── SKILL.md                 # 必需：入口说明与调用规范
├── references/               # 可选：详细指南、知识材料
├── scripts/                  # 可选：工具脚本
├── assets/                   # 可选：模板、图片、静态资源
├── examples/                 # 可选：示例
└── README.md                 # 可选：项目级说明（仅复杂 Skill）
```

不是所有 Skill 都需要创建全部目录。保持轻量，按实际需求添加。

## SKILL.md 元数据要求

每个独立 Skill 的 `SKILL.md` 开头应使用 YAML frontmatter，至少包含：

```yaml
---
name: skill-id
description: 简明说明它解决什么问题、何时使用。
---
```

建议字段（适用时）：
- `version`
- `author`
- `license`
- `category`
- `tags`
- `compatibility`
- `dependencies`
- `source`

字段应保持可验证；不确定的信息不要猜测或填造。

## 集合型 Skill 与子 Skill

集合目录可以包含多个独立 Skill。集合入口与子 Skill 不是重复资产，应保留层级，例如：

```text
skill-suite/
├── SKILL.md                 # 集合/工作流入口（如确有入口能力）
├── README.md                # 集合介绍、成员导航
└── skills/
    ├── sub-skill-a/
    │   └── SKILL.md
    └── sub-skill-b/
        └── SKILL.md
```

审计时要区分集合入口、子 Skill、辅助脚本、资源和完整项目。不能仅凭文件名或相同内容直接删除。

## 来源与维护规则

1. 新资产先确认它是独立 Skill、集合、项目、工具、资源还是数据。
2. 独立 Skill 进入对应场景分类；集合保留集合边界并在目录索引中标注成员。
3. 原始上游目录结构原则上保留其内部依赖；迁移前检查相对路径、安装说明和引用。
4. 来源、版本、许可证与改造记录写入元数据或资产说明。
5. 不用空目录制造分类；只有该分类有实际资产时再建立目录。
6. 不以同名、相似用途或文件哈希相同为唯一依据删除资产。
7. 分类目录只表达主要应用场景；跨场景能力用标签表达，避免多份复制。

## 当前已迁移目录

以下独立 Skill 已按应用场景完成第一批迁移，内部结构保持原样：

- `content-creation/article-illustrator`
- `content-creation/viral-video-copywriting`
- `marketing-commerce/ecommerce-copywriter`
- `marketing-commerce/product-marketing-copywriter`
- `office-productivity/ppt-generator`
- `office-productivity/pptx-generator`
- `office-productivity/ppt-roadshow-generator`
- `data-analysis/data-storytelling`
- `data-analysis/paper-analysis-assistant`
- `data-analysis/stock-analysis`
- `image-design/icon-generator`

## 第二批迁移目录

- `content-creation/content-research-writer`
- `content-creation/wechat-hotspot-publisher`
- `marketing-commerce/ecommerce-full-pipeline`
- `marketing-commerce/pet-commerce-creator`
- `office-productivity/convert-documents-to-markdown`
- `office-productivity/pdf-processing-pro`
- `ai-agents/agent-team`
- `ai-agents/multi-agent-meeting`
- `software-development/data-flow-skill`

## 视频创作分类迁移

- `video-production/ecommerce-video-marketing`
- `video-production/video-frame-extractor`
- `video-production/video-transcript-downloader`
- `video-production/video-recreation`
- `video-production/video-creation-pro`
- `video-production/video-creation-suite`
- `video-production/video-creation-collaborator`
- `video-production/digital-avatar-shopping-video`
- `video-production/dream-video-prompt-generator`

## 本仓库整理迁移策略

当前仓库包含注册表、搜索索引、应用项目、同步脚本、工作流和历史引用。为避免破坏现有使用：

- **阶段 1：** 盘点与场景分类，建立可追踪目录索引。
- **阶段 2：** 标识集合、独立 Skill、项目、工具和资源；解决重复与版本关系。
- **阶段 3：** 对已确认的独立 Skill 进行物理迁移，逐批更新所有路径引用。
- **阶段 4：** 校验注册表、自动同步、安装路径、文档链接和脚本，再提交迁移。
- **阶段 5：** 维护分类索引，后续新增资产遵循规范。

迁移前，现有路径暂时作为兼容入口，不做一次性大规模移动。
