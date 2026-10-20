# Material 3 Components Map

Material 3 组件的官方索引。每个组件优先按 `overview → guidelines → specs → accessibility` 阅读：先判断语义与行为，再取视觉数值，最后验证输入和辅助技术。

## 目录

- [选择原则](#选择原则)
- [完整组件索引](#完整组件索引)
- [导航与自适应](#导航与自适应)
- [输入与选择](#输入与选择)
- [反馈与浮层](#反馈与浮层)
- [开发映射](#开发映射)
- [跨平台边界](#跨平台边界)

## 选择原则

1. 从用户任务和信息结构选组件，不从截图或圆角选组件；总入口见 [Material components](https://m3.material.io/components)。
2. 保留组件默认状态、语义和尺寸，除非官方 customization 接口支持覆盖；参考 [Material customization](https://m3.material.io/foundations/customization)。
3. 导航组件按目的地数量与窗口类别变化；参考 [Adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design)。
4. 选择、命令、导航和信息反馈不可仅因外形相近而互换。
5. Android 优先 Compose/Views 原生实现，Web/Flutter 使用对应官方实现；Apple/Windows 改用目标平台语义等价组件。

## 完整组件索引

| 组件 | Overview | Guidelines | Specs | Accessibility |
|---|---|---|---|---|
| App bars | [Overview](https://m3.material.io/components/app-bars/overview) | [Guidelines](https://m3.material.io/components/app-bars/guidelines) | [Specs](https://m3.material.io/components/app-bars/specs) | [Accessibility](https://m3.material.io/components/app-bars/accessibility) |
| Badges | [Overview](https://m3.material.io/components/badges/overview) | [Guidelines](https://m3.material.io/components/badges/guidelines) | [Specs](https://m3.material.io/components/badges/specs) | [Accessibility](https://m3.material.io/components/badges/accessibility) |
| Bottom sheets | [Overview](https://m3.material.io/components/bottom-sheets/overview) | [Guidelines](https://m3.material.io/components/bottom-sheets/guidelines) | [Specs](https://m3.material.io/components/bottom-sheets/specs) | [Accessibility](https://m3.material.io/components/bottom-sheets/accessibility) |
| Button groups | [Overview](https://m3.material.io/components/button-groups/overview) | [Guidelines](https://m3.material.io/components/button-groups/guidelines) | [Specs](https://m3.material.io/components/button-groups/specs) | [Accessibility](https://m3.material.io/components/button-groups/accessibility) |
| Buttons | [Overview](https://m3.material.io/components/buttons/overview) | [Guidelines](https://m3.material.io/components/buttons/guidelines) | [Specs](https://m3.material.io/components/buttons/specs) | [Accessibility](https://m3.material.io/components/buttons/accessibility) |
| Cards | [Overview](https://m3.material.io/components/cards/overview) | [Guidelines](https://m3.material.io/components/cards/guidelines) | [Specs](https://m3.material.io/components/cards/specs) | [Accessibility](https://m3.material.io/components/cards/accessibility) |
| Carousel | [Overview](https://m3.material.io/components/carousel/overview) | [Guidelines](https://m3.material.io/components/carousel/guidelines) | [Specs](https://m3.material.io/components/carousel/specs) | [Accessibility](https://m3.material.io/components/carousel/accessibility) |
| Checkbox | [Overview](https://m3.material.io/components/checkbox/overview) | [Guidelines](https://m3.material.io/components/checkbox/guidelines) | [Specs](https://m3.material.io/components/checkbox/specs) | [Accessibility](https://m3.material.io/components/checkbox/accessibility) |
| Chips | [Overview](https://m3.material.io/components/chips/overview) | [Guidelines](https://m3.material.io/components/chips/guidelines) | [Specs](https://m3.material.io/components/chips/specs) | [Accessibility](https://m3.material.io/components/chips/accessibility) |
| Date pickers | [Overview](https://m3.material.io/components/date-pickers/overview) | [Guidelines](https://m3.material.io/components/date-pickers/guidelines) | [Specs](https://m3.material.io/components/date-pickers/specs) | [Accessibility](https://m3.material.io/components/date-pickers/accessibility) |
| Dialogs | [Overview](https://m3.material.io/components/dialogs/overview) | [Guidelines](https://m3.material.io/components/dialogs/guidelines) | [Specs](https://m3.material.io/components/dialogs/specs) | [Accessibility](https://m3.material.io/components/dialogs/accessibility) |
| Divider | [Overview](https://m3.material.io/components/divider/overview) | [Guidelines](https://m3.material.io/components/divider/guidelines) | [Specs](https://m3.material.io/components/divider/specs) | [Accessibility](https://m3.material.io/components/divider/accessibility) |
| Extended FAB | [Overview](https://m3.material.io/components/extended-fab/overview) | [Guidelines](https://m3.material.io/components/extended-fab/guidelines) | [Specs](https://m3.material.io/components/extended-fab/specs) | [Accessibility](https://m3.material.io/components/extended-fab/accessibility) |
| FAB menu | [Overview](https://m3.material.io/components/fab-menu/overview) | [Guidelines](https://m3.material.io/components/fab-menu/guidelines) | [Specs](https://m3.material.io/components/fab-menu/specs) | [Accessibility](https://m3.material.io/components/fab-menu/accessibility) |
| Floating action button | [Overview](https://m3.material.io/components/floating-action-button/overview) | [Guidelines](https://m3.material.io/components/floating-action-button/guidelines) | [Specs](https://m3.material.io/components/floating-action-button/specs) | [Accessibility](https://m3.material.io/components/floating-action-button/accessibility) |
| Icon buttons | [Overview](https://m3.material.io/components/icon-buttons/overview) | [Guidelines](https://m3.material.io/components/icon-buttons/guidelines) | [Specs](https://m3.material.io/components/icon-buttons/specs) | [Accessibility](https://m3.material.io/components/icon-buttons/accessibility) |
| Lists | [Overview](https://m3.material.io/components/lists/overview) | [Guidelines](https://m3.material.io/components/lists/guidelines) | [Specs](https://m3.material.io/components/lists/specs) | [Accessibility](https://m3.material.io/components/lists/accessibility) |
| Loading indicator | [Overview](https://m3.material.io/components/loading-indicator/overview) | [Guidelines](https://m3.material.io/components/loading-indicator/guidelines) | [Specs](https://m3.material.io/components/loading-indicator/specs) | [Accessibility](https://m3.material.io/components/loading-indicator/accessibility) |
| Menus | [Overview](https://m3.material.io/components/menus/overview) | [Guidelines](https://m3.material.io/components/menus/guidelines) | [Specs](https://m3.material.io/components/menus/specs) | [Accessibility](https://m3.material.io/components/menus/accessibility) |
| Navigation bar | [Overview](https://m3.material.io/components/navigation-bar/overview) | [Guidelines](https://m3.material.io/components/navigation-bar/guidelines) | [Specs](https://m3.material.io/components/navigation-bar/specs) | [Accessibility](https://m3.material.io/components/navigation-bar/accessibility) |
| Navigation drawer | [Overview](https://m3.material.io/components/navigation-drawer/overview) | [Guidelines](https://m3.material.io/components/navigation-drawer/guidelines) | [Specs](https://m3.material.io/components/navigation-drawer/specs) | [Accessibility](https://m3.material.io/components/navigation-drawer/accessibility) |
| Navigation rail | [Overview](https://m3.material.io/components/navigation-rail/overview) | [Guidelines](https://m3.material.io/components/navigation-rail/guidelines) | [Specs](https://m3.material.io/components/navigation-rail/specs) | [Accessibility](https://m3.material.io/components/navigation-rail/accessibility) |
| Progress indicators | [Overview](https://m3.material.io/components/progress-indicators/overview) | [Guidelines](https://m3.material.io/components/progress-indicators/guidelines) | [Specs](https://m3.material.io/components/progress-indicators/specs) | [Accessibility](https://m3.material.io/components/progress-indicators/accessibility) |
| Radio button | [Overview](https://m3.material.io/components/radio-button/overview) | [Guidelines](https://m3.material.io/components/radio-button/guidelines) | [Specs](https://m3.material.io/components/radio-button/specs) | [Accessibility](https://m3.material.io/components/radio-button/accessibility) |
| Search | [Overview](https://m3.material.io/components/search/overview) | [Guidelines](https://m3.material.io/components/search/guidelines) | [Specs](https://m3.material.io/components/search/specs) | [Accessibility](https://m3.material.io/components/search/accessibility) |
| Segmented buttons | [Overview](https://m3.material.io/components/segmented-buttons/overview) | [Guidelines](https://m3.material.io/components/segmented-buttons/guidelines) | [Specs](https://m3.material.io/components/segmented-buttons/specs) | [Accessibility](https://m3.material.io/components/segmented-buttons/accessibility) |
| Side sheets | [Overview](https://m3.material.io/components/side-sheets/overview) | [Guidelines](https://m3.material.io/components/side-sheets/guidelines) | [Specs](https://m3.material.io/components/side-sheets/specs) | [Accessibility](https://m3.material.io/components/side-sheets/accessibility) |
| Sliders | [Overview](https://m3.material.io/components/sliders/overview) | [Guidelines](https://m3.material.io/components/sliders/guidelines) | [Specs](https://m3.material.io/components/sliders/specs) | [Accessibility](https://m3.material.io/components/sliders/accessibility) |
| Snackbar | [Overview](https://m3.material.io/components/snackbar/overview) | [Guidelines](https://m3.material.io/components/snackbar/guidelines) | [Specs](https://m3.material.io/components/snackbar/specs) | [Accessibility](https://m3.material.io/components/snackbar/accessibility) |
| Split button | [Overview](https://m3.material.io/components/split-button/overview) | [Guidelines](https://m3.material.io/components/split-button/guidelines) | [Specs](https://m3.material.io/components/split-button/specs) | [Accessibility](https://m3.material.io/components/split-button/accessibility) |
| Switch | [Overview](https://m3.material.io/components/switch/overview) | [Guidelines](https://m3.material.io/components/switch/guidelines) | [Specs](https://m3.material.io/components/switch/specs) | [Accessibility](https://m3.material.io/components/switch/accessibility) |
| Tabs | [Overview](https://m3.material.io/components/tabs/overview) | [Guidelines](https://m3.material.io/components/tabs/guidelines) | [Specs](https://m3.material.io/components/tabs/specs) | [Accessibility](https://m3.material.io/components/tabs/accessibility) |
| Text fields | [Overview](https://m3.material.io/components/text-fields/overview) | [Guidelines](https://m3.material.io/components/text-fields/guidelines) | [Specs](https://m3.material.io/components/text-fields/specs) | [Accessibility](https://m3.material.io/components/text-fields/accessibility) |
| Time pickers | [Overview](https://m3.material.io/components/time-pickers/overview) | [Guidelines](https://m3.material.io/components/time-pickers/guidelines) | [Specs](https://m3.material.io/components/time-pickers/specs) | [Accessibility](https://m3.material.io/components/time-pickers/accessibility) |
| Toolbars | [Overview](https://m3.material.io/components/toolbars/overview) | [Guidelines](https://m3.material.io/components/toolbars/guidelines) | [Specs](https://m3.material.io/components/toolbars/specs) | [Accessibility](https://m3.material.io/components/toolbars/accessibility) |
| Tooltips | [Overview](https://m3.material.io/components/tooltips/overview) | [Guidelines](https://m3.material.io/components/tooltips/guidelines) | [Specs](https://m3.material.io/components/tooltips/specs) | [Accessibility](https://m3.material.io/components/tooltips/accessibility) |

Material 3 还提供按按钮族汇总的 [All buttons](https://m3.material.io/components/all-buttons)。若 sitemap 出现新组件，以 [Components](https://m3.material.io/components) 与 [sitemap](https://m3.material.io/sitemap.xml) 为准。

## 导航与自适应

### 顶层导航

[Navigation bar guidelines](https://m3.material.io/components/navigation-bar/guidelines) 的关键约束：

- 用于 3–5 个同级顶层目的地，主要面向 compact/medium 窗口，不是桌面导航的默认答案。
- 图标和标签共同表达目的地；一个时刻只有一个 active indicator。
- 可用 filled active icon / outlined inactive icon 或字重变化增强状态，但不能只靠颜色。
- 目的地切换应有明确的状态保留或重置策略；再次选择当前目的地通常返回顶部。
- 不以横向 swipe 在顶层目的地之间切换。
- expanded 窗口优先考虑 [Navigation rail](https://m3.material.io/components/navigation-rail/guidelines) 或 [Navigation drawer](https://m3.material.io/components/navigation-drawer/guidelines)。

### 页面内导航

- [Tabs](https://m3.material.io/components/tabs/guidelines) 用于同一上下文中的同级内容视图，不替代 app 顶层目的地。
- [Segmented buttons](https://m3.material.io/components/segmented-buttons/guidelines) 用于有限选项的单选或多选；先明确 selection 而非 navigation。
- [App bars](https://m3.material.io/components/app-bars/guidelines) 承载页面上下文、导航和少量相关动作，不应塞入所有命令。

## 输入与选择

| 需求 | 组件 | 选择依据 |
|---|---|---|
| 独立布尔设置，变更可立即生效 | [Switch](https://m3.material.io/components/switch/guidelines) | 标签表达设置本身，不写“开启/关闭”作为唯一文本 |
| 从若干互斥项中选一个 | [Radio button](https://m3.material.io/components/radio-button/guidelines) | 同时展示全部选项，有明确 group label |
| 一个或多个独立选择 | [Checkbox](https://m3.material.io/components/checkbox/guidelines) | 支持 checked/unchecked/indeterminate 语义 |
| 有限紧凑选项 | [Segmented buttons](https://m3.material.io/components/segmented-buttons/guidelines) | 明确单选或多选，不承担复杂导航 |
| 连续值或范围 | [Sliders](https://m3.material.io/components/sliders/guidelines) | 提供当前值、键盘/辅助技术输入和必要的精确替代 |
| 自由文本 | [Text fields](https://m3.material.io/components/text-fields/guidelines) | label 持续可见，错误与帮助文本有语义关联 |
| 日期/时间 | [Date pickers](https://m3.material.io/components/date-pickers/guidelines)、[Time pickers](https://m3.material.io/components/time-pickers/guidelines) | 支持 locale、键盘输入、范围和错误状态 |

## 反馈与浮层

- [Snackbar](https://m3.material.io/components/snackbar/guidelines) 用于短暂、非阻塞反馈，可带一个相关动作；不承载需要长时间阅读或必须确认的信息。
- [Dialogs](https://m3.material.io/components/dialogs/guidelines) 阻断当前流程，只用于需要用户关注和决策的内容；不要把普通表单都放进 dialog。
- [Bottom sheets](https://m3.material.io/components/bottom-sheets/guidelines) 面向移动触控的补充内容或操作；宽屏可按语义换为 [Side sheets](https://m3.material.io/components/side-sheets/guidelines)。
- [Menus](https://m3.material.io/components/menus/guidelines) 提供临时命令/选择；层级、键盘、焦点恢复和 dismiss 行为必须完整。
- [Loading indicator](https://m3.material.io/components/loading-indicator/guidelines) 与 [Progress indicators](https://m3.material.io/components/progress-indicators/guidelines) 按 determinate/indeterminate 和等待长度选择，并向辅助技术暴露状态。
- [Badges](https://m3.material.io/components/badges/guidelines) 是补充状态，不替代可读标签，也不承载复杂内容。

## 开发映射

| 技术栈 | 官方入口 | 实现要求 |
|---|---|---|
| Jetpack Compose | [Material 3 Compose](https://m3.material.io/develop/android/jetpack-compose) | 新 Android UI 优先；使用官方组件、主题和 adaptive API |
| Android Views | [MDC Android](https://m3.material.io/develop/android/mdc-android) | 现有 View 项目按组件库与主题迁移 |
| Flutter | [Material Flutter](https://m3.material.io/develop/flutter) | 使用 Flutter Material 3，但平台导航/输入仍需适配 |
| Web | [Material Web](https://m3.material.io/develop/web) | 先核对框架、维护状态和浏览器语义，避免复制 Android-only 行为 |

## 跨平台边界

- Android 页面直接使用 Material 组件时，系统返回、系统栏、输入法和窗口 inset 仍由 Android 规范决定，参考 [Android Mobile](https://developer.android.google.cn/design/ui/mobile)。
- iOS/macOS/Windows 不因视觉相似而复用 Material navigation bar、FAB 或 bottom sheet 解剖；换成目标平台官方组件，参考 [Platform routing](../cross-platform/platform-routing.md)。
- Web 可使用 Material 组件系统，但应保留 HTML 语义、键盘、hover/focus 和浏览器缩放；不能只复刻移动截图。
- Material 的 Wear/XR 组件属于特殊平台；除非任务明确面向相应设备，否则只作启发，入口以 [Material sitemap](https://m3.material.io/sitemap.xml) 为准。
