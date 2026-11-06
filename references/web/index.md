# Web：HIG 审美与按需工程参考

本 skill 以 HIG 为 Web 的通用审美参考，落实到层级、排版、对齐、重点色和视觉反馈。留白、字号、密度和材质按内容与操作需求确定，并延续用户指定风格和已有品牌。框架、组件库和[平台路由](../cross-platform/platform-routing.md)提供工程参考；Fluent、Material 用于查阅行为与能力。

以下资料按当前问题调用：简单调整直接实现，已有合理组件直接沿用，组件选择或风险需要澄清时查场景指导。用户可以直接描述目标。原生客户端映射与跨平台桌面扩展需另行授权。

| 场景层 | 读取 | 何时使用 |
|---|---|---|
| 从自然语言决定交互 | [场景决策](scenario-routing.md) | 组件或交互需要澄清时使用 |
| 找组件及容易混淆的形态 | [组件地图](component-atlas.md) | 按任务检索中文、英文和口语别名 |
| 浮层、反馈、表单、检索和列表详情 | [重点交互模式](interaction-patterns.md) | 确定状态、焦点、退出、恢复和响应式行为 |
| 框架、组件库及专业能力 | [技术选型](stack-selection.md) | 新项目或确有选型需求，不默认重写已有项目 |
| 检查决策是否适应情境 | [场景验收](scenario-evaluation.md) | 用对照场景检验，不只检查关键词 |

产品界面的 HIG 原则可按需查[已有 Foundations 整理](../apple/hig-foundations-patterns.md)和[信息层级](../cross-platform/information-hierarchy.md)，实现采用 Web API。以下 `apple-style-*` 提供可选 Web 实现参考；其中 Apple.com 数值与构图适用于相应展示任务。样式与动效分别处理，共同满足任务、Web 语义和无障碍要求。

| 任务 | 读取 | 范围 |
|---|---|---|
| 信息层级、语义重点色与有效密度 | [信息层级与直观交互](../cross-platform/information-hierarchy.md) | 跨平台推导；保留必要说明、数据摘要和无障碍信息 |
| 设计方向 | [设计哲学](apple-style-philosophy.md) | Apple 风格 Web |
| 样式、排版和布局数值 | [样式 Token](apple-style-tokens.md) | Apple.com 提取与 Web 实现参考 |
| 组件 | [组件模式](apple-style-components.md) | Apple 风格 Web |
| 页面与布局 | [布局模式](apple-style-patterns.md) | Apple 风格 Web |
| 无障碍 | [Web 无障碍](accessibility.md) | 可通用的 Web 指导；平台专属部分仍按来源核对 |
| Tailwind / CSS | [样式配置](apple-style-tailwind-config.md) | Apple 风格 Web |
| 中文字体特殊资源 | [PingFang 字体](pingfang-fonts.md) | 明确需要时使用，不是 Android / Windows 默认字体 |
| 动效参数 | [独立动效规范](apple-style-motion.md) | Apple 风格 Web，不是原生动画时长规范 |
| 动效实现 | [动画模板](apple-style-motion-templates.md) | Web 模板与中性 fallback |

Apple 原生任务请回到 [Apple 索引](../apple/index.md)，不要以 CSS 毛玻璃或 Web 动画替代系统行为。
