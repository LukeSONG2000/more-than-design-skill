# iPhone Duo 折叠屏适配指南

本文件整理 Apple Human Interface Guidelines 的 iPhone Duo 页面、关联 HIG 子页面，以及 Apple 的六个 iPhone Duo Tech Talk。用于设计、实现和验收 iPhone Duo 原生应用，也用于提取可迁移到其他折叠屏平台的布局原则。

## 使用边界与版本状态

- iPhone Duo 仍属于 iPhone，先遵守 iOS 的导航、触控、文字、无障碍和系统组件规范，再处理双显示与折叠姿态。
- 本文快照日期为 2026-09-15。Apple 当前将 Xcode 27.1 标为 Beta，并说明完整的开发适配文章仍将于本月稍后提供。
- `ReservedRegion`、Arrangement View、竖向系统栏、Hinge、场景附件和 Duo 相机能力按 iOS 27.1 SDK 资料记录。发布前必须对照最终 SDK、availability 和最新文档复核。
- 本文主要是 `layout`、`component behavior` 与 `platform capability` 指南，不是动画参数表。标准组件的布局和系统转场由系统负责；铰链数据只用于有意义的效果与交互。

## 快速路由

| 任务 | 先看 |
|---|---|
| 现有 iPhone App 适配 Duo | 基线、动态布局、标准容器、测试矩阵 |
| 内容跨过铰链或摄像头 | Reserved regions |
| 主从、上下或叠层内容 | Split views 与 Arrangement View |
| 导航栏、工具栏、Tab Bar | 竖向系统栏 |
| 多窗口、双显示内容 | Multitasking、scenes 与 scene accessories |
| 姿态驱动效果 | Hinge：只做效果，不做主体布局 |
| 相机 App | 双前摄与方向协调 |
| Android/Web 折叠屏 | 跨平台翻译边界 |

## 1. 设备模型

iPhone Duo 有外屏、内屏和中央铰链，两块显示各有前置摄像头。

- 闭合时使用外屏。外屏较宽且较矮，系统将导航、工具栏和 Tab Bar 放在侧边，为内容保留垂直空间。
- 展开且内屏处于横向形态时，系统栏继续位于侧边，保持从外屏到内屏的位置连续性。
- 内屏纵向形态仍使用常规横向系统栏。
- 外屏摄像头始终可见，并可扩展为 Dynamic Island；内屏摄像头位于屏下，只在启用时形成需要避让的区域。
- 部分折叠时，中央折叠区会把内屏划分成多个可用区域。

不要为“书本、帐篷、桌面”等每个姿态分别设计一套页面。Apple 的基础模型是：外屏通常提供 compact width，内屏通常提供 regular width；App 根据当前可用空间扩展既有信息结构。

## 2. 不可妥协的适配原则

1. **可调整尺寸优先。** 使用 size class、布局边距和 safe area，不依赖固定宽度、固定分辨率或设备型号。
2. **状态和功能连续。** 开合、旋转、分屏和姿态变化后保留选择、滚动、编辑、播放与导航上下文。
3. **信息层级可以展开，任务不能改变。** 外屏可只显示列表或详情，内屏可并排显示两层；两边必须能完成同一核心任务。
4. **先用标准容器。** `NavigationStack`、`NavigationSplitView`、`TabView`、`UISplitViewController`、`UITabBarController`、系统 sheet、popover、alert 和 context menu 会自动处理大量 Duo 行为。
5. **只移动必要元素。** 折叠时优先小范围位移、缩放或重新分配空间，避免整个界面突然换位。
6. **背景和前景分层处理。** 交互前景留在 safe area；允许背景图像或颜色延伸到边缘。
7. **每条边独立计算。** Duo 的 safe area 和 layout margins 可能不对称，不能用左侧 inset 乘二推导可用宽度。

## 3. 动态布局决策

### 3.1 判断顺序

```text
available size / size class
  -> safe area and layout margins
  -> active reserved regions
  -> semantic container choice
  -> overflow and control priority
  -> optional hinge-driven effects
```

