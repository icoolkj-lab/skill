# Skills 目录

本目录存放收录技能、技能套件和子技能。**找技能请先打开 [INDEX.md 技能导航](INDEX.md)**，不必从目录树逐层翻找。

## 分类目录

- 内容创作：content-creation
- 视频创作：video-production
- 电商与营销：marketing-commerce
- 图片与视觉设计：image-design
- 办公与文档：office-productivity
- 软件开发：software-development
- AI Agent 与协作：ai-agents
- 数据分析与研究：data-analysis
- 知识管理：knowledge-management
- 自动化与集成：automation-integration
- 专业行业应用：professional-domains
- Skill 开发与管理：skill-development
- 语音与音频：audio-production

## 目录原则

- 独立 Skill 的入口是 SKILL.md。
- 套件保留内部层级；明显多余的同名包装目录已整理为更直接的入口。
- 脚本、参考资料、模板、示例和运行资源属于技能包，不因文件多或体积大而删除。
- 分类索引提供查找入口，分类不复制技能文件。
- 来源、许可证、依赖和验证情况应在资产目录维护；未知状态不等于允许使用。

## 新 Skill 推荐结构

~~~text
<skill-id>/
├── SKILL.md
├── references/   # 可选：说明与知识材料
├── scripts/     # 可选：执行脚本
├── assets/      # 可选：静态资源
├── examples/    # 可选：示例
└── README.md    # 复杂技能可选
~~~

## 管理入口

- [技能导航索引](INDEX.md)
- [资产目录](../catalog/README.md)
- [创建模板](../templates/skill-template/)
- [治理规范](../docs/skill-asset-governance.md)
