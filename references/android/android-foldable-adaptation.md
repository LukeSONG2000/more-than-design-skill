# Android 折叠屏与自适应应用指南

本文件整理 Google 官方 Android Mobile Design、Adaptive Apps、Material 3 Adaptive、Jetpack WindowManager 和 Adaptive app quality guidance。用于 Android 折叠屏、大屏、多窗口和可调整尺寸窗口的设计、实现与验收，并与 [iPhone Duo 指南](../apple/iphone-duo-adaptation.md)建立设计语义对齐。

## 使用边界与快照

- 资料快照日期：2026-09-15。
- 折叠屏首先是可调整尺寸的 Android App，其次才是 posture、hinge、cover screen 或双显示的专项体验。
- `Android Mobile Design` 负责平台行为与设计原则；`Material 3 Adaptive` 负责导航和窗格容器；`Jetpack WindowManager` 负责窗口指标、折叠特征和显示模式。
- 不按 Pixel、Galaxy、OPPO、vivo 或某一分辨率分支。先读取当前窗口和能力，再选择布局；厂商/设备只进入测试记录与已知兼容性清单。
- 本文件处理 layout、component behavior 和 platform capability。视觉样式仍见 [material-foundations-styles.md](material-foundations-styles.md)，动效仍见 [material-motion.md](material-motion.md)。

## 快速路由

| 任务 | 先读 |
|---|---|
| 手机布局扩展到折叠屏/平板 | 窗口容量与 canonical layout |
| 内容或控件跨越折痕/铰链 | FoldingFeature 与 HingePolicy |
| 展开后显示双窗格 | List-detail / Supporting pane |
| Navigation bar 与 rail 切换 | Adaptive navigation |
| 半折媒体、相机、阅读体验 | Tabletop / Book posture |
| 外屏、后置显示、双显示 | Foldable display modes |
| 与 iPhone Duo 共用设计模型 | Android 与 Apple Duo 语义对齐 |
| 发布质量和设备覆盖 | 质量分级与测试矩阵 |

## 1. 官方能力模型

按以下顺序做布局决策：

```text
current app window size
  -> window size class
  -> folding features and posture
  -> content relationship and pane capacity
  -> navigation component and pane scaffold
  -> insets, cutouts, input and accessibility
  -> optional foldable-only enhancement
```

### 1.1 当前窗口，不是物理屏幕

- 使用分配给 App 的当前 window metrics。全屏、分屏、自由窗口、桌面窗口和折叠开合都会改变它。
- Window size class 作用于整体 App 布局；局部组件仍应依据自己的可用约束响应。
- 不以设备类型、屏幕对角线或 orientation 作为窗口容量的替代判断。
- Android 16/API 36 面向 `smallestWidth >= 600dp` 的目标应用会忽略部分 orientation、aspect ratio 和 resizability 限制；依赖 letterbox 或锁方向不是长期适配方案。

### 1.2 Window size classes

| Width class | 范围 | 常见布局能力 |
|---|---:|---|
| Compact | `< 600dp` | 单窗格、底部 navigation bar |
| Medium | `600-839dp` | 单窗格或受控双窗格、navigation rail 候选 |
| Expanded | `840-1199dp` | 双窗格、navigation rail/drawer |
| Large | `1200-1599dp` | 双窗格与更完整 supporting pane |
| Extra large | `>= 1600dp` | 信息需要时三窗格；限制内容最大宽度 |

这些是布局决策的起点，不是“一档对应一种设备”。同一台折叠屏在外屏、内屏、分屏和桌面窗口中可以落入不同类别。

Compose 一般从 `currentWindowAdaptiveInfo()` 获取 window size class；需要 fold-aware posture 与新版容量信息时，按当前 Material 3 Adaptive 文档核对 `currentWindowAdaptiveInfoV2()` 的稳定性和 opt-in 要求。

## 2. FoldingFeature 与物理分隔

Jetpack WindowManager 的 `FoldingFeature` 是折叠区域的主要事实来源。