- 用 SwiftUI Environment 或 UIKit trait collection 读取 size class。
- 不以 interface orientation 决定信息结构；内屏不保证遵循 App 声明的 supported interface orientations。
- 不使用 `UIScreen.main` 推断当前显示。双显示环境中它有歧义；使用 scene bounds、trait、SwiftUI environment 或 `windowScene.screen`。
- 需要贴合屏幕圆角时使用系统 Concentricity 能力，例如 `ConcentricRectangle` 或 `UICornerConfiguration`，不要手填某款设备的圆角值。

### 3.2 内容连续性

- compact：保留一个主工作面，通过导航在列表和详情之间切换。
- regular：可以同时显示列表与详情、主内容与辅助内容，但不改变数据状态和操作结果。
- 改变尺寸时不要重置导航栈、已选项、筛选、编辑草稿或媒体位置。
- 可滚动文章和 Feed 通常应继续自然流动，不要为了铰链把连续内容整体位移。

## 4. Reserved regions

Reserved region 表示内容需要避开、或组件需要适配的显示区域。

| 区域 | 类型 | 状态 | 处理 |
|---|---|---|---|
| 外屏摄像头 / Dynamic Island | occlusion | 始终存在，活动内容可能扩展 | 使用 safe area 和系统栏；自定义边缘 UI 查询区域 |
| 内屏屏下摄像头 | occlusion | 摄像头启用时出现 | 相机激活后让关键内容移开，不预留永久空洞 |
| 中央折叠区 | division | 部分折叠时活动，完全展开时为零宽 | 不让关键控件、文字或单个视觉主体跨越中心 |

### 4.1 选择位移范围

- 独立元素能单独避让时，只移动该元素。
- 多个元素构成一个语义整体时，一起移动容器，保留内部关系。
- 书本姿态通常把提示或辅助面板移到 trailing 区域；桌面姿态通常把远距离查看内容放上区、操作控件放下区。
- 网格优先使用偶数列，使内容自然分到铰链两侧；可查询 inactive division region，提前决定列数，但不要为平展状态制造可见缝隙。
- 系统 presentation 已会自动避让时，不再叠加自定义 offset。

### 4.2 API 边界

- SwiftUI 从 `GeometryProxy` 查询 reserved regions；UIKit 从 `UIView` 查询对应区域及 frame。
- 默认只返回活动区域；`.includeInactive` 适合高层级布局决策。
- Reserved region 用于布局。不要用实时 hinge angle 反推安全区或手写中心禁区。

## 5. Split views 与 Arrangement View

### 5.1 标准 split view

- 使用 `NavigationSplitView` 或 `UISplitViewController` 表达主从导航。
- 外屏或窄窗口折叠为单列；内屏或宽窗口展开为多列。
- 让系统管理列宽、margin 和折叠区域；只配置内容优先级与列语义。

### 5.2 Arrangement View

Arrangement View 是 iOS 27.1 的双视图布局容器，包含 primary 与 secondary，不承担导航。

| Arrangement | 适用关系 | 自适应方式 |
|---|---|---|
| split | 现有 `HStack` / `VStack`、主内容与详情，任何一侧都不应被遮挡 | 较宽时左右分，较高时上下分；可限制轴 |
| overlay | 现有 `ZStack`、明确的前景与背景，允许次要内容被部分覆盖或折叠 | 平展时叠放，折叠时分到两侧；可根据 z-index 切换次要视图状态 |

规则：

- SwiftUI 使用 `ArrangementView`；UIKit 使用 `UIArrangementViewController`。
- 把 `NavigationStack`、`NavigationSplitView` 或 `TabView` 放在 Arrangement View 外部。
- 不要把 Arrangement View 放进 `List` 或 `ScrollView`。
- 如果现有布局不是明确的双视图关系，不要为了使用新 API 强行拆成 primary/secondary。

## 6. 竖向系统栏

竖向栏是 iPhone Duo 的核心平台模式，不是可随意仿制的视觉样式。

### 6.1 原生优先

- SwiftUI 将 `.toolbar` 与 `NavigationStack` 或 `NavigationSplitView` 配合。
- UIKit 优先 `UINavigationController` 与 `UITabBarController`。孤立的自定义 `UIToolbar`、`UINavigationBar` 或 `UITabBar` 内容不会自动获得完整的容器级竖向布局判断。
- 在 Split View 中，通常只有 detail 列参与共享侧边栏区域；inspector 不获得独立系统栏。
- 侧边位置与硬件对齐，在 RTL 中不会镜像到另一侧；文案和内容方向仍按本地化规则处理。

