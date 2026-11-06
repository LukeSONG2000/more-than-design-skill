# Platform Design Routing

用于在 Android/Material、Windows/Microsoft Fluent、Apple/HIG 与 Web 之间选择正确的规范入口。先决定产品实际运行环境，再决定视觉表达；不能用偏好的视觉语言覆盖目标平台的交互习惯。

## 目录

- [官方根入口](#官方根入口)
- [平台决策矩阵](#平台决策矩阵)
- [Web 语境决策](#web-语境决策)
- [冲突优先级](#冲突优先级)
- [跨平台翻译](#跨平台翻译)
- [适用性标签](#适用性标签)
- [调用与验收](#调用与验收)

## 官方根入口

| 体系 | 设计规范 | 开发文档 | 本 skill 路由 |
|---|---|---|---|
| Google / Android | [Android Mobile Design](https://developer.android.google.cn/design/ui/mobile)、[Material 3](https://m3.material.io/) | [Material 3 Develop](https://m3.material.io/develop)、[Adaptive Apps](https://developer.android.com/develop/adaptive-apps) | [../android/google-android-map.md](../android/google-android-map.md)；折叠屏见 [../android/android-foldable-adaptation.md](../android/android-foldable-adaptation.md) |
| Microsoft / Windows | [Windows Design](https://learn.microsoft.com/en-us/windows/apps/design/)、[Fluent 2](https://fluent2.microsoft.design/) | [Windows development](https://developer.microsoft.com/zh-cn/windows/develop)、[WinUI 3](https://learn.microsoft.com/windows/apps/winui/winui3/) | [../windows/microsoft-windows-map.md](../windows/microsoft-windows-map.md) |
| Apple | [Apple Design / HIG](https://developer.apple.com/cn/design/) | [Apple Developer Documentation](https://developer.apple.com/documentation/) | [../apple/apple-official-docs-map.md](../apple/apple-official-docs-map.md) |

## 平台决策矩阵

| 产品环境 | 主规范 | 关键约束 | 不应默认搬入 |
|---|---|---|---|
| Android 手机 | [Android Mobile](https://developer.android.google.cn/design/ui/mobile) + [Material 3](https://m3.material.io/) | Android 系统返回、edge-to-edge、WindowInsets、动态颜色、触控 | iOS 居中导航标题、Apple Tab Bar 解剖、Windows 标题栏 |
| Android 大屏/折叠屏 | [Adaptive Apps](https://developer.android.com/develop/adaptive-apps) + [Material adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design) | 五档 window size class、folding features、posture、canonical panes、多窗口与多输入 | 固定手机宽度、按设备名设计、复制 iPhone Duo 的竖向栏/API |
| Windows 桌面 | [Windows Design](https://learn.microsoft.com/en-us/windows/apps/design/) + [WinUI](https://learn.microsoft.com/windows/apps/winui/winui3/) | 窗口、标题栏、命令、键鼠、焦点、高对比度 | 移动端底部导航、触控专用手势、模拟 Mica 的普通 blur |
| iPhone/iPad | [HIG](https://developer.apple.com/design/human-interface-guidelines/) + [UIKit/SwiftUI](https://developer.apple.com/documentation/) | 系统导航、标准控件、Dynamic Type、系统材料 | Android predictive back、Windows command bar |
| macOS | [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) + [AppKit](https://developer.apple.com/documentation/appkit) | 菜单栏、窗口、工具栏、键鼠、快捷键 | 把 iPhone 页面直接放大 |
| watchOS、visionOS、CarPlay 等 | [HIG Platforms](https://developer.apple.com/design/human-interface-guidelines/platforms) | 对应硬件、输入方式与安全约束 | 作为普通 Web/移动端装饰模板 |
| Web | [HIG](https://developer.apple.com/design/human-interface-guidelines/) 为本 skill 的通用审美参考；框架、Fluent、Material 按需提供工程参考 | 尊重现有品牌；浏览器语义、响应式、输入与可访问性 | 把审美等同大留白，或把选库等同选默认外观 |

## Web 语境决策

Web 采用 HIG 作为通用审美准则，这是本 skill 的设计偏好。它在实现中指导层级、排版、对齐、重点色和视觉反馈。信息密度、留白、标题尺寸与材质服务于内容和操作：紧凑后台强调扫描与比较，内容页面强调阅读和表达。

组件库、Material 和 Fluent 按需补充组件能力、交互行为、自适应和工程约束。选型遵循实际框架指导，视觉细节结合 HIG、已有品牌和用户要求实现。成熟的交互、Web 语义和无障碍能力随实现一同保留。

简单修改直接完成，组件、交互或技术问题按需查阅资料。产品界面参考 HIG 通用原则，宣传展示任务可进一步借鉴 Apple.com 构图。此调整适用于 Web；原生平台继续遵循各自规范与行为。

### 快速选择

| 当前需要 | 按需参考 |
|---|---|
| 局部视觉完善 | 在现有实现上应用 HIG 通用审美 |
| 多窗格、命令、键盘行为存在疑问 | 查 Fluent 相关行为与工程指导 |
| 自适应或组件能力存在疑问 | 查 Material 或所用框架的能力文档 |
| 已有成熟设计系统 | 延续已有体系，在授权范围内改善视觉细节 |

## 冲突优先级

出现冲突时按以下顺序处理：

1. 目标操作系统的交互和无障碍要求。
2. 项目已有组件、品牌与技术约束。
3. 任务指定的设计体系。
4. 本 skill 的 Web HIG 审美偏好；仅在相关问题上按需参考工程资料。

不要平均混合。可组合的是原则，例如语义色、清晰层级和减少动态；不可直接混合的是控件解剖、导航语义、系统材料、返回行为和平台 API。

## 跨平台翻译

跨平台翻译目标是保留**任务语义**，不是逐像素复制。

| 语义 | Android / Material | Windows / Fluent | Apple | 翻译要求 |
|---|---|---|---|---|
| 顶层目的地 | [Navigation bar](https://m3.material.io/components/navigation-bar/guidelines) 或大屏 [Navigation rail](https://m3.material.io/components/navigation-rail/guidelines) | [NavigationView](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/navigationview) | [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | 保留目的地与状态，不复制外形；按窗口与平台换容器 |
| 返回 | [Predictive back](https://developer.android.google.cn/design/ui/mobile/guides/patterns/predictive-back) 区分系统 Back 与应用 Up | [Navigation basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics) 的历史与层级 | [Navigation and search](https://developer.apple.com/design/human-interface-guidelines/navigation-and-search) | 使用平台历史栈和手势，不自造通用返回动画 |
| 局部模式切换 | [Segmented buttons](https://m3.material.io/components/segmented-buttons/guidelines) 或 [Tabs](https://m3.material.io/components/tabs/guidelines) | [TabView](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/tab-view) 或语义合适的选择控件 | [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) | 先确认是筛选、单选还是页面导航，再选控件 |
| 临时命令 | [Menus](https://m3.material.io/components/menus/guidelines) | [Menus and context menus](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/menus) | [Menus](https://developer.apple.com/design/human-interface-guidelines/menus) | 菜单结构可共享，呈现、键盘和触控行为服从平台 |
| 表面材质 | [Surface color roles](https://m3.material.io/styles/color/roles) 与 elevation | [Mica/Acrylic/Smoke](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/materials) | [Materials/Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials) | 系统材料只在原平台使用；Web 用语义近似并明确 fallback |
| 颜色个性化 | [Dynamic color](https://m3.material.io/styles/color/dynamic/user-generated-source) | [Windows color](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/color) 的主题/强调色 | [HIG color](https://developer.apple.com/design/human-interface-guidelines/color) 的语义系统色 | 不跨平台复制具体色值，保留角色和对比关系 |
| 动效 | [Material motion](https://m3.material.io/styles/motion/overview/how-it-works) | [Fluent motion](https://fluent2.microsoft.design/motion/) | [HIG motion](https://developer.apple.com/design/human-interface-guidelines/motion) | 保留因果和连续性，参数与系统转场服从平台 |

Android 官方还提供从 iOS 迁移的逐项检查：[10 Steps to Android](https://developer.android.google.cn/design/ui/mobile/guides/foundations/translate-designs)。重点是内容先于品牌、使用 Android 系统 UI、区分 Up/Back、将 iOS segmented control 按语义转换为 tabs 或 Android 选择控件，并在完成结构与行为后再做品牌样式。

## 适用性标签

在新增或调用参考资料时使用以下标签：

- **Universal**：内容层级、语义 Token、键盘可达、对比度、减少动态等可跨平台迁移原则。
- **Platform-adapted**：目标可迁移，但组件、参数或交互必须换成目标平台实现。
- **Platform-only**：系统材质、系统导航、硬件输入、专属 API 或品牌资源，只在对应平台使用。
- **Inspiration-only**：watch、XR、CarPlay 等特殊场景对普通 Web/移动端仅供约束模型或创意启发。

## 调用与验收

### 调用模板

1. `target`: Android / Windows / Apple / Web。
2. `context`: 手机、平板、折叠屏、桌面窗口、浏览器、多输入或特殊硬件。
3. `system`: 现有组件库、品牌 Token、技术栈。
4. `reference`: 对应平台地图中的官方页面。
5. `separation`: 样式、组件、行为、动效、无障碍分别决策。
6. `fallback`: 平台专属能力在其他平台的中性替代。

### 验收问题

- 组件是否承担正确语义，而不仅是外观相似？
- 是否优先使用目标平台标准组件和系统行为？
- 导航、返回、窗口、键盘、指针和触控是否符合目标环境？
- 色彩、字体、材质、形状和 elevation 是否来自同一体系或明确的自有系统？
- 动效是否单独定义，且支持 reduced motion / animations off？
- 每项平台专属能力是否有边界说明和 fallback？
- 设计依据是否链接到官方原文？
