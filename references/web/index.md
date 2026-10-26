# Web：按产品语境选择体系

Web 没有统一的 Apple 默认规范。先服从现有品牌、组件库、技术栈与工作流；未确定体系时读[平台路由](../cross-platform/platform-routing.md)。选用 Fluent 或 Material 时，分别到 [Windows](../windows/index.md) 或 [Android](../android/index.md) 中查 Web 范围，不照搬原生 API。

本目录多数文档是 **Apple 风格 Web 参考**，不是 Apple 原生 HIG 实现，也不是跨平台通用数值标准。

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