### 6.2 顺序与分组

1. 顶部放 Back、Close 等主导航。
2. 紧随其后放 Done 等 prominent action。
3. 其余条目保留原有语义分组，由系统处理间距。
4. 控件留在它所影响的内容附近；不要把 leading pane 的局部操作强行塞到全局侧边栏。

- 同时提供 symbol 与 title，让系统按轴和 overflow 场景选择表示；title 也用于扩展形式和菜单。
- 尽量减少纯文本 toolbar item，因为文本项会留在横向栏。
- 自定义 view 默认按横向处理；能适配竖向时设置 vertical preferred，只能横向时明确 horizontal only。

### 6.3 Overflow 与压缩

- 默认从底部向顶部溢出。先对 item group，再对单项设置 visibility priority。
- 高频操作和表达状态的条目应最后溢出。
- 导航型界面通常优先保留 Tab Bar，让 toolbar item 进入 overflow。
- 任务型界面可选择优先保留 toolbar，压缩 Tab Bar。
- 使用 `ToolbarOverflowMenu` 或 UIKit 的 `additionalOverflowItems` 合并额外操作；省略号只表示 overflow。
- 大多数 App 保留系统默认竖向行为。只有沉浸式单页、无滚动且无需栏的界面，或只有一个控制项的轻量 sheet，才考虑 opt out。

### 6.4 样式与动效边界

- 栏的轴向、背景、滚动边缘效果、Item 过渡和 overflow 呈现由系统决定。
- App 只提供语义、分组、优先级、symbol/title 和少量公开配置。
- 不为竖向栏手写旋转、位移或弹簧动画，也不把其形态作为 Web/Android 的通用样式。
- 自定义竖向栏默认没有系统 scroll-edge effect；启用 Reduce Transparency 时系统仍会提供可读背景。

## 7. Multitasking、scenes 与多显示

- 所有 App 都要适应 Duo Split View；把视频与 App 上下堆叠等布局视为普通窗口变化，通过 size class 与 scene geometry 处理。
- 保存和恢复工作上下文，因为开合、分屏、场景切换和系统回收都可能突然发生。
- iPhone Duo 支持多个 UI scene 实例；外屏不能总是创建新窗口。场景激活请求必须处理失败，优先使用系统提供、不可用时会隐藏的窗口创建操作。
- Scene accessory 由系统动态决定是否可用。它只能补充主界面，核心任务在没有 accessory 时仍必须完整可用。
- `CameraCaptureAccessory` 可在内屏全屏相机活动时，把补充界面放到外屏；在同一个相机 view 上注册并监听 availability。

这些能力属于 Apple/Duo 专项。一般跨平台产品可以迁移“多窗口状态连续”和“辅助显示不可作为唯一入口”原则，但不能复制其 API 或系统窗口行为。

## 8. Hinge：只用于效果与交互

SwiftUI 的 hinge change 能力和 UIKit 的 `UIHingeInteraction` 可以报告闭合、部分展开、完全展开及角度。

- 布局避让使用 size class、safe area、reserved regions 和 Arrangement View。
- hinge angle 适合驱动视差、内容倾斜、物理反馈或姿态相关交互，不用于主体布局尺寸计算。
- 只有 partially open 状态需要持续响应角度；离开该状态时重置效果状态。
- 在无铰链设备上 hinge 可能不存在，必须有无效果 fallback。
- Respect Reduce Motion；信息、选择和操作结果不能依赖角度动画表达。

## 9. 双前摄与相机 App

该节仅在产品真正提供相机采集时加载。

- 虚拟前置摄像头会在内外摄像头之间自动切换，但只暴露两者共有的能力。
- 需要完整硬件能力时分别访问 outer/inner camera，并用 `AVCaptureDeviceDirectionCoordinator` 根据目标 view 和当前显示方向选择设备。
- `front` 在双面显示设备上不足以描述“朝向用户”；方向相对于承载预览的 view。双显示同时工作时，每个 view 使用独立 coordinator。
- 方向变化后在合适的 capture session 隔离范围内重新配置设备，并考虑镜像。
- 校验 preview layer 的 `videoGravity`、相机 `dynamicAspectRatio` 和 rotation coordinator。
- 采用 rotation coordinator 后，按官方建议评估关闭 sensor orientation compensation 以减少额外处理。

