# Google / Android Official Map

Android 手机、平板、折叠屏和 Android 大屏任务的官方资料地图。Android Mobile Design 负责平台行为和移动模式，Material 3 负责 Design System、组件和实现。两者应一起使用。

资料快照：2026-09-15。Android 折叠屏开发主线已归入 Adaptive Apps；详细抽取和 Apple Duo 语义对齐见 [android-foldable-adaptation.md](android-foldable-adaptation.md)。

## 目录

- [根入口与开发路线](#根入口与开发路线)
- [Android Mobile Design 地图](#android-mobile-design-地图)
- [Adaptive Apps 与折叠屏地图](#adaptive-apps-与折叠屏地图)
- [Material 3 Foundations 地图](#material-3-foundations-地图)
- [Material 3 Styles 地图](#material-3-styles-地图)
- [组件与开发入口](#组件与开发入口)
- [平台专属边界](#平台专属边界)
- [任务路由](#任务路由)

## 根入口与开发路线

| 范围 | 官方入口 | 用途 |
|---|---|---|
| Android 移动设计 | [Design for mobile](https://developer.android.google.cn/design/ui/mobile) | Android 导航、系统栏、布局、模式、Home、无障碍 |
| Material 3 | [Material Design 3](https://m3.material.io/) | Foundations、Styles、Components、Material 3 Expressive |
| Material 开发 | [Develop](https://m3.material.io/develop) | Android、Flutter、Web 开发入口 |
| Jetpack Compose | [Material 3 in Compose](https://m3.material.io/develop/android/jetpack-compose) | Android 新项目首选的 Compose Material 3 路线 |
| Android Views | [Material Components for Android](https://m3.material.io/develop/android/mdc-android) | 传统 View 系统与 Material Components |
| Adaptive Apps | [Adaptive Apps](https://developer.android.com/develop/adaptive-apps) | 手机、平板、折叠屏、ChromeOS、桌面窗口的统一自适应开发主线 |
| Material 3 Adaptive | [Compose Material 3 Adaptive](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps) | WindowSizeClass、adaptive navigation、list-detail/supporting pane 与 posture |
| Jetpack WindowManager | [WindowManager](https://developer.android.com/jetpack/androidx/releases/window) | Window metrics、FoldingFeature、显示模式与传统 View/Compose 底层能力 |
| Flutter | [Material for Flutter](https://m3.material.io/develop/flutter) | Flutter 的 Material 3 实现 |
| Web | [Material Web](https://m3.material.io/develop/web) | Web Components/Material Web 入口；先核对项目维护状态和现有框架 |
| 完整 URL 清单 | [Material 3 sitemap](https://m3.material.io/sitemap.xml) | 发现新增、改名和细分页面 |

## Android Mobile Design 地图

### Foundations

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Accessibility | [Accessibility](https://developer.android.google.cn/design/ui/mobile/guides/foundations/accessibility) | 触控目标、对比度、文字、TalkBack 与可达性 |
| System bars | [System bars](https://developer.android.google.cn/design/ui/mobile/guides/foundations/system-bars) | edge-to-edge、状态栏、导航栏、WindowInsets |
| Glossary | [Glossary](https://developer.android.google.cn/design/ui/mobile/guides/foundations/glossary) | 统一 Android 术语 |
| iOS 到 Android 翻译 | [10 Steps to Android](https://developer.android.google.cn/design/ui/mobile/guides/foundations/translate-designs) | 将 iOS/Web 产品转换为 Android 原生信息结构与控件 |

### Styles

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Color | [Android mobile color](https://developer.android.google.cn/design/ui/mobile/guides/styles/color) | 语义角色、HCT、动态颜色与静态 fallback |
| Themes | [Themes](https://developer.android.google.cn/design/ui/mobile/guides/styles/themes) | light/dark、品牌主题和系统个性化 |

### Layout & content

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Layout basics | [Layout basics](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/layout-basics) | 内容区域、窗口、基础响应式 |
| App anatomy | [App anatomy](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/app-anatomy) | 系统 UI、导航、内容和浮层关系 |
| Grids and units | [Grids and units](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/grids-and-units) | dp/sp、网格与测量 |
| Content structure | [Content structure](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/content-structure) | 信息层级与分组 |
| Layout/navigation patterns | [Layout and navigation patterns](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns) | 单页、列表详情、多窗格导航 |
| Common layouts | [Common layouts](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/common-layouts) | 常见页面骨架 |
| Adaptive layout | [Adapt layout](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/adapt-layout) | 手机、平板、折叠屏与窗口变化 |
| Postures/orientation | [Postures and orientation](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/postures-and-orientation) | 折叠姿态与旋转 |
| Immersive content | [Immersive content](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/immersive-content) | 全屏媒体和沉浸内容 |
| Edge-to-edge | [Edge-to-edge](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/edge-to-edge) | 内容延伸至系统栏并处理 inset |
| Images/graphics | [Images and graphics](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/images-graphics) | 图片比例、裁切和图形内容 |

### Patterns and Home

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Predictive back | [Predictive back](https://developer.android.google.cn/design/ui/mobile/guides/patterns/predictive-back) | 系统返回预览、Back/Up 语义和转场 |
| Settings | [Settings](https://developer.android.google.cn/design/ui/mobile/guides/patterns/settings) | 设置分类、层级与控件 |
| Help/feedback | [Help and feedback](https://developer.android.google.cn/design/ui/mobile/guides/patterns/help-content) | 帮助入口、反馈与支持内容 |
| Passkeys | [Passkeys](https://developer.android.google.cn/design/ui/mobile/guides/patterns/passkeys) | 登录与凭据体验 |
| Onboarding/auth | [Onboarding and authentication](https://developer.android.google.cn/design/ui/mobile/guides/patterns/onboarding) | 首次体验、登录、权限前置说明 |
| Notifications | [Notifications](https://developer.android.google.cn/design/ui/mobile/guides/home-screen/notifications) | 通知内容、优先级和操作 |
| Live updates | [Live updates](https://developer.android.google.cn/design/ui/mobile/guides/home-screen/live-updates) | 进行中、时间敏感的持续状态 |
| Picture-in-picture | [Picture-in-picture](https://developer.android.google.cn/design/ui/mobile/guides/home-screen/picture-in-picture) | 视频/通话离开页面后的持续任务 |

### Widgets

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Overview | [Widgets](https://developer.android.google.cn/design/ui/mobile/guides/widgets) | Android Home 小组件总览 |
| Layouts | [Widget layouts](https://developer.android.google.cn/design/ui/mobile/guides/widgets/layouts) | 信息结构和组件布局 |
| Sizing | [Widget sizing](https://developer.android.google.cn/design/ui/mobile/guides/widgets/sizing) | 响应式尺寸和网格 |
| Style | [Widget style](https://developer.android.google.cn/design/ui/mobile/guides/widgets/style) | 颜色、形状、排版 |
| Configuration | [Widget configuration](https://developer.android.google.cn/design/ui/mobile/guides/widgets/configuration) | 添加和编辑配置 |
| Discovery/promotion | [Widget discovery and promotion](https://developer.android.google.cn/design/ui/mobile/guides/widgets/discovery-promotion) | 发现、预览和应用内推广 |

## Adaptive Apps 与折叠屏地图

| 分类 | 官方页面 | 本 skill 用法 |
|---|---|---|
| 总览 | [Adaptive Apps](https://developer.android.com/develop/adaptive-apps) | 自适应能力、canonical patterns、form factors 总入口 |
| 入门 | [Get started](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps) | Compose Material 3 Adaptive、配置变化与连续性 |
| 窗口 | [Support different display sizes](https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes)、[Window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) | 按当前 App window 而非设备或物理屏幕设计 |
| 导航 | [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation) | NavigationSuiteScaffold 在 bar/rail 之间适配 |
| Canonical layouts | [Canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts) | feed、list-detail、supporting pane 的语义选择 |
| 折叠屏概念 | [Learn about foldables](https://developer.android.com/develop/adaptive-apps/guides/foldables/learn-about-foldables) | 折叠状态、posture、continuity、multitasking 与 drag/drop |
| 折叠特征 | [Make your app fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware) | FoldingFeature、tabletop/book、bounds、occlusion 与 separation |
| 特殊显示 | [Foldable display modes](https://developer.android.com/develop/adaptive-apps/guides/foldables/support-foldable-display-modes) | rear display、dual-screen 与 capability fallback |
| 多铰链 | [Trifolds and landscape foldables](https://developer.android.com/develop/adaptive-apps/guides/foldables/trifolds-and-landscape-foldables) | 不假设单一铰链、单一自然方向或 HALF_OPENED |
| 相机 | [Camera on multiple form factors](https://developer.android.com/develop/adaptive-apps/guides/camera-form-factors-support) | 预览比例、旋转、tabletop、rear/dual screen |
| 兼容边界 | [Orientation, aspect ratio, resizability](https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability) | Android 16 大屏行为与 fixed-orientation 风险 |
| 质量 | [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)、[Foldables tests](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables) | Tier 3/2/1 与官方测试矩阵 |

本节只负责官方入口；设计与实现规则集中在 [android-foldable-adaptation.md](android-foldable-adaptation.md)，避免与 Foundations/Styles 重复。

## Material 3 Foundations 地图

| 分类 | 官方页面 | 核心问题 |
|---|---|---|
| Accessibility principles | [Principles](https://m3.material.io/foundations/overview/principles) | 如何从尊重个体与共同设计出发，而不是只做最低合规 |
| Assistive technology | [Assistive technology](https://m3.material.io/foundations/overview/assistive-technology) | 屏幕阅读器、放大、语音和替代输入 |
| Accessible design | [Designing overview](https://m3.material.io/foundations/designing/overview) | 结构、流程、元素和色彩对比 |
| Accessible writing | [Writing overview](https://m3.material.io/foundations/writing/best-practices) | 文本缩放、截断和清晰表达 |
| Content design | [Content design overview](https://m3.material.io/foundations/content-design/overview) | UX 文案、替代文本、通知与全球化写作 |
| Customization | [Customization](https://m3.material.io/foundations/customization) | 品牌主题、动态颜色与静态方案 |
| Design tokens | [Design tokens overview](https://m3.material.io/foundations/design-tokens/overview)、[How to use tokens](https://m3.material.io/foundations/design-tokens/how-to-use-tokens) | reference/system/component 三层和上下文切换 |
| Gestures | [Gestures](https://m3.material.io/foundations/interaction/gestures) | 触控手势与替代操作 |
| Inputs/selection | [Inputs](https://m3.material.io/foundations/interaction/inputs)、[Selection](https://m3.material.io/foundations/interaction/selection) | 触控、键盘、指针和选择模型 |
| States | [States overview](https://m3.material.io/foundations/interaction/states/overview)、[Applying states](https://m3.material.io/foundations/interaction/states/applying-states)、[State layers](https://m3.material.io/foundations/interaction/states/state-layers) | disabled/hover/focus/pressed/dragged 的组合与视觉信号 |
| Adaptive design | [Adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design) | show/hide、levitate、reflow 与多输入 |
| Scaffold | [Scaffold overview](https://m3.material.io/foundations/layout/scaffold/overview) | bars、panes、rails 的页面骨架 |
| Grid/spacing/density | [Grids and spacing](https://m3.material.io/foundations/layout/grids-spacing/overview)、[Density](https://m3.material.io/foundations/layout/grids-spacing/density) | 网格、间距和密度 |
| Breakpoints | [Breakpoints overview](https://m3.material.io/foundations/layout/breakpoints/overview) | 按窗口类别而不是设备名设计 |
| Bidirectionality | [Bidirectionality and RTL](https://m3.material.io/foundations/layout/bidirectionality-rtl) | RTL 镜像、阅读顺序和图标方向 |
| Canonical layouts | [Canonical examples](https://m3.material.io/foundations/layout/canonical-examples/overview) | feed、list-detail、supporting pane |
| Usability | [Usability](https://m3.material.io/foundations/usability/overview) | 易用性与 M3 Expressive 的应用边界 |

Material 网站会调整部分路径；若上表中的深层路径变更，用 [Material 3 sitemap](https://m3.material.io/sitemap.xml) 和对应页面标题重新定位。

## Material 3 Styles 地图

| 样式领域 | 官方入口 | 细分 |
|---|---|---|
| Color | [Color system](https://m3.material.io/styles/color/system/overview) | [Roles](https://m3.material.io/styles/color/roles)、[Static](https://m3.material.io/styles/color/static/baseline)、[Dynamic](https://m3.material.io/styles/color/dynamic/choosing-a-source)、[Advanced](https://m3.material.io/styles/color/advanced/overview) |
| Elevation | [Elevation](https://m3.material.io/styles/elevation/overview) | [Applying elevation](https://m3.material.io/styles/elevation/applying-elevation)、[Tokens](https://m3.material.io/styles/elevation/tokens) |
| Interface icons | [Material Symbols](https://fonts.google.com/icons) | [Icons overview](https://m3.material.io/styles/icons/overview)、[Applying icons](https://m3.material.io/styles/icons/applying-icons)、[Designing icons](https://m3.material.io/styles/icons/designing-icons)；跨平台映射见 [../cross-platform/cross-platform-interface-icons.md](../cross-platform/cross-platform-interface-icons.md) |
| App icons | [Adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive) | [Image Asset Studio](https://developer.android.com/studio/write/create-app-icons)、[Google Play icon spec](https://developer.android.com/distribute/google-play/resources/icon-design-specifications)；跨平台生产见 [../cross-platform/cross-platform-app-icons.md](../cross-platform/cross-platform-app-icons.md) |
| Motion | [Motion](https://m3.material.io/styles/motion/overview/how-it-works) | [Specs](https://m3.material.io/styles/motion/overview/specs)、[Transitions](https://m3.material.io/styles/motion/transitions/transition-patterns)；详见 [material-motion.md](material-motion.md) |
| Shape | [Shape principles](https://m3.material.io/styles/shape/overview-principles) | [Corner radius](https://m3.material.io/styles/shape/corner-radius-scale)、[Shape morph](https://m3.material.io/styles/shape/shape-morph) |
| Spacing | [Spacing](https://m3.material.io/styles/spacing/overview) | [Applying spacing](https://m3.material.io/styles/spacing/applying-spacing)、[Tokens](https://m3.material.io/styles/spacing/tokens) |
| Typography | [Typography](https://m3.material.io/styles/typography/overview) | [Fonts](https://m3.material.io/styles/typography/fonts)、[Type scale](https://m3.material.io/styles/typography/type-scale-tokens)、[Editorial](https://m3.material.io/styles/typography/editorial-treatments) |

详细抽取见 [material-foundations-styles.md](material-foundations-styles.md)。

## 组件与开发入口

- 全组件目录见 [Material 3 Components](https://m3.material.io/components) 和本地 [material-components-map.md](material-components-map.md)。
- Android 新实现优先 [Jetpack Compose Material 3](https://m3.material.io/develop/android/jetpack-compose)；传统项目使用 [Material Components for Android](https://m3.material.io/develop/android/mdc-android)。
- 组件的 `overview` 用于角色，`guidelines` 用于行为，`specs` 用于尺寸/Token，`accessibility` 用于语义和输入验收；不要只读截图或 specs。

## 平台专属边界

- **Android-only / Android-adapted**：系统栏、WindowInsets、Predictive Back、`FoldingFeature`、rear/dual display mode、Android 通知、Home Widgets 和系统动态颜色来源。参考 [Android Mobile](https://developer.android.google.cn/design/ui/mobile) 与 [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)。
- **Material 可跨平台**：语义 Token、组件角色、状态、布局策略和动效原则可用于 Flutter/Web，但具体组件实现和导航行为仍服从运行平台。参考 [Material Develop](https://m3.material.io/develop)。
- **特殊设备**：Material 中的 [Watches](https://m3.material.io/foundations/watches/overview) 和 XR 内容仅用于对应设备，普通 Android 手机或 Web 不默认引用。

## 任务路由

| 任务 | 先读 | 再读 |
|---|---|---|
| 从 iOS/Figma 迁移 Android | [10 Steps to Android](https://developer.android.google.cn/design/ui/mobile/guides/foundations/translate-designs) | [Material components](https://m3.material.io/components) |
| 手机到平板/折叠屏 | [android-foldable-adaptation.md](android-foldable-adaptation.md) | [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)、[Material adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design) |
| 主题与品牌色 | [Android color](https://developer.android.google.cn/design/ui/mobile/guides/styles/color) | [Material color roles](https://m3.material.io/styles/color/roles) |
| 导航架构 | [Layout and navigation patterns](https://developer.android.google.cn/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns) | [Navigation bar](https://m3.material.io/components/navigation-bar/guidelines)、[rail](https://m3.material.io/components/navigation-rail/guidelines)、[drawer](https://m3.material.io/components/navigation-drawer/guidelines) |
| 返回与页面转场 | [Predictive back](https://developer.android.google.cn/design/ui/mobile/guides/patterns/predictive-back) | [Material motion](https://m3.material.io/styles/motion/overview/how-it-works) |
| 表单和选择 | [Inputs](https://m3.material.io/foundations/interaction/inputs) | [Text fields](https://m3.material.io/components/text-fields/guidelines)、[selection components](https://m3.material.io/components) |
| 界面图标与自定义 Symbol | [../cross-platform/cross-platform-interface-icons.md](../cross-platform/cross-platform-interface-icons.md) | [Material Symbols](https://fonts.google.com/icons)、[Icons in Compose](https://developer.android.com/develop/ui/compose/graphics/images/material) |
| Launcher / Play App Icon | [../cross-platform/cross-platform-app-icons.md](../cross-platform/cross-platform-app-icons.md) | [Adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive)、[Play icon spec](https://developer.android.com/distribute/google-play/resources/icon-design-specifications) |
| 无障碍验收 | [Android accessibility](https://developer.android.google.cn/design/ui/mobile/guides/foundations/accessibility) | [Material principles](https://m3.material.io/foundations/overview/principles) |
