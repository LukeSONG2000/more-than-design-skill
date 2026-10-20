# Apple 原生动效入口

本页只路由原生动效，不另造参数表，也不重复 API 示例。先按目标系统和标准控件行为核对官方来源；Apple 风格 Web 的时长不是原生规范。

| 任务 | 来源与实现 |
|---|---|
| 连续性、目的性和减少动态 | [HIG Motion](https://developer.apple.com/design/human-interface-guidelines/motion)、[HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)；完整来源范围见[官方地图](apple-official-docs-map.md) |
| 加载和进度反馈 | [HIG Loading](https://developer.apple.com/design/human-interface-guidelines/loading)、[组件与输入](hig-components-inputs.md) |
| Liquid Glass 状态变形和转场 | [Liquid Glass 独立动效入口](liquid-glass/motion.md) |
| Live Activities 内容更新 | [实时活动动效章节](apple-live-activities.md#8-动效)，包含系统外壳与内容动画边界、版本差异和 WidgetKit 来源 |
| 原生符号与状态效果 | [界面图标映射](../cross-platform/cross-platform-interface-icons.md)，只读取 Apple / SF Symbols 部分 |

仅在目标是 Web 时使用 [Web 动效参数](../web/apple-style-motion.md)与[Web 动画模板](../web/apple-style-motion-templates.md)。样式另从 [Apple 索引](index.md)或 [Liquid Glass 索引](liquid-glass/index.md)进入。
