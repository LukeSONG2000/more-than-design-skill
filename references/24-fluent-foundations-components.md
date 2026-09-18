# Microsoft Fluent Foundations & Components

本文件同时覆盖 Windows 原生签名体验和 Fluent 2 的跨平台基础。Windows 桌面应用优先 Windows Design + WinUI；Fluent React/Web Components 主要用于 Web。动效独立见 [25-microsoft-motion.md](25-microsoft-motion.md)。

## 目录

- [Fluent 原则](#fluent-原则)
- [Design Token 与主题](#design-token-与主题)
- [颜色](#颜色)
- [材质](#材质)
- [Geometry 与 Elevation](#geometry-与-elevation)
- [排版与图标](#排版与图标)
- [布局与命令](#布局与命令)
- [无障碍](#无障碍)
- [WinUI 控件入口](#winui-控件入口)
- [Fluent Web 组件索引](#fluent-web-组件索引)
- [跨平台边界](#跨平台边界)

## Fluent 原则

[Fluent 2 design principles](https://fluent2.microsoft.design/design-principles/) 的核心不是统一截图，而是在平台自然性、专注、包容和 Microsoft 身份之间建立一致性：

- **Natural on every platform**：大部分交互服从运行平台原生模式；共享品牌不应覆盖平台习惯。
- **Built for focus**：层级、命令、动效和内容帮助用户完成任务，不制造持续干扰。
- **One for all, all for one**：设计包容不同能力、语言、输入和环境。
- **Unmistakably Microsoft**：通过 Token、图标、内容和适量品牌表达建立家族感，而不是强制每个平台同形。

Windows 原生体验同时遵守 [Windows design principles](https://learn.microsoft.com/en-us/windows/apps/design/design-principles) 的 Effortless、Calm、Personal、Familiar、Complete + coherent。

## Design Token 与主题

[Fluent design tokens](https://fluent2.microsoft.design/design-tokens/) 分为：

| 层级 | 作用 | 示例语义 |
|---|---|---|
| Global / raw | 保存原始色值、尺寸、字体和其他基础值 | palette、font family、spacing scale |
| Alias / semantic | 描述界面角色和状态 | foreground、background、stroke、brand、status |
| Component mapping | 将语义角色映射到组件槽位 | button foreground/background、field border |

使用规则：

- 业务组件引用 alias/semantic 角色，不直接引用 raw 色值。
- 主题至少覆盖 light、dark、high contrast；品牌主题不能破坏系统主题和交互状态。
- 同一角色在 Web 与 Windows 可映射不同实现；一致的是语义，不是像素。
- Fluent React 通过 [FluentProvider](https://fluent2.microsoft.design/components/web/react/core/fluentprovider/usage) 提供主题上下文；Web Components 通过 [design tokens](https://learn.microsoft.com/en-us/fluent-ui/web-components/design-system/design-tokens) 和 CSS custom properties 配置。

## 颜色

[Fluent color](https://fluent2.microsoft.design/color/) 以 neutral、shared 和 brand 三组色彩建立界面：

- neutral 构成大面积背景、文字、边界和层级，是生产力界面的主体。
- brand 用于关键动作、选择、焦点和品牌识别，应克制，不能让所有控件同等强调。
- shared/status 色表达 error、warning、success、information 等语义，不按页面装饰选色。
- hover、pressed、selected、disabled 和 focus 是交互状态，不应只对基础颜色做任意明暗变化。

Windows 原生应响应用户的 light/dark、强调色与高对比度偏好，参考 [Windows color](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/color)。高对比度模式优先使用系统资源，不保留会降低识别度的品牌背景；参考 [High contrast themes](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/high-contrast-themes)。

## 材质

[Windows materials](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/materials) 与 [Fluent material](https://fluent2.microsoft.design/material/) 将材质用于层级和上下文，不是普通背景装饰。

| 材质 | 官方语义 | 正确场景 | 边界 |
|---|---|---|---|
| Solid | 不透明基础表面 | 内容密集、性能/无障碍 fallback、普通容器 | 不需要透明时默认使用 |
| Mica | 与桌面背景和窗口状态建立关系的 app/window base | Windows 顶层窗口和标题栏附近的长期背景 | Windows-only；不是控件内部 blur |
| Acrylic | 带纹理的半透明材质，保持后方上下文 | 临时、light-dismiss 的 flyout、menu、popover 等 | Windows-only 系统材质；大面积长期背景慎用 |
| Smoke | 模态层后方的暗化遮罩 | 对话框等需要阻断背景交互的场景 | 通常为半透明黑色遮罩，不是玻璃卡片 |

原生 WinUI 优先系统 API，让平台处理主题、窗口激活、性能和 fallback。Web 可用颜色、透明度和有限 blur 表达“层级近似”，但必须称为 Web fallback，不能声称等同 Mica/Acrylic。

## Geometry 与 Elevation

### Windows geometry

[Windows geometry](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/geometry) 的常用层级：

| 场景 | Corner radius |
|---|---:|
| 顶层容器、flyout、dialog | `8px` |
| 页面内控件、bar | `4px` |
| 接触屏幕/窗口边缘，或 maximized/snapped 的窗口边缘 | `0px` |

这些值用于 Windows 原生层级，不是要求 Web/Android/Apple 全部使用 8/4/0。圆角应随相邻关系和窗口状态变化，不能让贴边内容露出无意义空隙。

### Layering and elevation

[Windows layering](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/layering) 通过 shadow 与 contour 表达有目的的层级，并把应用理解为 base layer（菜单、命令、导航）和 content layer。

| 元素 | Windows elevation reference |
|---|---:|
| Window / dialog | `128` |
| Flyout | `32` |
| Tooltip | `16` |
| Card | `8` |
| Control | `2` |
| Layer | `1` |

数值表示平台层级参考，不应直接转成跨平台 CSS shadow。Web 使用 [Fluent elevation](https://fluent2.microsoft.design/elevation/) 的语义和 Token；优先少量稳定层级，避免每张卡片都悬浮。

## 排版与图标

### Typography

[Windows typography](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography) 默认使用 Segoe UI Variable，包含 weight 与 optical size 轴。常规 UI 以 Regular/Semibold 为主，默认左对齐、sentence case。

| Role scale reference | Font size / line height |
|---|---|
| Caption | `12 / 16` effective px |
| Body | `14 / 20` effective px |
| Subtitle | `18 / 24` effective px |
| Title | `20 / 28` effective px |
| Title large | `28 / 36` effective px |
| Display | `40 / 52` effective px |
| Display large | `68 / 92` effective px |

- 小号文字参考底线为 `14px Semibold` 或 `12px Regular`，仍需结合高 DPI、语言和用户缩放测试。
- 非 Windows 平台不能假设有 Segoe UI Variable；[Selawik](https://github.com/microsoft/Selawik) 是 Microsoft 开源的 metric-compatible fallback 选项，Web 仍应提供系统字体链。
- Fluent Web 的角色和 Token 见 [Fluent typography](https://fluent2.microsoft.design/typography/)。

### Iconography

- Windows 原生使用 [Segoe Fluent Icons](https://learn.microsoft.com/en-us/windows/apps/design/iconography/segoe-fluent-icons-font) 或 WinUI `SymbolIcon`、`FontIcon`、`IconSource`，保持推荐字号、光学尺寸和平台语义。
- Web 使用 [Fluent iconography](https://fluent2.microsoft.design/iconography/) 与官方 Fluent icons 包。
- 图标按钮提供 accessible name；不熟悉的图标配 tooltip 或文本。
- 不把 Segoe Fluent Icons 复制到 Android/iOS 覆盖 Material Symbols/SF Symbols，除非 Microsoft 品牌产品明确要求。
- Segoe PUA 代码点不是跨平台协议；完整类型选择、mirroring、AnimatedIcon 和语义映射见 [31-cross-platform-interface-icons.md](31-cross-platform-interface-icons.md)。Windows Shell/App Icon 另见 [32-cross-platform-app-icons.md](32-cross-platform-app-icons.md)。

## 布局与命令

### Responsive layout

[Windows responsive design](https://learn.microsoft.com/en-us/windows/apps/design/layout/responsive-design) 提供六类策略：

| 策略 | 含义 |
|---|---|
| Reposition | 在窗口变化时移动区域 |
| Resize | 调整控件/内容尺寸并设置合理 min/max |
| Reflow | 改变行列或阅读流 |
| Show/hide | 按优先级显示、折叠或移入菜单 |
| Re-architect | 从单窗格切换为多窗格或不同导航架构 |
| Adaptive replacement | 用更适合当前窗口/输入的组件替换原组件 |

不要按设备型号设计固定画布。窗口可被 resize、snap、缩放并跨显示器移动；测试有效像素和文字缩放，参考 [Screen sizes and breakpoints](https://learn.microsoft.com/en-us/windows/apps/design/layout/screen-sizes-and-breakpoints-for-responsive-design)。

### Navigation and commanding

[Navigation basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics) 建议保持 consistent、simple、clear，避免不必要深层级；层级超过两级时考虑 breadcrumb，少量页面可 flat，大量目的地采用 hierarchy。

[Commanding basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/commanding-basics) 的优先顺序：

1. 直接操控内容。
2. 将高频核心命令放在 canvas 或 command bar。
3. 次要命令进入 overflow、menu 或 context menu。
4. 可逆操作优先提供 undo；只有重大且不可逆后果才要求确认。

桌面工作流必须完整支持 keyboard、pointer、focus 和 shortcut，不以触控尺寸为唯一设计依据。

## 无障碍

[Windows accessibility overview](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview) 要求应用支持 keyboard、screen reader、customization 和 high contrast，并通过 UI Automation 暴露控件语义。

- 使用标准 WinUI 控件可自动获得大部分 AutomationPeer 和输入行为；自定义控件按 [Custom automation peers](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/custom-automation-peers) 实现。
- 每个可操作元素有 accessible name、role、state；装饰元素不制造噪音。
- Tab order 与视觉/任务顺序一致，焦点始终可见；参考 [Keyboard accessibility](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/keyboard-accessibility)。
- 不硬编码会在 high contrast 消失的颜色、边界或图标；参考 [High contrast themes](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/high-contrast-themes)。
- 自动化扫描加 Narrator、键盘、高对比度、缩放和真实任务手测；参考 [Accessibility testing](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-testing)。
- Fluent Web 同时遵守浏览器语义和 [Fluent accessibility](https://fluent2.microsoft.design/accessibility/)。

## WinUI 控件入口

[Controls for Windows apps](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/) 是 WinUI 原生控件总入口。常用路由：

| 任务 | 官方控件文档 |
|---|---|
| 顶层/层级导航 | [NavigationView](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/navigationview)、[BreadcrumbBar](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/breadcrumbbar) |
| 同一窗口多文档/页签 | [TabView](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/tab-view) |
| 命令 | [Commanding](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/commanding)、[Menus](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/menus) |
| 对话/提示 | [Dialogs and flyouts](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/dialogs-and-flyouts)、[TeachingTip](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/dialogs-and-flyouts/teaching-tip) |
| 集合与数据 | [Lists](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/lists)、[ItemsView](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/itemsview) |
| 输入 | [Text controls](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/text-controls)、[Checkbox](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/checkbox)、[Radio button](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/radio-button)、[Toggle switch](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/toggles) |
| 日期时间 | [Date and time controls](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/date-and-time) |
| 进度与状态 | [Progress controls](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/progress-controls) |

实际控件名称、平台版本和 API 以 [WinUI Gallery](https://apps.microsoft.com/detail/9p3jfpwwdzrc) 与当前文档为准。

## Fluent Web 组件索引

Fluent React v9 入口见 [Web React](https://fluent2.microsoft.design/components/web/react)，常用安装包为 `@fluentui/react-components`。下表链接均指官方 usage 页面：

| 组件 | 官方页面 | 组件 | 官方页面 |
|---|---|---|---|
| Accordion | [Usage](https://fluent2.microsoft.design/components/web/react/core/accordion/usage) | Avatar | [Usage](https://fluent2.microsoft.design/components/web/react/core/avatar/usage) |
| AvatarGroup | [Usage](https://fluent2.microsoft.design/components/web/react/core/avatargroup/usage) | Badge | [Usage](https://fluent2.microsoft.design/components/web/react/core/badge/usage) |
| Breadcrumb | [Usage](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage) | Button | [Usage](https://fluent2.microsoft.design/components/web/react/core/button/usage) |
| Card | [Usage](https://fluent2.microsoft.design/components/web/react/core/card/usage) | Carousel | [Usage](https://fluent2.microsoft.design/components/web/react/core/carousel/usage) |
| Checkbox | [Usage](https://fluent2.microsoft.design/components/web/react/core/checkbox/usage) | Combobox | [Usage](https://fluent2.microsoft.design/components/web/react/core/combobox/usage) |
| Dialog | [Usage](https://fluent2.microsoft.design/components/web/react/core/dialog/usage) | Divider | [Usage](https://fluent2.microsoft.design/components/web/react/core/divider/usage) |
| Drawer | [Usage](https://fluent2.microsoft.design/components/web/react/core/drawer/usage) | Dropdown | [Usage](https://fluent2.microsoft.design/components/web/react/core/dropdown/usage) |
| Field | [Usage](https://fluent2.microsoft.design/components/web/react/core/field/usage) | FluentProvider | [Usage](https://fluent2.microsoft.design/components/web/react/core/fluentprovider/usage) |
| Icon | [Usage](https://fluent2.microsoft.design/components/web/react/core/icon/usage) | Image | [Usage](https://fluent2.microsoft.design/components/web/react/core/image/usage) |
| InfoLabel | [Usage](https://fluent2.microsoft.design/components/web/react/core/infolabel/usage) | Input | [Usage](https://fluent2.microsoft.design/components/web/react/core/input/usage) |
| Label | [Usage](https://fluent2.microsoft.design/components/web/react/core/label/usage) | Link | [Usage](https://fluent2.microsoft.design/components/web/react/core/link/usage) |
| List | [Usage](https://fluent2.microsoft.design/components/web/react/core/list/usage) | Menu | [Usage](https://fluent2.microsoft.design/components/web/react/core/menu/usage) |
| MessageBar | [Usage](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage) | Nav | [Usage](https://fluent2.microsoft.design/components/web/react/core/nav/usage) |
| Persona | [Usage](https://fluent2.microsoft.design/components/web/react/core/persona/usage) | Popover | [Usage](https://fluent2.microsoft.design/components/web/react/core/popover/usage) |
| ProgressBar | [Usage](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage) | RadioGroup | [Usage](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage) |
| Rating | [Usage](https://fluent2.microsoft.design/components/web/react/core/rating/usage) | SearchBox | [Usage](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage) |
| Select | [Usage](https://fluent2.microsoft.design/components/web/react/core/select/usage) | Skeleton | [Usage](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage) |
| Slider | [Usage](https://fluent2.microsoft.design/components/web/react/core/slider/usage) | SpinButton | [Usage](https://fluent2.microsoft.design/components/web/react/core/spin/usage) |
| Spinner | [Usage](https://fluent2.microsoft.design/components/web/react/core/spinner/usage) | Switch | [Usage](https://fluent2.microsoft.design/components/web/react/core/switch/usage) |
| TabList | [Usage](https://fluent2.microsoft.design/components/web/react/core/tablist/usage) | Tag | [Usage](https://fluent2.microsoft.design/components/web/react/core/tag/usage) |
| TagPicker | [Usage](https://fluent2.microsoft.design/components/web/react/core/tagpicker/usage) | Text | [Usage](https://fluent2.microsoft.design/components/web/react/core/text/usage) |
| Textarea | [Usage](https://fluent2.microsoft.design/components/web/react/core/textarea/usage) | Toast | [Usage](https://fluent2.microsoft.design/components/web/react/core/toast/usage) |
| Toolbar | [Usage](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage) | Tooltip | [Usage](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage) |
| Tree | [Usage](https://fluent2.microsoft.design/components/web/react/core/tree/usage) |  |  |

若组件新增或路径变化，从 [Fluent React component index](https://fluent2.microsoft.design/components/web/react) 重新进入，不依赖旧代码示例。

## 跨平台边界

| 内容 | 适用性 | 处理方式 |
|---|---|---|
| Semantic Token、focus、内容、命令优先级 | Universal / adapted | 可迁移原则，具体组件与数值服从平台；来源 [Fluent principles](https://fluent2.microsoft.design/design-principles/) |
| Mica/Acrylic/Smoke、caption buttons、UI Automation | Windows-only | 使用 WinUI/Windows API，不在 Web/Android/Apple 声称等价；来源 [Windows materials](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/materials) |
| Fluent React/Web Components | Web/Microsoft products | 适合企业 Web 和 Microsoft 生态；不是 Windows 原生控件；来源 [Fluent React](https://fluent2.microsoft.design/components/web/react) |
| Fluent iOS/Android libraries | Microsoft product-specific | 只有项目明确需要 Microsoft 家族一致性时覆盖默认平台路由；来源 [Fluent develop](https://fluent2.microsoft.design/get-started/develop) |
| Segoe UI Variable/Segoe Fluent Icons | Windows-first | 非 Windows 提供字体/图标 fallback；来源 [Typography](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography) 与 [Icon font](https://learn.microsoft.com/en-us/windows/apps/design/iconography/segoe-fluent-icons-font) |