| 属性 | 语义 | 设计用途 |
|---|---|---|
| `bounds` | 折痕或铰链在当前窗口中的矩形 | 计算分隔区和可用 pane，不让关键内容跨越 |
| `state` | `FLAT` 或 `HALF_OPENED` | 判断是否处于非平展姿态 |
| `orientation` | `HORIZONTAL` 或 `VERTICAL` | 区分 tabletop 与 book 类布局 |
| `occlusionType` | `NONE` 或 `FULL` | 判断区域是否真的遮挡像素 |
| `isSeparating` | 是否把窗口分成逻辑区域 | 决定是否把折叠区作为 pane 分隔 |

### 2.1 关键规则

- `FULL` occlusion 区域不能放任何可见内容；`isSeparating` 为 true 时避免在铰链附近放控件，即使像素仍可见。
- 文字、关键图像主体、FAB、菜单触发器、拖放目标和对话框不能落在不可读或难以触达的折叠区域。
- 可将铰链作为两个 pane 的自然 gutter，但不要绘制装饰性“中缝”。
- 不要假设只有一个 feature。三折设备可能有多个铰链，也不一定支持 `HALF_OPENED`；布局应遍历当前 display features，并在无法形成稳定 pane 时回退到单窗格。
- 双屏设备即使报告 `FLAT`，只要 `isSeparating` 为 true，仍按两个物理区域处理。

### 2.2 API 路线

- Compose 使用 `collectFoldingFeaturesAsState()` 响应 folding features 的变化。
- 更低层或传统 View 项目使用 `WindowInfoTracker` 和 `WindowLayoutInfo`。
- Material adaptive pane scaffold 可通过 `HingePolicy` 决定 `AlwaysAvoid`、`AvoidOccluding`、`AvoidSeparating` 或 `NeverAvoid`；根据内容风险选择，不默认把所有折痕都当完全不可用。
- Android `FoldingFeature` 不提供可移植、可靠的精确 hinge angle。不要以传感器角度驱动跨厂商核心布局或关键动画。

## 3. Posture 只在有明确收益时增强

窗口尺寸决定基础布局，posture 用于少量有真实使用价值的差异化体验。

### Tabletop posture

典型条件是 `HALF_OPENED + HORIZONTAL`，或 `windowPosture.isTabletop`。

- 媒体、视频通话和相机：把主要观看/预览内容放在上方直立区域，把播放、通话或拍摄控制放在下方可触区域。
- 导航通常保留 navigation bar；官方 `NavigationSuiteScaffold` 默认会在 tabletop posture 倾向 navigation bar。
- 控制与内容仍属于同一任务，展开/合拢后应恢复普通布局和状态。

### Book posture

典型条件是 `HALF_OPENED + VERTICAL`。

- 适合长文阅读、双页文档、参考/编辑或特定相机场景。
- 左右 pane 都要有完整 readable bounds；不要让一行文字、单个图表或关键视觉主体跨过 hinge。
- RTL 需要按内容方向处理页面顺序；不能把硬件坐标直接当 leading/trailing。

### Cover screen

Android cover screen 的比例差异很大，有些接近普通手机，有些接近方形。

- 保持 edge-to-edge，并处理 camera cutout 与 system insets。
- 聚焦一个主要任务和少量可达控制，不把展开态完整三窗格压缩到外屏。
- 保留当前内容、选择和任务状态；展开后补充信息，而不是跳到无关首页。

## 4. Canonical layouts 与 pane 语义

先判断内容关系，再选容器。

| 模式 | 内容关系 | 窄窗口 | 宽窗口 | Compose 路线 |
|---|---|---|---|---|
| List-detail | 列表项与可独立理解的详情 | 列表或详情单独显示；Back 返回列表 | 列表与详情并排，可有 extra pane | `NavigableListDetailPaneScaffold` / `ListDetailPaneScaffold` |
| Supporting pane | 次要内容只有依附主内容才有意义 | 隐藏、下移或放入 sheet | 主内容 + 工具/评论/相关内容 | `NavigableSupportingPaneScaffold` / `SupportingPaneScaffold` |
| Feed | 同类内容集合，靠网格和尺度表达层级 | 单列或少列 | 自适应多列，保留合理卡片宽度 | adaptive grid / feed pattern |

### 4.1 Pane adaptation

Material 3 Adaptive 用 pane adapted value 表达窗格状态：

