# Microsoft / Windows Official Map

Windows 桌面应用默认使用 Windows Design + WinUI/Windows App SDK。Fluent 2 补充跨平台 Design System 和 Web 实现，但不能替代 Windows 原生窗口、命令、键盘和无障碍行为。

## 目录

- [根入口](#根入口)
- [设计原则与总览](#设计原则与总览)
- [Windows Design 地图](#windows-design-地图)
- [Windows 开发路线](#windows-开发路线)
- [Fluent 2 地图](#fluent-2-地图)
- [平台专属边界](#平台专属边界)
- [任务路由](#任务路由)

## 根入口

| 范围 | 官方入口 | 用途 |
|---|---|---|
| Windows 设计 | [Windows Design](https://learn.microsoft.com/en-us/windows/apps/design/) | Windows 原则、布局、签名体验、无障碍、导航、窗口和资源 |
| Windows 开发 | [Windows development](https://developer.microsoft.com/zh-cn/windows/develop) | WinUI、Windows App SDK、工具与示例入口 |
| Windows UI 开发 | [Develop Windows apps](https://learn.microsoft.com/windows/apps/develop/) | WinUI 控件、窗口、输入、主题和 UI API |
| WinUI 3 | [WinUI 3](https://learn.microsoft.com/windows/apps/winui/winui3/) | Windows App SDK 的现代原生 UI 框架 |
| Fluent 2 | [Fluent 2](https://fluent2.microsoft.design/) | Microsoft 跨平台视觉、Token、内容和 Web 组件 |
| Fluent Web | [Fluent 2 Web React](https://fluent2.microsoft.design/components/web/react) | React v9 与 Web Components 组件入口 |

## 设计原则与总览

[Windows 11 design principles](https://learn.microsoft.com/en-us/windows/apps/design/design-principles) 用五组特征描述平台体验：

- **Effortless**：高频任务直达，减少无意义步骤。
- **Calm**：界面不过度争夺注意力，层级与动效支持任务。
- **Personal**：响应主题、强调色、输入和用户偏好。
- **Familiar**：沿用 Windows 用户已知的窗口、导航、命令和快捷键。
- **Complete + coherent**：组件、状态、图标、文案和行为形成一致系统。

[Guidelines overview](https://learn.microsoft.com/en-us/windows/apps/design/guidelines-overview) 将规范按 Color、Commanding、Elevation、Geometry、Haptics、Iconography、Layout、Materials、Motion、Navigation、Typography、Usability、Widgets、Writing 分类。调用时先确定问题类别，不用视觉截图替代行为文档。

## Windows Design 地图

### App basics

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| App silhouette | [App silhouette](https://learn.microsoft.com/en-us/windows/apps/design/basics/app-silhouette) | 标题栏、导航、命令与内容的整体骨架 |
| Navigation basics | [Navigation basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics) | flat/hierarchical 架构、历史、breadcrumb、NavigationView |
| Commanding basics | [Commanding basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/commanding-basics) | 直接操控、主命令、菜单、撤销和确认 |
| Content basics | [Content basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/content-basics) | 数据展示、空状态、错误和内容组织 |
| Title bar design | [Title bar design](https://learn.microsoft.com/en-us/windows/apps/design/basics/titlebar-design) | 系统标题栏、拖动区域、caption buttons 和定制边界 |

### Signature experiences

| 领域 | 官方链接 | 关键内容 |
|---|---|---|
| Color | [Color](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/color) | 中性基础、系统主题、强调色、light/dark/high contrast |
| Geometry | [Geometry](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/geometry) | Windows 11 圆角层级与贴边规则 |
| Layering | [Layering](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/layering) | elevation、shadow、stroke 和基础/内容层 |
| Materials | [Materials](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/materials) | Mica、Acrylic、Smoke 和 Solid 的语义 |
| Motion | [Motion](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/motion) | Windows motion 原则、curve、duration 和控件转场 |
| Typography | [Typography](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography) | Segoe UI Variable、type ramp、字重与 fallback |

### Layout and responsiveness

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Layout overview | [Layout](https://learn.microsoft.com/en-us/windows/apps/design/layout/) | Windows 窗口布局总入口 |
| Responsive design | [Responsive design](https://learn.microsoft.com/en-us/windows/apps/design/layout/responsive-design) | reposition、resize、reflow、show/hide、re-architect |
| Screen sizes/breakpoints | [Screen sizes and breakpoints](https://learn.microsoft.com/en-us/windows/apps/design/layout/screen-sizes-and-breakpoints-for-responsive-design) | 有效像素和自适应触发条件 |
| Attached layouts | [Attached layouts](https://learn.microsoft.com/en-us/windows/apps/design/layout/attached-layouts) | RelativePanel 等相对布局关系 |
| Custom panels | [Custom panels](https://learn.microsoft.com/en-us/windows/apps/design/layout/custom-panels-overview) | 标准布局不足时的测量/排列边界 |
| Grid tutorial | [Grid tutorial](https://learn.microsoft.com/en-us/windows/apps/design/layout/grid-tutorial) | Grid 行列、star/auto/fixed 组合 |

### Accessibility and usability

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Accessibility overview | [Accessibility overview](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview) | UI Automation、键盘、屏幕阅读器、高对比度 |
| Checklist | [Accessibility checklist](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-checklist) | 发布前系统验收 |
| Basic information | [Basic accessibility information](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/basic-accessibility-information) | name/role/state、tab order、focus |
| Keyboard accessibility | [Keyboard accessibility](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/keyboard-accessibility) | 快捷键、焦点、键盘完整路径 |
| High contrast | [High contrast themes](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/high-contrast-themes) | 系统色、高对比度和图片/边界处理 |
| Accessible text | [Accessible text requirements](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessible-text-requirements) | 缩放、对比、可读与自动化名称 |
| Testing | [Accessibility testing](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-testing) | Accessibility Insights、Narrator 和手工测试 |
| Custom controls | [Custom automation peers](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/custom-automation-peers) | 自定义控件暴露 UI Automation |
| Usability | [Usability](https://learn.microsoft.com/en-us/windows/apps/design/usability/) | 输入、可发现性、效率和容错 |

### Iconography, writing, help, settings

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Iconography | [Icons in Windows apps](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/icons) | Windows 图标选择、IconElement/IconSource 和使用总览 |
| Segoe Fluent Icons | [Segoe Fluent Icons font](https://learn.microsoft.com/en-us/windows/apps/design/iconography/segoe-fluent-icons-font) | 原生 Windows glyph、推荐字号、mirroring 和 PUA 边界；跨平台映射见 `31-cross-platform-interface-icons.md` |
| App icons | [App icons](https://learn.microsoft.com/en-us/windows/apps/design/iconography/app-icons) | 包、Store 和系统呈现资产；设计、构建与最终槽位见 `32-cross-platform-app-icons.md` |
| Writing style | [Writing style](https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style) | Windows UI 文案、语气和大小写 |
| App help | [Guidelines for app help](https://learn.microsoft.com/en-us/windows/apps/design/in-app-help/guidelines-for-app-help) | 可发现帮助、内联说明和外部支持 |
| Instructional UI | [Instructional UI](https://learn.microsoft.com/en-us/windows/apps/design/in-app-help/instructional-ui) | 首次提示、teaching tip 和引导边界 |
| App settings | [Guidelines for app settings](https://learn.microsoft.com/en-us/windows/apps/design/app-settings/guidelines-for-app-settings) | 设置分类、保存和入口 |

### Globalization and widgets

| 页面 | 官方链接 | 调用时机 |
|---|---|---|
| Globalization portal | [Globalization](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/globalizing-portal) | 本地化、区域格式、字体与文本方向 |
| RTL/layout/fonts | [Adjust layout, fonts, and RTL](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/adjust-layout-and-fonts--and-support-rtl) | 镜像、文本扩展与国际字体 |
| Global-ready formats | [Global-ready formats](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/use-global-ready-formats) | 日期、时间、数字和区域格式 |
| Widgets overview | [Widgets](https://learn.microsoft.com/en-us/windows/apps/design/widgets/) | Windows Widgets 总体结构 |
| Widget fundamentals | [Widget design fundamentals](https://learn.microsoft.com/en-us/windows/apps/design/widgets/widgets-design-fundamentals) | 内容、布局和更新模型 |
| Widget interaction | [Widget interaction design](https://learn.microsoft.com/en-us/windows/apps/design/widgets/widgets-interaction-design) | 点击、deep link、滚动与限制 |
| Widget states | [Widget states and UI](https://learn.microsoft.com/en-us/windows/apps/design/widgets/widgets-states-and-ui) | loading、error、empty 和 signed-out |

### Resources

[Windows design resources](https://learn.microsoft.com/en-us/windows/apps/design/downloads/) 提供 Windows UI Kit、字体、WinUI Gallery 和 Microsoft Store 资产。资源用于对齐官方组件和资产，不替代当前文档与实际 WinUI 控件测试。

## Windows 开发路线

| 内容 | 官方链接 | 说明 |
|---|---|---|
| WinUI 3 | [WinUI 3](https://learn.microsoft.com/windows/apps/winui/winui3/) | Windows App SDK 的现代 C#/C++ 原生 UI |
| Windows App SDK | [Windows App SDK](https://learn.microsoft.com/windows/apps/windows-app-sdk/) | 窗口、App lifecycle、通知、部署等现代 API |
| UI controls | [Controls for Windows apps](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/) | WinUI 控件角色、示例和 API 路由 |
| First app | [Create your first WinUI 3 app](https://learn.microsoft.com/windows/apps/winui/winui3/create-your-first-winui3-app) | 项目结构与基础应用 |
| Windows SDK | [Windows SDK](https://learn.microsoft.com/windows/apps/windows-sdk/) | 平台 SDK 与版本要求 |
| Desktop docs | [Desktop application development](https://learn.microsoft.com/windows/apps/desktop/) | 桌面技术和迁移入口 |
| WinUI source | [microsoft-ui-xaml](https://github.com/microsoft/microsoft-ui-xaml) | 官方开源实现和 issue；行为规范仍以文档/API 为准 |
| WinUI Gallery | [WinUI Gallery](https://apps.microsoft.com/detail/9p3jfpwwdzrc) | 在 Windows 上验证实际控件外观和交互 |
| winapp CLI | [winapp CLI](https://learn.microsoft.com/windows/apps/dev-tools/winapp-cli/) | Windows 应用开发命令行工具 |
| AI-assisted development | [Windows development skills](https://learn.microsoft.com/windows/apps/develop/ai-assisted/) | 官方 AI/agent 辅助开发入口 |

Windows 桌面新项目通常优先 WinUI 3；技术选择仍需结合部署、现有 WPF/Win32/Windows Forms 代码和 API 需求，入口见 [Develop Windows desktop apps](https://learn.microsoft.com/windows/apps/desktop/)。

## Fluent 2 地图

### Foundations and styles

| 领域 | 官方链接 | 用途 |
|---|---|---|
| Design principles | [Fluent principles](https://fluent2.microsoft.design/design-principles/) | Natural on every platform、focus、inclusion、Microsoft identity |
| Design tokens | [Design tokens](https://fluent2.microsoft.design/design-tokens/) | global/raw 与 alias/semantic Token，light/dark/high contrast/brand |
| Color | [Color](https://fluent2.microsoft.design/color/) | neutral/shared/brand 与 interaction states |
| Material | [Material](https://fluent2.microsoft.design/material/) | Solid、Acrylic、Mica、Smoke 的 Fluent 语义 |
| Elevation | [Elevation](https://fluent2.microsoft.design/elevation/) | depth、shadow 和 layer hierarchy |
| Layout | [Layout](https://fluent2.microsoft.design/layout/) | grid、spacing、responsive 与 density |
| Typography | [Typography](https://fluent2.microsoft.design/typography/) | type ramp、font、line height 和 hierarchy |
| Shape | [Shape](https://fluent2.microsoft.design/shapes/) | corner radius 与容器层级 |
| Iconography | [Iconography](https://fluent2.microsoft.design/iconography/) | Fluent icons 和跨平台适配 |
| Motion | [Motion](https://fluent2.microsoft.design/motion/) | Fluent Web 动效原则与 transition；见 [25-microsoft-motion.md](25-microsoft-motion.md) |
| Accessibility | [Accessibility](https://fluent2.microsoft.design/accessibility/) | inclusive foundations、输入和高对比度 |
| Content design | [Content design](https://fluent2.microsoft.design/content-design/) | 语气、术语和产品文案 |

### Design and develop

| 路线 | 官方链接 | 用途 |
|---|---|---|
| Start designing | [Design](https://fluent2.microsoft.design/get-started/design) | Figma 资源、主题和设计流程 |
| Start developing | [Develop](https://fluent2.microsoft.design/get-started/develop) | React/Web Components/iOS/Android 库入口 |
| React v9 | [Fluent React](https://fluent2.microsoft.design/components/web/react) | `@fluentui/react-components` 组件与 Provider |
| Web Components | [Fluent Web Components](https://learn.microsoft.com/en-us/fluent-ui/web-components/) | `@fluentui/web-components` 与 CSS custom properties |

完整 Fluent Web 组件索引见 [24-fluent-foundations-components.md](24-fluent-foundations-components.md)。

## 平台专属边界

- **Windows-first**：Mica、系统 Acrylic、Smoke、caption buttons、标题栏、NavigationView、Windows high contrast 和 UI Automation。使用 [Windows Design](https://learn.microsoft.com/en-us/windows/apps/design/) 与 WinUI，而不是 CSS 模拟。
- **Fluent for Web**：可在 Microsoft 风格企业 Web 使用 Fluent React/Web Components，但其实现不自动等同 WinUI；入口见 [Fluent React](https://fluent2.microsoft.design/components/web/react)。
- **Fluent iOS/Android**：官方库可用于 Microsoft 产品一致性，但本 skill 默认仍让 iOS 使用 Apple、Android 使用 Google/Material；除非项目明确是 Microsoft 生态产品。开发入口见 [Fluent develop](https://fluent2.microsoft.design/get-started/develop)。
- **Cross-platform**：focus、语义 Token、清晰命令、无障碍和内容原则可迁移；窗口、材料、键盘模型和组件解剖必须适配。

## 任务路由

| 任务 | 先读 | 再读 |
|---|---|---|
| Windows 应用整体骨架 | [App silhouette](https://learn.microsoft.com/en-us/windows/apps/design/basics/app-silhouette) | [Navigation basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics) |
| 生产力工具命令 | [Commanding basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/commanding-basics) | [WinUI controls](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/) |
| 窗口自适应 | [Responsive design](https://learn.microsoft.com/en-us/windows/apps/design/layout/responsive-design) | [Screen sizes/breakpoints](https://learn.microsoft.com/en-us/windows/apps/design/layout/screen-sizes-and-breakpoints-for-responsive-design) |
| 标题栏定制 | [Title bar design](https://learn.microsoft.com/en-us/windows/apps/design/basics/titlebar-design) | [WinUI title bar](https://learn.microsoft.com/en-us/windows/apps/develop/title-bar) |
| Mica/Acrylic | [Windows materials](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/materials) | [Fluent material](https://fluent2.microsoft.design/material/) |
| Web 企业工作台 | [Fluent layout](https://fluent2.microsoft.design/layout/) | [Fluent React components](https://fluent2.microsoft.design/components/web/react) |
| 界面图标 | [31-cross-platform-interface-icons.md](31-cross-platform-interface-icons.md) | [Icons in Windows apps](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/icons)、[WinUI Gallery](https://github.com/microsoft/WinUI-Gallery) |
| App Icon / Shell 资产 | [32-cross-platform-app-icons.md](32-cross-platform-app-icons.md) | [App icon design](https://learn.microsoft.com/en-us/windows/apps/design/iconography/app-icon-design)、[construction](https://learn.microsoft.com/en-us/windows/apps/design/iconography/app-icon-construction) |
| 无障碍验收 | [Accessibility overview](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview) | [Checklist](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-checklist) |
| 动效 | [Windows motion](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/motion) | [Fluent motion](https://fluent2.microsoft.design/motion/) 与 [25-microsoft-motion.md](25-microsoft-motion.md) |
