# 本地精选 Skill 目录

本页是本地精选技能的分类目录，由 scripts/sync_frontend.py 根据 data/local_skills.json 与 public/data/local_skills.json 合并生成。完整描述以结构化数据为准。

<!-- LOCAL-SKILLS-START -->
## 💾 本地技能库

共 **89** 个精选技能，按用途分类（最后同步 2026-11-12，由 `scripts/sync_frontend.py` 自动生成本段）。

### 内容创作与发布（10个）
- **content-creation-publisher** 
- **intelligent-content-system** 
- **article-illustrator** 
- **baoyu-url-to-markdown** 
- **baoyu-format-markdown** 
- **baoyu-post-to-wechat** 
- **baoyu-post-to-x** 
- **baoyu-xhs-images** 
- **wechat-hotspot-publisher** 
- **cy-carousel-skill**  - 给选题交回可直接发布的封面 + 10 页竖版轮播 (1440×1920)。带质检流水线：选题比稿→事实核查回论文/史料→只用开放授权素材→手排逐页→渲染→零错误自检→打包，附置顶评论与来源清单。自带 ELIZA、聪明汉斯等样板。

### 视频创作（13个）
- **video-creation-suite**  - 短视频一站式流水线：脚本→分镜→配音→字幕→成片，覆盖选题到发布的完整创作链路。
- **video-creation-collaborator** 
- **video-creation-pro** 
- **video-recreation** 
- **video-frame-extractor** 
- **viral-video-copywriting** 
- **historical-science-video-prod** 
- **historical-interview-scripts** 
- **three-body-video-creator** 
- **native-subtitle-quote-image**  - 保留视频内嵌原字幕、精确取帧，拼成 3:4 社交平台长图的 Agent Skill。两级 seek 避开长 GOP 跳帧残影，字幕条零间隙；可 Codex/Claude Code 一句话调用或单独跑 Python，附中/英/韩三语 README 与成品案例。
- **ancient-rap-battle**  - 把导演活拆成可复跑流水线：文本层挑历史死对头四句一换韵带典故 + Suno API；画面层生图三视图/特写 + 运镜；MiniMax H3 做口型动作对齐 + 史料注释。需 Claude Code + Suno + Midjourney + MiniMax，一期约 $15。
- **lemo-opuscar**  - 66 套现成风格（art-deco/blueprint/ink-wash/ukiyoe/watercolor 等）+ OPUSCAR 98 奥斯卡特别放映。Canvas/WebGL 逐帧渲染 + 原创配乐 + TTS 旁白，不用视频生成模型/素材库。支持一问一答定制专属风格。Claude Opus 5.5 专用。
- **anything2explainer**  - 任意主题/文章→黑幕运动图形讲解视频（1280×720@30fps，词级字幕/章节进度条/顶部 HUD）。研究→旁白→TTS→时间线对齐→故事板→并行 Remotion 构建→QC，4 检查点；每帧代码绘制不用视频模型，中文云希/英文 kokoro 配音，全程留档。

### 电商与营销（7个）
- **ecommerce-full-pipeline**  - 电商从选品到内容到投放的一站式技能：选品分析、文案、图文、短视频批量产出。
- **pet-commerce-creator** 
- **ecommerce-copywriter** 
- **ecommerce-video-marketing** 
- **product-marketing-copywriter** 
- **product-video-creator** 
- **xiaohongshu-makeup** 

### PPT与演示（6个）
- **NanoBanana-PPT-Skills** 
- **ppt-generator**  - 给一份大纲或主题，直接产出结构化 PPT：逐页标题、要点、配图建议与演讲备注，适合周报、汇报、答辩快速成稿。
- **pptx-generator** 
- **nanobanana-ppt-visualizer** 
- **ppt-roadshow-generator** 
- **remotion-video-enhancer** 

### 语音与音频（3个）
- **tts-voice-synthesis** 
- **qwen3-tts-local** 
- **qwen3-asr-assistant** 

### 数字人与视频配音（6个）
- **infinitetalk** 
- **infinitetalk-shopping-avatar** 
- **digital-avatar-shopping-video** 
- **dream-video-prompt-generator** 
- **agentkit-multimedia-shopping** 
- **srt-whiteboard-animation** 

### 文档与分析（6个）
- **paper-analysis-assistant** 
- **contract-review** 
- **law-to-markdown** 
- **stock-analysis** 
- **ontoly-software-graph** 
- **data-flow-skill** 

