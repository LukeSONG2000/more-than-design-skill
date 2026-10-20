# 跨平台路由与语义映射

只在平台选择、共享语义或对应资源任务需要时读取，不默认加载全部平台。

| 任务 | 读取 | 实际范围 |
|---|---|---|
| 选择设计体系、处理冲突 | [平台路由](platform-routing.md) | Android、Windows、Apple、Web |
| 原生与共享层边界 | [平台基线](cross-platform-baseline.md) | 主要是 iOS 26+ 与 Android OEM，不代表完整 Windows 基线 |
| 窗口、输入与能力降级 | [自适应能力](adaptive-platform-capabilities.md) | 主要是 iOS 与 Android；Windows 需另查其平台资料 |
| 组件语义与测试 | [语义组件和测试](semantic-components-testing.md) | 主要是 iOS 与 Android OEM，不代表完整 Windows 测试矩阵 |
| 界面图标 | [图标语义映射](cross-platform-interface-icons.md) | SF Symbols、Material Symbols、Segoe Fluent Icons |
| 应用品牌图标 | [App Icon](cross-platform-app-icons.md) | Apple、Android、Windows 各自生产与验收 |

目标平台入口：[Apple](../apple/index.md)、[Android](../android/index.md)、[Windows](../windows/index.md)、[Web](../web/index.md)。共享业务语义，不共享平台 API 或系统外观；样式和动效分别进入目标平台资料。
