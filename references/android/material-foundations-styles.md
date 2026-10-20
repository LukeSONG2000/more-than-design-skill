# Material 3 Foundations & Styles

本文件只整理 Material 3 的基础原则与视觉样式。动效参数和转场模式单独见 [material-motion.md](material-motion.md)，组件行为与规格见 [material-components-map.md](material-components-map.md)。

## 目录

- [基础原则](#基础原则)
- [无障碍与内容](#无障碍与内容)
- [Design Token 与定制](#design-token-与定制)
- [输入与状态](#输入与状态)
- [自适应布局](#自适应布局)
- [颜色](#颜色)
- [排版](#排版)
- [Elevation](#elevation)
- [Shape](#shape)
- [Spacing](#spacing)
- [Icons](#icons)
- [跨平台边界](#跨平台边界)

## 基础原则

Material 3 是可适配的 Design System，不是固定皮肤。Android 项目应同时遵守 Android 平台行为与 Material 组件规范；Flutter/Web 可使用 Material 的语义和组件，但不能自动继承 Android 系统导航。入口见 [Material 3](https://m3.material.io/) 与 [Android Mobile Design](https://developer.android.google.cn/design/ui/mobile)。

实现顺序：

1. 先确定内容、任务、导航和输入方式，参考 [Material layout](https://m3.material.io/foundations/layout/layout-overview/adaptive-design)。
2. 再选择语义组件和状态，参考 [Components](https://m3.material.io/components) 与 [States](https://m3.material.io/foundations/interaction/states/overview)。
3. 然后通过 Token、颜色、字体、形状和 spacing 表达品牌，参考 [Customization](https://m3.material.io/foundations/customization)。
4. 最后添加有因果关系的动效，参考 [Material motion](https://m3.material.io/styles/motion/overview/how-it-works)。

## 无障碍与内容

### Accessibility by default

[Material accessibility principles](https://m3.material.io/foundations/overview/principles) 将可访问性作为设计起点：尊重个体差异、先理解用户与环境、共同设计，并把 WCAG 等最低要求视为起点而不是终点。

- 元素应具有明确角色、名称、状态和操作，辅助技术入口见 [Assistive technology](https://m3.material.io/foundations/overview/assistive-technology)。
- 结构、流程、交互元素和对比度分别检查，入口见 [Designing overview](https://m3.material.io/foundations/designing/overview) 与 [Color contrast](https://m3.material.io/foundations/designing/color-contrast)。
- 文字需要支持系统缩放，不应因固定容器被裁断；参考 [Text resizing](https://m3.material.io/foundations/writing/text-resizing) 与 [Text truncation](https://m3.material.io/foundations/writing/text-truncation)。
- 不用颜色、动效或位置作为唯一信号；状态至少提供另一个可感知线索，参考 [Applying states](https://m3.material.io/foundations/interaction/states/applying-states)。

### Content design

- 以任务结果命名操作，保持简洁、具体、可翻译；总入口见 [Content design](https://m3.material.io/foundations/content-design/overview)。
- 图片、图标和图表按信息价值决定替代文本；参考 [Alt text](https://m3.material.io/foundations/content-design/alt-text)。
- 通知只传递时间相关且有行动价值的信息；参考 [Notifications content](https://m3.material.io/foundations/content-design/notifications)。
- 国际化内容避免依赖固定字符数和英语语序；参考 [Global writing](https://m3.material.io/foundations/content-design/global-writing/overview)。

## Design Token 与定制

[Material design tokens](https://m3.material.io/foundations/design-tokens/overview) 分为三类：

| 层级 | 含义 | 使用方式 |
|---|---|---|
| Reference | 原始颜色、字体、尺寸等可选值 | 作为系统输入，不直接散落在组件代码 |
| System | `color.primary`、`shape.medium` 等语义角色 | 主题和跨组件一致性的主要接口 |
| Component | 某组件内部槽位映射 | 通常由系统角色派生，只有明确组件需求才覆盖 |

具体落地见 [How to use tokens](https://m3.material.io/foundations/design-tokens/how-to-use-tokens)。Token 应描述角色而不是当前外观，避免把 hex、阴影、圆角和时间硬编码到业务组件；主题上下文至少考虑 light/dark、contrast、密度、窗口和 RTL。

[Customization](https://m3.material.io/foundations/customization) 的推荐组合是：

- 自定义主题承载品牌。
- Android 可使用动态颜色响应用户系统个性化。
- 始终保留静态方案，确保不支持动态颜色或品牌需要稳定表达时仍可用。
- 通过语义色角色维持前景/容器配对，不只替换 `primary` 一个颜色。

## 输入与状态

### 多输入

[Material inputs](https://m3.material.io/foundations/interaction/inputs) 覆盖触控、鼠标、触控板、键盘和辅助输入。自适应界面不能只改变宽度，还要调整 hover、focus、快捷键、目标尺寸和信息密度。

[Gestures](https://m3.material.io/foundations/interaction/gestures) 适用于直接操控，但关键操作必须有可发现、可访问的替代入口。平台系统手势区域不能被应用手势无条件占用。

### States

[States overview](https://m3.material.io/foundations/interaction/states/overview) 包含 enabled、disabled、hovered、focused、pressed、dragged、selected 等状态。应用规则：

- 状态可组合，例如 selected + focused；不能假设永远互斥。
- 至少用两个可感知特征表达重要状态，例如颜色加图标、outline 或文本。
- 同类组件的状态层、光标、焦点和禁用处理应一致。
- state layer 是组件反馈的一部分，不应被品牌背景吞没；参考 [State layers](https://m3.material.io/foundations/interaction/states/state-layers)。
- 不要以降低 opacity 的方式让禁用内容完全不可读；按照对应组件的 [Accessibility](https://m3.material.io/components) 页面核对。

## 自适应布局

[Material adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design) 同时面向 mobile、desktop 和 spatial，并考虑 touch、pointer 与 keyboard。核心不是“整体缩放”，而是组件和区域在窗口变化时 show/hide、levitate、reflow 或更换呈现。

### Window size classes

当前 Material 3 [breakpoints](https://m3.material.io/foundations/layout/breakpoints/overview) 以窗口宽度而不是设备型号分类：

| 类别 | 宽度 | 常见结构 |
|---|---:|---|
| Compact | `< 600dp` | 单窗格、底部 navigation bar |
| Medium | `600–839dp` | 单窗格或扩展单窗格，视任务使用 rail |
| Expanded | `840–1199dp` | 双窗格、navigation rail/drawer |
| Large | `1200–1599dp` | 双窗格并增加留白或 supporting pane |
| Extra large | `>= 1600dp` | 最多三窗格，避免无限拉宽内容 |

断点是设计输入，不是设备清单。典型策略：compact/medium 一窗格，expanded/large 两窗格，extra large 在信息结构需要时三窗格。对应 [Canonical examples](https://m3.material.io/foundations/layout/canonical-examples/overview) 包括 feed、list-detail 和 supporting pane。

适配时逐项问：

- `reveal`：是否显示原本隐藏的导航、命令或辅助内容？
- `divide`：是否拆成多窗格？
- `resize`：组件是否达到合理最大宽度而非铺满？
- `reposition`：导航、FAB、工具栏是否换位？
- `swap`：navigation bar 是否应换成 rail/drawer，dialog 是否应换成 side sheet？

布局骨架见 [Scaffold](https://m3.material.io/foundations/layout/scaffold/overview)，网格与密度见 [Grids and spacing](https://m3.material.io/foundations/layout/grids-spacing/overview) 和 [Density](https://m3.material.io/foundations/layout/grids-spacing/density)。

本节只维护通用 Material 自适应布局和视觉策略。Android `FoldingFeature`、tabletop/book posture、canonical pane 实现、display modes、质量分级及 Apple Duo 对齐统一见 [android-foldable-adaptation.md](android-foldable-adaptation.md)。

## 颜色

[Material color system](https://m3.material.io/styles/color/system/overview) 用语义角色组织颜色，而不是按页面随意选色。当前体系包含 primary、secondary、tertiary、error、surface、outline 等角色族，并通过 `on-*` 前景与 `*-container` 容器配对保持层级和对比。

### 角色规则

- `primary` 承担最高优先级动作与强调，不能让所有可点击元素都同等突出。
- `secondary` 和 `tertiary` 用于区分层级、类别或补充表达，不是随机装饰色。
- `surface` 族构成大部分界面；elevation 可由 surface 色调层级表达，而非到处叠阴影。
- `on-*` 只用于对应背景角色；不要因为视觉接近交换前景配对。
- `outline` 与 `outlineVariant` 用于边界层级，不替代文本对比。

完整角色见 [Color roles](https://m3.material.io/styles/color/roles)。方案应覆盖 light/dark，并按产品需要提供 standard、medium 和 high contrast 级别。

### Dynamic color

Android 12/API 31 起可从壁纸或内容源生成动态方案；设计概念见 [Choosing a source](https://m3.material.io/styles/color/dynamic/choosing-a-source) 与 [User-generated source](https://m3.material.io/styles/color/dynamic/user-generated-source)。

- HCT 用 hue、chroma、tone 组织色彩和可访问性色调关系。
- 一个 source color 可生成 primary、secondary、tertiary、neutral 和 neutral variant tonal palettes。
- 动态颜色是用户个性化，不应破坏品牌识别、状态色或内容可读性。
- 必须提供 [Static baseline](https://m3.material.io/styles/color/static/baseline) 或自定义静态 fallback。
- Web、iOS 和 Windows 不应假装拥有 Android 壁纸动态颜色；可提供用户主题或品牌主题作为语义替代。

## 排版

[Material typography](https://m3.material.io/styles/typography/overview) 通过角色定义内容层级：display、headline、title、body、label。M3 Expressive 在 baseline 角色之外加入 emphasized 变体，当前完整体系可达 30 个样式角色。

- 组件选择语义角色，不按视觉大小直接挑字号。
- 字体、字号、行高、字重和 tracking 通过 Token 成组应用；参考 [Type scale tokens](https://m3.material.io/styles/typography/type-scale-tokens)。
- 可变字体可使用 weight、width、optical size 等轴，但必须测试语言覆盖与 fallback；参考 [Fonts](https://m3.material.io/styles/typography/fonts)。
- 正文优先可读性，展示性字体只用于适量、短文本；编辑内容见 [Editorial treatments](https://m3.material.io/styles/typography/editorial-treatments)。
- Android 使用 `sp` 并尊重系统字体缩放；不要固定行高或容器截断放大文本。

## Elevation

[Material elevation](https://m3.material.io/styles/elevation/overview) 表示表面之间的 z 轴关系，可由 tonal surface 或 shadow 表达。M3 更依赖颜色层级，不要求每个卡片都有阴影。

- elevation 必须有结构或交互意义，例如浮动、覆盖、拖拽、模态关系。
- 使用少量一致层级，优先组件默认值；避免业务页面自行发明连续阴影刻度。
- 不同平台对阴影渲染不同，跨平台保持层级语义而非复制 shadow 参数。
- 具体应用和 Token 见 [Applying elevation](https://m3.material.io/styles/elevation/applying-elevation) 与 [Elevation tokens](https://m3.material.io/styles/elevation/tokens)。

## Shape

[Material shape principles](https://m3.material.io/styles/shape/overview-principles) 将 shape 用于分组、强调、状态和表达。M3 Expressive 扩充了形状集合与 morph 能力，但形状本身不应成为唯一语义信号。

- 常见较大圆角参考：large `20dp`、extra large `32dp`、extra-extra large `48dp`；实际组件值以 [Corner radius scale](https://m3.material.io/styles/shape/corner-radius-scale) 和组件 specs 为准。
- 不要让所有容器都使用同一大圆角，也不要在密集工作流中以形状制造无效装饰。
- [Shape morph](https://m3.material.io/styles/shape/shape-morph) 可表达状态、进度或环境变化，但应保持因果和可读性，并提供 reduced motion 方案。

## Spacing

[Material spacing](https://m3.material.io/styles/spacing/overview) 基于可组合的间距刻度，基础节奏以 `8dp` 为主，`4dp` 用于更细的图标、文字和内部校准。

- 区分 padding、gap 和 margin；优先由父布局控制 padding/gap，避免子项各自堆 margin。
- 小屏常见外边距可从 `16dp` 起，但必须按组件 specs、窗口类别和内容密度调整。
- spacing 不能独立于触控目标、文字缩放和网格。
- 应用方法和完整值见 [Applying spacing](https://m3.material.io/styles/spacing/applying-spacing) 与 [Spacing tokens](https://m3.material.io/styles/spacing/tokens)。

## Icons

[Material icons](https://m3.material.io/styles/icons/overview) 推荐 Material Symbols。它支持 `FILL`、`wght`、`GRAD`、`opsz` 等轴，并提供 Outlined、Rounded 和 Sharp 风格。

- 一个产品区域内保持一致风格和光学尺寸。
- 选中状态可在 outlined/filled 间变化，但不能只靠 fill 表达关键状态。
- 图标按钮必须有可访问名称；生僻图标配文本或 tooltip。
- 自定义图标使用 24dp 基准画布、20dp live area、2dp padding 和官方 keyline；常规 stroke/weight 为 2dp/400。
- Compose 旧 `material-icons-*` 图标库不再是最新推荐；从 [Google Fonts Icons](https://fonts.google.com/icons) 下载 Android XML，再通过 `Icon` 使用。
- 平台迁移时换成目标平台图标资产；Material Symbols 不应覆盖 SF Symbols 或 Segoe Fluent Icons 的原生语义。
- 完整轴、网格、原生 API、RTL、工具和跨平台映射见 [../cross-platform/cross-platform-interface-icons.md](../cross-platform/cross-platform-interface-icons.md)。Launcher/Play App Icon 是另一条资产链，见 [../cross-platform/cross-platform-app-icons.md](../cross-platform/cross-platform-app-icons.md)。

## 跨平台边界

| 内容 | 适用性 | 处理方式 |
|---|---|---|
| 语义 Color/Type/Shape/Spacing Token | Universal / adapted | 可迁移角色模型，具体值和字体服从项目与平台；来源 [Design tokens](https://m3.material.io/foundations/design-tokens/overview) |
| Material 组件角色与状态 | Platform-adapted | Android 直接使用；Web/Flutter 可使用官方实现；Apple/Windows 换成语义等价原生组件；来源 [Components](https://m3.material.io/components) |
| Dynamic Color from wallpaper | Android-only | 非 Android 改为用户主题或品牌主题；来源 [Dynamic color](https://m3.material.io/styles/color/dynamic/user-generated-source) |
| Predictive Back、system bars、WindowInsets | Android-only | 不跨平台模拟；来源 [Predictive back](https://developer.android.google.cn/design/ui/mobile/guides/patterns/predictive-back) 与 [System bars](https://developer.android.google.cn/design/ui/mobile/guides/foundations/system-bars) |
| Adaptive window strategies | Universal / adapted | 可迁移 show/hide、reflow、swap，导航组件换成目标平台版本；来源 [Adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design) |