- `Expanded`：完整参与当前布局。
- `Hidden`：容量不足时隐藏，通过导航或明确入口访问。
- `Levitated`：以浮层形式保留辅助内容。
- `Reflowed`：将窗格内容重排到另一个 pane 下方。

这些是设计语义，不是固定动画。让 scaffold 和 `AnimatedPane` 管理默认 pane 过渡；业务状态独立于 pane 当前是否可见。

### 4.2 状态与返回

- hoist 当前选择、pane destination 和业务状态，使窗口变化只改变呈现。
- compact 下进入 detail 后，系统 Back/预测性返回应回到 list；expanded 下切换详情通常不等同于页面级导航。
- 需要在配置变化和进程重建后恢复的 pane key/选择应可保存，例如使用 `Parcelable`、`SavedStateHandle`、`rememberSaveable` 或 ViewModel 中的持久状态来源。
- 不为 compact 和 expanded 建立两套不相通的导航栈。

## 5. Adaptive navigation

- `NavigationSuiteScaffold` 根据 window size class 在 navigation bar 与 navigation rail 之间选择，并响应运行时窗口变化。
- compact 宽度、compact 高度或 tabletop posture 通常使用 navigation bar；其他较宽环境通常使用 rail。
- 目的地、选中状态和 badge 语义保持不变，只有导航容器和空间位置变化。
- 多 pane 内的局部操作留在所影响的 pane 附近；不要把所有操作集中到全局 rail。
- Android 没有 iPhone Duo 那种由系统把 toolbar/tab bar 旋转到固定硬件侧的规则。不要复制 Duo 的竖向 bar 顺序或 RTL 特例。

## 6. Insets、弹层与可达性

- edge-to-edge 内容使用 `WindowInsets`、cutout 和系统栏信息；背景可以延伸，交互前景必须保持可见可达。
- 对话框、菜单、popover-like surface 与拖放目标应避开 `FULL` occlusion 和 separating hinge。
- pane 中的触控目标仍按 Material/Android 无障碍要求设计，不因铰链附近空间紧张而缩小。
- 支持触控、键盘、鼠标/触控板和手写笔；大屏与桌面窗口不能只保留触控路径。
- 字体缩放、TalkBack、RTL、深浅色、对比度、系统动画关闭和键盘出现都要参与布局测试。

## 7. App continuity、multitasking 与生命周期

- 折叠、展开、旋转、窗口缩放和密度变化都可能触发 configuration change，Activity 可能重建。
- 保存并恢复导航位置、选中项、滚动、编辑草稿、播放位置、相机模式和进行中的任务。
- Android 12/API 31+ 的大屏默认支持 multi-window；Android 16 的大屏适配要求进一步降低了依赖锁方向/固定比例的可行性。
- 支持分屏、自由窗口、desktop windowing、Picture-in-Picture、拖放和多实例时，分别验证状态所有权与返回行为。
- 不把当前“folded/unfolded”状态写进业务模型；它是短生命周期的呈现环境。

## 8. Foldable display modes 与相机

以下属于可选、设备相关能力，不是所有 Android 折叠屏的共同基线。

### Rear display mode

- 将当前 Activity 移到展开设备的外屏，常用于使用高质量后摄自拍。
- 系统通过不可定制的确认界面让用户授权切换；不要自行伪造或跳过。
- 内屏会关闭，因此这是显示迁移，不是双屏并行。

### Dual-screen mode

- 在内外屏同时显示不同或互补内容，例如双向翻译、被摄者预览。
- 它是 secondary presentation，而不是简单镜像整个主界面。
- 能力和系统版本因设备/OEM 而异，使用 Jetpack WindowManager 做 availability 检查并提供单屏 fallback。

### Camera

- tabletop：预览在上，控制在下。
- rear display：外屏作为后摄取景器。
- dual-screen：主操作与被摄者预览分离。
- CameraX/Camera2 预览需要在窗口、姿态和显示变化后重新核对旋转、裁切、aspect ratio 与镜像；控制不能遮挡预览主体或 hinge。

## 9. 样式与动效分离

### 样式

- 使用 Material color roles、surface/elevation、shape、typography 和 spacing。
- 展开布局不是把卡片无限拉宽；使用最大内容宽度、网格和 pane 比例维持可读性。
- hinge gutter 属于布局约束，不是品牌分隔线或拟物折痕。

