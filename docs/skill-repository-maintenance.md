# Skill 仓库维护与审计

## 只读盘点

在仓库根目录运行：

```bash
python scripts/audit_skill_repository.py
```

生成完整 JSON 清单：

```bash
python scripts/audit_skill_repository.py --json-out docs/reports/skill-inventory.json
```

脚本会统计：

- 仓库文件总数；
- 全仓 `SKILL.md` 数量及 frontmatter；
- 每个 Skill 的路径、`name`、`description` 和 SHA-256；
- 内容完全相同的文件组；
- 完全重复的 Skill 文档组；
- macOS `__MACOSX`、`._*`、`.DS_Store` 元数据文件。

脚本只读扫描，不会自动删除、移动或覆盖文件。相同 SHA 只代表文件字节完全一致，不代表这些文件可以安全删除。

## 去重决策规则

1. **完全相同的重复 Skill 入口**：确认保留路径、安装入口、引用和工作流后，才删除多余副本。
2. **同名不同内容**：先比较 frontmatter、正文、依赖、脚本、参考资料和版本信息；不得按名称直接删除。
3. **集合与子 Skill**：父级入口和子级能力分别登记，不把它们当作重复。
4. **项目镜像**：根目录和 `projects/` 下的文件即使 SHA 相同，也要先确认项目是否分叉、构建是否依赖两处路径。
5. **共享脚本/素材**：确认运行时引用后再考虑抽取公共目录；否则保留独立包内副本，保证 Skill 可单独安装。
6. **系统元数据**：`._*`、`.DS_Store` 和 `__MACOSX` 内容可清理，但先确认不包含真实源码文件。

## 推荐操作流程

1. 在独立分支执行只读盘点。
2. 检查重复组并给出“可删除 / 保留 / 待核验”结论。
3. 每批只处理一类文件，提交独立 Commit。
4. 扫描所有相对路径、README 安装命令、索引 JSON 和 GitHub Actions 引用。
5. 运行 Skill Validator 和项目自身测试。
6. 比较整理前后的清单、文件数量与 Git diff。
7. 完成验收后再创建 PR，由仓库维护者决定是否合并。

## 当前维护文档

- [仓库结构说明](repository-structure.md)
- [仓库清理与去重报告](repository-cleanup-report.md)