### 智能体协作（9个）
- **agent-team**  - 多 Agent 角色分工、任务分发与协同编排，像一支团队一样完成复杂任务。
- **multi-agent-meeting**  - 让多个 Agent 围绕议题基于卡片发言、辩论并产出结论，支持会议卡片溯源。
- **peers-advisory-group** 
- **antinet-security-scan**  - 知易系统的第一道安全闸门。由锦衣卫 Worker 在收到文件/URL 时调用，输出结构化判定(pass/reject)并写入 provenance 留痕，保障数据不出域流水线的前端防线。
- **antinet-doc-parse**  - 知易系统的文档结构化入口。由密卷房 Worker 调用，仅处理已通过安全扫描的本地文件，三级 fallback 依次尝试，输出结构化结果与置信度；数据不出域。
- **antinet-four-color-cards**  - 知易系统的知识记录层。由通政司主调用，把信息拆成蓝卡(事实)、绿卡(解释)、黄卡(风险)、红卡(行动)，黄卡经监察院复核、红卡由丞相府补全策略，全部经太史阁留痕，保证每张卡片可溯源。
- **antinet-provenance**  - 知易系统的证据链与审计层。各官署在关键操作节点写入事件(actor/action/target/trace_id)，支持按 trace_id、时间窗、官署维度检索，支撑审计面板与回滚定位。
- **expert-prompt-migrator** 
- **awesome-jev**  - 只做选择题的极廉价分类模型 Jev，把『先读再筛』倒成『先判再读』：不把全文塞上下文就对批次分类，概率近 0.5 的留人工复核。228 个项目按 6 大场景编目，npx skills add 装完让 Agent 找参考实现。

### 产品与项目管理（2个）
- **product-manager-toolkit** 
- **sales-ai-assistant** 

### 设计与可视化（4个）
- **frontend-design** 
- **ai-drawio**  - 用代码生成 draw.io 流程图/架构图，流程图、时序图、思维导图结构一键成图。
- **pop-up-book-illustration** 
- **web-to-app** 

### AI 创意与可视化（8个）
- **hairline**  - 33 个等轴测细线图形库 + 两个 Agent Skill（hairline-create 把想法生成单文件无依赖 HTML 线框图；hairline-adopt 把 SVG/Logo 重建为可交互线框）。零运行时依赖、约 35 kB、MIT，React/原生 JS 通用。克制风格：只描边、无填充渐变、图内无文字。
- **anatomy**  - 先为概念发明物理对应物（缓存命中=弹子锁、令牌桶=带阀水桶、多画布 GPU=龙门绘图仪），再用等轴测相机与零件库逐件造出可交互 SVG/HTML/React。可叠加 WebGL 着色器，悬停爆炸拆解，零 npm 依赖，自带几何审计与 headless 截图自检。
- **machine-skill**  - 查真实尺寸原理→程序化 three.js 把机器搭进自包含 HTML，推力/转速/温度/流量由内置物理求解器实时计算（涡扇布雷顿循环、火箭喷管、泵性能曲线）。旋转/剖切/爆炸/X 光/慢放/标注/破坏模式，可录 20–30 秒成片。MIT，教学模型非工程计算。
- **RuiC-card-skill**  - 一句话/参考图→画四层图（主体/背景/线稿/文字）→Blender 按景深撑开→镭射材质流光→Three.js 单文件网页。交付网页链接 + card.blend 源工程 + 四层透明 PNG + 配置 + 渲染图 + 验收截图，可拖拽旋转翻面调滑块，四种卡面质感。
- **handraw-style**  - 把 261→290 种手绘风格、161 种排版图型、36 种单色主题全部编号化；看图选编号，输出中英双语生图 Prompt。『编号管画风、主题管内容』，同编号可反复换主题；传参考图限定只借线条/笔触/材质/配色。
- **threejs-scroll-worlds**  - 一个持久 Three.js 世界 + 归一化可逆滚动状态，相机/光照/材质随章节演化。滚动即叙事时间线，适合产品展示与沉浸式官网首屏。
- **scrollytelling-web**  - 固定场景、scrub 时间线、产品拆解、渐进式 3D 揭示，按复杂度在 CSS/Motion/GSAP/Three.js 间选最小引擎。轻量滚动叙事方案。
- **jack-scroll-3d-sites**  - 滚动 scrub 视频或帧序列，Apple 风产品展示，建议 40–150 帧。滚动驱动逐帧播放的 3D 产品演示。

### 文档处理（4个）
- **pptx** 
- **xlsx**  - Excel/xlsx 读写、清洗、透视与公式填充，适合台账、对账与批量报表。
- **pdf**  - PDF 批量转 Markdown、表格抽取、合并拆分与页码重排，把重复劳动一次跑完。
- **docx** 

### 技能管理（2个）
- **find-skill** 
- **skill-creator** 

### 财务分析（3个）
- **creating-financial-models** 
- **market-research-reports** 
- **ledger-tasks-yylo** 

### 文化创作（1个）
- **poetry-music-visual** 

### 邮件与办公自动化（1个）
- **email-concierge** 

### 医疗与行业 Agent（1个）
- **hospital_agent_upgrade** 

### 收录开源技能（4个）
- **archify** 
- **diagram-design** 
- **mattpocock-skills** 
- **srt-whiteboard-animation** 


<!-- LOCAL-SKILLS-END -->