### 动效

- 使用 Material 3 Adaptive scaffold、`AnimatedPane`、Navigation 和 Predictive Back 提供的默认连续性。
- 动画只解释 pane 显示/隐藏、列表到详情、导航容器变化和姿态功能切换。
- Android 官方 `FoldingFeature` 不提供稳定的精确角度；不要统一设定“跟随铰链角度”的弹簧、透视或折纸动画。
- 系统动画关闭或 reduced motion 环境下，状态、层级和操作结果仍须清楚。
- Motion token 和 transition pattern 只在 [material-motion.md](material-motion.md) 维护。

## 10. Android 与 Apple Duo 语义对齐

### 10.1 可以共享的设计语义

| 共享语义 | Android 折叠屏 | iPhone Duo | 共同验收 |
|---|---|---|---|
| `availableCapacity` | Window metrics + WindowSizeClass | scene/window size + size class | 不按设备名或 orientation 决定主体布局 |
| `contentContinuity` | 保存 Activity/pane/navigation 状态 | 保持 display/scene/navigation 状态 | 开合后任务、选择和上下文不丢失 |
| `separatingRegion` | `FoldingFeature.isSeparating` + `bounds` | division reserved region | 关键内容和控件不跨物理分隔 |
| `occludingRegion` | `occlusionType == FULL` + cutout/insets | occlusion reserved region | 前景避让，背景按平台规则延伸 |
| `listDetail` | List-detail pane scaffold | Navigation split view | 窄窗口单 pane、宽窗口并排，选中项一致 |
| `supportingContent` | Supporting pane + Hidden/Levitated/Reflowed | Arrangement split/overlay | 次要内容可换位置，核心内容和任务不变 |
| `postureEnhancement` | tabletop/book posture | 部分折叠时的区域布局 | 只为明确场景增强，不为每个角度重做页面 |
| `adaptiveNavigation` | navigation bar/rail/drawer | 横向/竖向系统 bars | 目的地与状态不变，组件按平台重新呈现 |
| `secondaryDisplay` | rear/dual-screen WindowManager modes | scene accessory / CameraCaptureAccessory | 辅助显示不是完成核心任务的唯一入口 |
| `motionContinuity` | AnimatedPane / Predictive Back / Material motion | 系统容器转场 / HIG motion | 动效解释变化，减少动态时仍可理解 |

### 10.2 不能做一对一映射的能力

| 差异 | Android | iPhone Duo | 处理 |
|---|---|---|---|
| 设备形态 | 多 OEM、横折/竖折/双屏/三折、多个 hinge | 固定 Duo 设备模型 | 共享能力对象，不共享设备枚举 |
| 精确铰链角度 | `FoldingFeature` 不提供可靠通用角度 | Apple Hinge API 可用于效果 | 共享层只保留 posture category，不保留 angle 合同 |
| 系统栏 | App 通过 Material Adaptive 选择 bar/rail/drawer | 系统容器自动采用 Duo 竖向 bars | 不共享轴向、顺序、RTL 硬件侧规则 |
| 折叠区域 API | WindowManager display/folding feature | Reserved Region division/occlusion | 统一成语义 region，平台分别查询 |
| 双视图容器 | Canonical pane scaffolds 和 pane adapted values | Split view 与 Arrangement View | 按内容关系对齐，不按类名对齐 |
| 外屏并行 | rear display 或设备限定 dual-screen mode | scene accessory / camera accessory | capability check + 无辅助屏 fallback |
| 方向限制 | Android 16 在大屏覆盖部分 manifest 限制 | Duo 内屏不服从传统 orientation 假设 | 共同原则是布局不依赖锁方向，API 不共享 |

### 10.3 建议的共享能力合同

```text
AdaptiveEnvironment
  widthClass: compact | medium | expanded | large | extraLarge
  heightClass: compact | medium | expanded
  separatingRegions[]
  occludingRegions[]
  posture: flat | tabletop | book | other
  paneCapacity: one | two | three
  secondaryDisplayAvailable: bool
  inputCapabilities[]
  reduceMotion: bool
```

约束：

