# Skill 仓库维护与审计

## 维护原则

- 日常整理直接在 `main` 上进行，使用小批量、可回滚的提交。
- 不创建临时整理分支，不要求通过 PR 才能完成仓库内部维护。
- 只删除经过验证的无用文件、字节级重复且不承担独立用途的副本、缓存或系统元数据。
- 保留 Skill 完整包、套件结构、依赖资源、来源和许可证信息。
- 对许可证、来源或运行用途不明确的资产，先保留并核查。
- 每次变更检查相关路径引用、索引、README、脚本和 CI 工作流。

## 只读盘点

在仓库根目录运行：

```bash
python scripts/audit_skill_repository.py
```

生成 JSON 清单：

```bash
python scripts/audit_skill_repository.py --json-out docs/reports/skill-inventory.json
```

扫描项目应统计仓库文件、Skill frontmatter、路径、name、description、内容 SHA-256、重复文件组及系统元数据。扫描工具必须只读，不自动删除、移动或覆盖资产。

## 去重决策

1. 完全重复的入口：核对保留入口、引用、安装关系后才移除副本。
2. 同名不同内容：比较 frontmatter、正文、依赖、脚本、references、版本和来源。
3. 集合与子 Skill：分别保留并登记关系。
4. 项目快照：确认项目是否分叉、独立运行和引用关系后再处理。
5. 共享脚本或素材：若副本服务于独立安装/分发，保留并建立一致性检查。
6. 系统元数据：清理 `._*`、`.DS_Store`、`__MACOSX` 等无效文件，但不误删源码。

## 提交与验证

每批整理使用清晰的 commit message；尽可能运行：

```bash
python scripts/build_skill_catalog.py
python scripts/validate_skill_catalog.py
python scripts/check_skill_mirrors.py
```

并运行涉及项目自身的测试。对 GitHub Actions 的结果，只有在检查实际运行记录后才能标记通过。

## 维护文档

- [仓库结构说明](repository-structure.md)
- [历史清理记录](repository-cleanup-report.md)
- [资产治理规范](skill-asset-governance.md)
