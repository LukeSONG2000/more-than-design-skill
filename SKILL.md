---
name: more-than-design-skill
description: Use with frontend-design for platform-aware UI across Android/Material, Windows/Fluent, Apple/HIG, and context-sensitive web; keep native behavior, visual style, and motion distinct.
license: MIT
version: 1.4.0
author: LukeSONG2000
category: productivity
tags:
  - frontend
  - docs
  - planning
  - analysis
metadata:
  version: 1.4.0
  category: productivity
  tags:
    - frontend
    - docs
    - planning
    - analysis
  namespace: "@LukeSONG2000"
  description_zh: frontend-design 的多平台设计伴随参考层：按 Android/Material、Windows/Microsoft Fluent、Apple/HIG 和 Web 项目语境路由官方规范，并分离样式、组件、行为与动效。
  author: LukeSONG2000
  homepage: https://github.com/LukeSONG2000/more-than-design-skill
  compatibility:
    claude_code: true
    codex: true
  claude:
    legacy_name: more-than-design
    auto_activate: false
---

# More Than Design

在前端与客户端设计任务中，把目标平台的官方规范变成可执行的设计和实现约束。本 skill 与 `frontend-design` 同时使用：`frontend-design` 负责创意与实现，本 skill 负责平台路由、官方资料检索、组件语义、动效边界、跨平台翻译和验收。

## 先判定平台