## 10. 游戏

- 可以锁定 portrait 或 landscape，但设备姿态变化时仍要填满可用显示。
- 尽量保持文字和控制尺寸稳定，通过调整画面 aspect ratio 适配。
- 优先改变取景范围或构图，不优先使用 letterbox/pillarbox。
- 无法避免留边时，用与场景连续的美术扩展填充，不把重要玩法放进 reserved region。

## 11. 跨平台翻译边界

| 原则/能力 | 可迁移部分 | Apple/Duo 专有部分 | Android 对应 |
|---|---|---|---|
| 自适应尺寸 | 基于当前窗口容量重排 | Duo 外/内屏 size class 组合 | Material Adaptive window size classes |
| 折叠避让 | 关键内容不跨铰链，位移最小化 | `ReservedRegion` / `UIViewReservedRegion` | `FoldingFeature` bounds/occlusion/separation + HingePolicy |
| 双视图布局 | 主从、split、overlay 语义 | `ArrangementView` / `UIArrangementViewController` | List-detail/Supporting pane 与 pane adapted values |
| 系统导航 | 标准组件优先、操作可达 | Duo 竖向 bars、固定硬件侧、系统 overflow | `NavigationSuiteScaffold` 按窗口容量选择 bar/rail |
| 姿态效果 | 能力检测、减少动态、无效果 fallback | Hinge APIs 可提供实时角度 | WindowManager posture；`FoldingFeature` 不提供可靠通用角度 |
| 多显示 | 状态连续、辅助显示不是唯一入口 | scene accessory / CameraCaptureAccessory | Android multi-display/window APIs |
| 相机方向 | 相对目标 surface 选择摄像头 | Duo virtual front camera 与 direction coordinator | CameraX/Camera2 按设备能力实现 |

不要在 Android 或 Web 上画一条中缝、复制 Duo 竖向栏，或声称自定义折叠动画等同系统行为。跨平台共享的是任务语义、容量判断、避让原则和测试方法。

完整的 Android 官方路线、差异和共享能力合同见 [../android/android-foldable-adaptation.md](../android/android-foldable-adaptation.md)。

## 12. 验收矩阵

至少覆盖：

- 外屏与内屏；完全闭合、完全展开、书本式部分折叠、桌面式部分折叠。
- 内外屏各自可用的纵向/横向形态，以及 Split View 与视频堆叠窗口。
- compact/regular size class 切换，键盘出现，超大 Dynamic Type。
- safe area 四边不对称、摄像头区域活动、fold division region 活动/不活动。
- 标准栏的横向/竖向切换、RTL 固定硬件侧、overflow、优先级和 compression。
- 列表/详情、媒体、编辑草稿、筛选与滚动位置在开合过程中的连续性。
- VoiceOver、Reduce Motion、Reduce Transparency、Increase Contrast、深浅色。
- 新 API 不可用、非 Duo iPhone 和旧系统 fallback。
- 相机项目额外覆盖内外摄像头切换、镜像、预览裁切、旋转与双显示。

验收证据应记录 Xcode/SDK 版本、模拟器或真机、当前 display、pose、size class、reserved regions、窗口模式和 fallback 路径。只证明“能编译”不等于完成 Duo 适配。

## 13. 官方来源地图

### HIG 与开发入口

- [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)
- [Get ready for iPhone Duo](https://developer.apple.com/iphone-duo/)
- [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)
- [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)
- [SwiftUI `ToolbarOverflowMenu`](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu)
- [SwiftUI `sceneAccessory(content:)`](https://developer.apple.com/documentation/swiftui/view/sceneaccessory%28content%3A%29)

### Apple Tech Talks

- [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/)
- [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/)
- [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/)
- [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463/)
- [Leverage multiple displays and scenes on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111464/)
- [Build a great camera experience for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111465/)