- 合同描述产品需要的语义，不暴露 `FoldingFeature`、`ReservedRegion` 或具体设备名。
- 平台层可把 Android Medium 映射到单 pane，也可在内容足够紧凑时映射双 pane；不要假设 Apple regular 等于 Android Expanded。
- `posture` 只控制可选增强。没有 posture 数据时，window class + region 仍能完成全部核心任务。
- `secondaryDisplayAvailable` 不能决定核心功能是否存在，只决定是否增加补充呈现。

## 11. 质量分级与测试矩阵

### 质量目标

| 等级 | 含义 | 本 skill 建议 |
|---|---|---|
| Tier 3 Adaptive ready | 全屏/全窗口运行，核心流程可完成，基础外部输入可用 | 最低兼容，不作为成熟折叠屏交付目标 |
| Tier 2 Adaptive optimized | 所有尺寸和配置都有优化布局与输入体验 | 普通生产 App 的默认交付基线 |
| Tier 1 Adaptive differentiated | 利用 posture、多任务、拖放、手写笔或相机等设备能力 | 产品场景确有收益时采用，不为评级堆功能 |

### 必测组合

- compact、medium、expanded；产品面向桌面/超大屏时再覆盖 large 与 extra large。
- folded outer/cover、unfolded inner、竖向/横向、tabletop、book；设备不支持的姿态记录为不适用。
- 单柔性屏、物理双屏；面向三折设备时覆盖多个 folding features。
- full screen、split screen、自由窗口/desktop windowing、PiP 和多实例（项目支持时）。
- `FLAT`/`HALF_OPENED`、horizontal/vertical、`NONE`/`FULL`、separating/non-separating。
- navigation bar/rail、单 pane/双 pane/三 pane、list-detail/supporting pane 的运行时切换。
- 配置变化与进程重建后的选择、滚动、草稿、播放、Back stack 和相机状态。
- TalkBack、字体缩放、RTL、键盘、鼠标/触控板、手写笔、深浅色、对比度和系统动画关闭。
- 最新 Android 与仍支持的旧版本；至少一个 fold-in with outer display 模拟器和与目标用户相符的代表性真机。
- rear display/dual-screen/camera 仅在声明支持时测试，并验证用户拒绝、不可用与中途退出路径。

官方质量指南建议使用 resizable emulator，并提供 foldable、平板、Chromebook 与双屏模拟环境。测试报告应记录窗口 dp、size class、folding features、posture、导航/pane 状态、Android/API、WindowManager/Material Adaptive 版本、设备/OEM 和 fallback。

## 12. 官方来源地图

### 设计

- [Android Design for mobile](https://developer.android.com/design/ui/mobile)
- [Adapt layout](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout)
- [Postures and orientation](https://developer.android.com/design/ui/mobile/guides/layout-and-content/postures-and-orientation)
- [Material 3 adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design)
- [Material canonical layouts](https://m3.material.io/foundations/layout/canonical-examples/overview)

### Adaptive Apps 与 foldables

- [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)
- [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps)
- [Support different display sizes](https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes)
- [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes)
- [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
- [Canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts)
- [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)
- [Build a list-detail layout](https://developer.android.com/develop/adaptive-apps/guides/list-detail)
- [Build a supporting pane layout](https://developer.android.com/develop/adaptive-apps/guides/build-a-supporting-pane-layout)
- [Learn about foldables](https://developer.android.com/develop/adaptive-apps/guides/foldables/learn-about-foldables)
- [Make your app fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware)
- [Support foldable display modes](https://developer.android.com/develop/adaptive-apps/guides/foldables/support-foldable-display-modes)
- [Support trifolds and landscape foldables](https://developer.android.com/develop/adaptive-apps/guides/foldables/trifolds-and-landscape-foldables)
- [Support camera on multiple form factors](https://developer.android.com/develop/adaptive-apps/guides/camera-form-factors-support)
- [App orientation, aspect ratio, and resizability](https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability)

### API 与质量

- [Jetpack WindowManager](https://developer.android.com/jetpack/androidx/releases/window)
- [`FoldingFeature`](https://developer.android.com/reference/androidx/window/layout/FoldingFeature)
- [Material 3 Adaptive `HingePolicy`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/HingePolicy)
- [Material 3 Adaptive `PaneAdaptedValue`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/PaneAdaptedValue)
- [Adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)
- [Foldable quality tests](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables)