| 目标 | 默认设计体系 | 默认开发体系 | 首读 |
|---|---|---|---|
| Android 手机、平板、折叠屏 | [Android Mobile Design](https://developer.android.google.cn/design/ui/mobile) + [Material 3](https://m3.material.io/) | [Android Adaptive Apps](https://developer.android.com/develop/adaptive-apps) + Jetpack Compose Material 3，必要时 Android Views | [19-google-android-map.md](references/19-google-android-map.md)；折叠屏另读 [30-android-foldable-adaptation.md](references/30-android-foldable-adaptation.md) |
| Windows 桌面应用 | [Windows Design](https://learn.microsoft.com/en-us/windows/apps/design/) + [Fluent 2](https://fluent2.microsoft.design/) | [WinUI 3](https://learn.microsoft.com/windows/apps/winui/winui3/) + Windows App SDK | [23-microsoft-windows-map.md](references/23-microsoft-windows-map.md) |
| iPhone、iPhone Duo、iPad、Mac、Watch、TV、Vision、CarPlay | [Apple Design / HIG](https://developer.apple.com/cn/design/) | [Apple Developer Documentation](https://developer.apple.com/documentation/) | [10-apple-official-docs-map.md](references/10-apple-official-docs-map.md)；Duo 另读 [29-iphone-duo-adaptation.md](references/29-iphone-duo-adaptation.md) |
| Web | 按产品语境选择，不固定套用一个体系 | 项目现有框架优先 | [18-platform-routing.md](references/18-platform-routing.md) |

目标平台规则优先于视觉偏好。Android 不复刻 iOS 控件解剖，Windows 不套移动端导航，Apple 平台不以 Web 毛玻璃模拟系统材质。

## Web 选择规则

Web 没有单一默认体系。先服从现有产品、代码库和品牌，再按以下顺序判断；语境相同且无其他约束时，偏好为 Apple > Microsoft > Google。

- 消费产品、内容展示、创意工具、硬件或品牌叙事：优先 Apple 的内容层级、克制材料和连续动效。
- 企业软件、生产力工具、桌面密集工作台、多窗格和键鼠工作流：优先 Microsoft Fluent。
- 移动优先、跨尺寸应用、明确的组件系统、动态主题或 Google 生态：优先 Material 3。
- 可借用另一体系的原则，但同一操作面不要混合相互竞争的组件结构、状态模型或导航语义。

完整决策树、冲突处理和跨平台翻译见 [18-platform-routing.md](references/18-platform-routing.md)。

针对 iOS 26+ 与 Android OEM 碎片化场景，补充阅读 [26-cross-platform-baseline.md](references/26-cross-platform-baseline.md)、[27-adaptive-platform-capabilities.md](references/27-adaptive-platform-capabilities.md) 和 [28-semantic-components-testing.md](references/28-semantic-components-testing.md)。涉及 iPhone Duo 时必须再读 [29-iphone-duo-adaptation.md](references/29-iphone-duo-adaptation.md)；涉及 Android 折叠屏时必须再读 [30-android-foldable-adaptation.md](references/30-android-foldable-adaptation.md)。

涉及界面图标时读取 [31-cross-platform-interface-icons.md](references/31-cross-platform-interface-icons.md)，按语义分别解析为 SF Symbols、Material Symbols 或 Segoe Fluent Icons。涉及应用品牌图标时读取 [32-cross-platform-app-icons.md](references/32-cross-platform-app-icons.md)，不要把界面 Symbol、商店图标、平台实渲 App Icon 和应用内 Logo 混为同一资产。

## 调用流程

1. 确认运行平台、输入方式、窗口形态、技术栈和已有设计系统。
2. 从对应官方地图进入，不凭记忆套 Token；优先标准控件和平台组件。
3. 将需求拆成 `foundation/style`、`component`、`behavior/pattern`、`motion`、`accessibility` 五类。
4. 样式与动效分别查阅和实现。视觉数值不能代替交互行为，动效参数不能掩盖错误组件。
5. 只把可迁移原则带到其他平台；把平台 API、系统材质、系统导航和硬件输入留在原平台。
6. 按键盘、触摸、指针、屏幕阅读器、减少动态、深浅色、高对比度和窗口变化验收。
7. 输出设计依据时链接到本 skill 中列出的官方原文，不把二手总结当规范来源。

## 核心约束

### 原生优先

- Android：优先 Material 3 组件、系统返回、edge-to-edge、WindowInsets 和动态颜色；不要重绘系统行为。
- Windows：优先 WinUI 控件、标题栏、命令系统、键盘/指针语义和 Mica/Acrylic 的官方用法。
- Apple：优先 SwiftUI/UIKit/AppKit 标准控件。Liquid Glass 的系统组件外观与转场由系统负责，自定义玻璃只用于官方允许的自定义视图场景。
- Web：使用项目现有组件库；从平台体系借语义、层级和动效，不伪装成不可用的系统控件。

### 样式与动效分离

- 样式包含颜色、字体、间距、形状、图标、材质和 elevation。
- 动效包含状态变化、空间移动、转场、物理参数、编舞和 reduced motion。
- Material 动效见 [22-material-motion.md](references/22-material-motion.md)，Microsoft 动效见 [25-microsoft-motion.md](references/25-microsoft-motion.md)，Apple 动效见 [07-motion.md](references/07-motion.md)、[09-motion-templates.md](references/09-motion-templates.md) 和 [16-liquid-glass-api-motion-color.md](references/16-liquid-glass-api-motion-color.md)。

### 图标系统分层

- 界面图标共享业务语义，不共享平台字体或 glyph：Apple 用 SF Symbols，Android/Material 用 Material Symbols，Windows 用 Segoe Fluent Icons/WinUI。
- App Icon 共享品牌识别，不共享最终外框和平台效果；分别遵循 Icon Composer、Windows manifest/ICO 和 Android Adaptive Icon/Play 资产规则。
- SF Symbols、Material Symbols、Segoe Fluent Icons、App Icon、商店图标和应用内 Logo 是不同资产层，禁止相互替代。

### 平台专属能力

- Android 专属或强绑定：Dynamic Color、Predictive Back、系统栏/WindowInsets、`FoldingFeature`、Material Adaptive pane/navigation、Android 小组件与通知模型。
- Windows 专属或强绑定：Mica、Acrylic、Smoke、WinUI 标题栏、Windows 命令与窗口模型。
- Apple 专属或强绑定：Liquid Glass 系统呈现、SF Symbols、Dynamic Island、Live Activities、iPhone Duo 竖向系统栏/Reserved Region/Arrangement View/场景附件、CarPlay、visionOS 空间输入、Digital Crown。
- 跨平台实现必须提供中性 fallback，并明确它是语义对应，不声称等同系统原生效果。

## 无障碍底线

- 不把颜色、形状或动效作为唯一状态信号。
- 保留可见焦点、键盘完整路径、语义名称、足够触控目标和文本缩放能力。
- 支持深色、高对比度、减少动态、屏幕阅读器和不同输入方式。
- 平台无障碍要求从各自官方入口核对：[Material accessibility](https://m3.material.io/foundations/overview/principles)、[Windows accessibility](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview)、[Apple accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)。

## 参考目录

### 平台路由

| 文件 | 内容 |
|---|---|
| [18-platform-routing.md](references/18-platform-routing.md) | Android、Windows、Apple 与 Web 的选择决策树、冲突处理、跨平台翻译和验收路线 |
| [26-cross-platform-baseline.md](references/26-cross-platform-baseline.md) | iOS 26+ SwiftUI 与 Android OEM 的平台基线、分层和 Liquid Glass 边界 |
| [27-adaptive-platform-capabilities.md](references/27-adaptive-platform-capabilities.md) | WindowSizeClass、窗口/输入/系统能力、语义效果映射和 fallback |
| [28-semantic-components-testing.md](references/28-semantic-components-testing.md) | 语义组件映射、Android OEM 测试矩阵、行为一致性与视觉容差 |
| [31-cross-platform-interface-icons.md](references/31-cross-platform-interface-icons.md) | SF Symbols、Material Symbols、Segoe Fluent Icons 的语义、原生 API、RTL、无障碍和工具链 |
| [32-cross-platform-app-icons.md](references/32-cross-platform-app-icons.md) | Apple、Windows、Android App Icon 的设计规范、派生方式、工具、打包槽位和最终表面验收 |

### Material & Google Design

| 文件 | 内容 |
|---|---|
| [19-google-android-map.md](references/19-google-android-map.md) | Android Mobile Design 与 Material 3 官方深度链接地图、开发入口、任务路由 |
| [20-material-foundations-styles.md](references/20-material-foundations-styles.md) | Material 3 无障碍、内容、Token、状态、布局、色彩、字体、elevation、shape、spacing、icon |
| [21-material-components-map.md](references/21-material-components-map.md) | Material 3 全组件 overview/guidelines/specs/accessibility 索引与组件选择规则 |
| [22-material-motion.md](references/22-material-motion.md) | Material 3 Expressive motion、空间/效果动效、过渡模式、Web fallback 和 reduced motion |
| [30-android-foldable-adaptation.md](references/30-android-foldable-adaptation.md) | Android 折叠屏、Adaptive Apps、WindowManager、pane/navigation、显示模式、测试与 Apple Duo 语义对齐 |

### Microsoft Design

| 文件 | 内容 |
|---|---|
| [23-microsoft-windows-map.md](references/23-microsoft-windows-map.md) | Windows Design、WinUI/Windows App SDK、Fluent 2 官方地图和任务路由 |
| [24-fluent-foundations-components.md](references/24-fluent-foundations-components.md) | Windows/Fluent 原则、Token、颜色、材质、布局、排版、无障碍和 Web 组件索引 |
| [25-microsoft-motion.md](references/25-microsoft-motion.md) | Windows 原生 Motion 与 Fluent Web Motion，时间/缓动、转场、编舞和无动画策略 |

### Apple Design

| 文件 | 内容 |
|---|---|
| [08-apple-docs-coverage.md](references/08-apple-docs-coverage.md) | Apple 官方文档覆盖状态和任务路由 |
| [10-apple-official-docs-map.md](references/10-apple-official-docs-map.md) | Apple Design/HIG 官方 URL 分类地图 |
| [11-hig-foundations-patterns.md](references/11-hig-foundations-patterns.md) | HIG Foundations 与 Patterns |
| [12-hig-components-inputs.md](references/12-hig-components-inputs.md) | HIG Components 与 Inputs |
| [13-platform-resources-technologies.md](references/13-platform-resources-technologies.md) | Apple 平台差异、资源、字体、SF Symbols 和技术品牌 |
| [29-iphone-duo-adaptation.md](references/29-iphone-duo-adaptation.md) | iPhone Duo 双显示、折叠姿态、Reserved Region、Arrangement View、竖向系统栏、场景、相机与测试 |

### Apple Liquid Glass 专项

| 文件 | 内容 |
|---|---|
| [14-liquid-glass-adoption.md](references/14-liquid-glass-adoption.md) | HIG Materials、Adopting Liquid Glass、Landmarks 示例与跨平台边界 |
| [15-liquid-glass-controls.md](references/15-liquid-glass-controls.md) | 原生控件、regular/clear、颜色、状态与 fallback |
| [16-liquid-glass-api-motion-color.md](references/16-liquid-glass-api-motion-color.md) | SwiftUI/UIKit/AppKit API、系统转场、颜色与深色模式 |
| [17-liquid-glass-deep-link-map.md](references/17-liquid-glass-deep-link-map.md) | Liquid Glass 官方深度链接地图 |

### Apple.com 与通用实现参考

| 文件 | 内容 |
|---|---|
| [00-philosophy.md](references/00-philosophy.md) | Apple/HIG 设计哲学和设计签名 |
| [01-tokens.md](references/01-tokens.md) | Apple.com 色彩、排版、间距、断点、圆角与材质 Token |
| [02-components.md](references/02-components.md) | Apple 风格 Web 组件模式 |
| [03-patterns.md](references/03-patterns.md) | Apple 风格页面布局模式 |
| [04-accessibility.md](references/04-accessibility.md) | Web 对比度、焦点、ARIA 和减少动态 |
| [05-tailwind-config.md](references/05-tailwind-config.md) | Apple 风格 Tailwind/CSS 实现 |
| [06-fonts.md](references/06-fonts.md) | PingFang SC 跨平台字体与 fallback |
| [07-motion.md](references/07-motion.md) | Apple 风格独立 Motion Token |
| [09-motion-templates.md](references/09-motion-templates.md) | Apple 风格前端动画模板 |
