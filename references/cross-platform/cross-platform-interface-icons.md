# 跨平台界面图标与原生 Symbol

本文件处理应用界面中的操作、导航、状态和类别图标。它不处理代表应用本身的 App Icon；App Icon 见 [cross-platform-app-icons.md](cross-platform-app-icons.md)。

## 1. 核心原则

- 先定义语义，再由每个平台解析为自己的原生图标。共享 `action.search`、`navigation.back` 之类的语义，不共享某个平台的字形名称或字体代码点。
- Apple 使用 SF Symbols，Android/Material 使用 Material Symbols，Windows 使用 Segoe Fluent Icons 或 WinUI 图标类型。不要把一套平台字体打包到另一平台。
- 优先平台库已有图标；只有库中没有准确语义时才设计自定义图标。
- 图标样式属于视觉层；图标切换、Symbol Effect、AnimatedIcon 和轴动画属于动效层，分别设计和验收。
- 不熟悉、不可唯一理解或高风险操作不能只显示图标；增加文字、tooltip、确认或上下文说明。
- 图标按钮必须有可访问名称；装饰图标从辅助技术中隐藏。

## 2. 共享语义合同

业务代码和设计稿可以维护平台无关的语义名，再在各端分别解析：

| 语义组 | 示例 token | 必须保持一致 | 允许平台不同 |
|---|---|---|---|
| 导航 | `navigation.back`, `navigation.forward`, `navigation.up` | 去向、可用状态、RTL 结果 | 箭头造型、线宽、动画 |
| 基本操作 | `action.add`, `action.close`, `action.search`, `action.refresh` | 动作含义、标签、禁用逻辑 | 字形、光学尺寸、按压反馈 |
| 内容操作 | `action.share`, `action.delete`, `action.download`, `action.favorite` | 成功/失败/破坏性语义 | outline/fill、颜色角色 |
| 更多与菜单 | `overflow.more`, `menu.open` | 打开的命令集合 | 水平/垂直省略号、菜单呈现 |
| 状态 | `status.success`, `status.warning`, `status.error`, `status.syncing` | 状态和可访问文案 | 图标、颜色、是否动画 |
| 选择 | `state.selected`, `state.unselected` | 选择结果和读屏状态 | fill 变体、FILL 轴、系统选择器 |

不要建立 `sf.trash`、`material.delete` 或 Unicode 代码点这样的共享 token。平台资源名称会变化，且授权、可用版本和 RTL 行为不同。

## 3. Apple: SF Symbols

[SF Symbols HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) 是 Apple 界面图标的首选来源。SF Symbols 与 San Francisco 字体对齐，适合工具栏、标签栏、菜单、正文和系统控件。

### 3.1 选择和视觉规则

- 先在 SF Symbols App 中搜索语义，并检查符号、变体和目标系统版本的 availability。
- 九档 weight 应与相邻文字的字重匹配；small、medium、large scale 用于调整相对强调，不用任意缩放破坏光学关系。
- outline 通常适合工具栏、列表和图文并排；fill 常用于选中态、标签栏或需要更强强调的位置。优先让系统控件选择变体。
- slash 表示不可用或关闭状态；circle/square 等 enclosed 变体可改善小尺寸辨识度，但不能只为装饰混用。
- Monochrome、Hierarchical、Palette、Multicolor 四种 rendering mode 按信息层级选择；使用系统颜色以适配深色、vibrancy 和高对比度。
- Variable Color 表示强度、容量或进度变化，不用于伪造深度；层级深度使用 Hierarchical。
- Symbol Effects 只用于操作反馈、状态变化或持续活动。遵守 Reduce Motion，不用循环动画吸引无关注意力。
- 方向性和文字相关符号优先使用系统自动本地化版本，不手工镜像所有图标。

### 3.2 原生 API

| 技术栈 | 系统 Symbol | 自定义 Symbol | 配置重点 |
|---|---|---|---|
| SwiftUI | `Image(systemName:)` | `Image(_:)` + Symbol Image Set | `font`, `imageScale`, `symbolVariant`, `symbolRenderingMode`, `symbolEffect` |
| UIKit | `UIImage(systemName:)` | `UIImage(named:)` | `UIImage.SymbolConfiguration`, text style、weight、scale、palette |
| AppKit | `NSImage(systemSymbolName:accessibilityDescription:)` | `NSImage(named:)` | `NSImage.SymbolConfiguration` 与 baseline |

- 图标与文字并排时按文字 baseline 对齐；不要只靠外接矩形视觉居中。
- 新符号或新特性需要 availability 判断；旧系统提供语义等价的旧符号或自有 fallback asset。
- 自定义 Symbol 使用 SF Symbols 导出的模板和 Symbol Image Set；保持可插值路径、渲染层级与辅助功能信息。

### 3.3 工具与授权

- [SF Symbols App](https://developer.apple.com/sf-symbols/)：搜索、availability、变体、渲染、动画和自定义 Symbol 标注。
- [Apple Design Resources](https://developer.apple.com/design/resources/)：官方模板和设计资源。
- SF Symbols 含受保护的 Apple 产品/功能符号。遵守使用条款，不将 SF Symbol 或近似图形用于 App Icon、Logo、商标，也不作为通用 Web/Android/Windows 字体分发。

## 4. Android/Material: Material Symbols

[Material Symbols](https://fonts.google.com/icons) 是当前 Material 图标来源。旧 Compose `material-icons-core` / `material-icons-extended` 图标集不再维护为最新视觉，新的 Android 实现优先从 Google Fonts 图标库下载 Android XML。

### 4.1 样式和变量轴

- 三种家族为 Outlined、Rounded、Sharp。同一产品面保持一个主家族，不按页面随机混用。
- `FILL` 在 0 和 1 之间表达未填充/填充状态，可用于选择或状态过渡。
- `wght` 为 100-700，默认 regular 400；保持同一操作面的视觉重量一致。
- `GRAD` 细调强调且比 weight 更少改变图标尺寸，可降低暗色界面眩光或增强强调。
- `opsz` 为 20-48dp，随实际显示尺寸进行光学修正，不用单一轮廓机械缩放覆盖全部尺寸。

### 4.2 自定义 Material 图标

- 基准画布为 24dp，常规 live area 为 20x20dp，外围各 2dp padding。
- 官方额外光学尺寸为 20、40、48dp；20dp 适合桌面或高密度布局。
- keyline 参考：18dp 方形、20dp 圆形、16x20dp 竖矩形、20x16dp 横矩形。
- 默认外角半径 2dp；Outlined 内角保持方形。常规 stroke/weight 为 2dp/400。
- 图形应简洁、清晰、正面呈现；不要过度写实、倾斜或制造三维透视。复杂图形只做必要的 optical correction。

### 4.3 Android 实现

| 场景 | 推荐实现 |
|---|---|
| Jetpack Compose | 从 Google Fonts 下载最新 Android XML，作为 VectorDrawable，通过 `Icon(painterResource(...), contentDescription=...)` 使用 |
| Android Views | VectorDrawable + `ImageView`、`MaterialButton` 的 icon 属性或对应 Material 组件 |
| Web | Material Symbols 可变字体或按需 SVG；字体请求只包含使用的名称和轴，避免加载完整字库 |
| 设计稿 | Material Symbols Figma plugin；自定义图标使用官方 24dp keyline template |

- Compose `Icon` 默认使用 `LocalContentColor` 且默认为 24dp，适合单色小图标；需要保留原始多色内容时使用 `Image`。
- 方向性图标使用 RTL-aware 资源或 auto-mirrored VectorDrawable；不要镜像播放、媒体、商标和本身无方向语义的符号。
- Material Symbols 采用 Apache 2.0；仍需保留许可并避免把 Google 品牌图标当作自有品牌资产。

### 4.4 工具

- [Google Fonts Icons](https://fonts.google.com/icons)：搜索、FILL、weight、grade、optical size，下载 SVG/PNG/Android XML。
- [Material Symbols Figma plugin](https://www.figma.com/community/plugin/1088610476491668236/material-symbols)：设计稿使用。
- [Material icon keyline template](https://storage.googleapis.com/material-io-design/downloads/gm_icon_template.ai.zip)：自定义图标网格。
- [Material Symbols developer guide](https://developers.google.com/fonts/docs/material_symbols)：Web 字体、自托管、子集和轴配置。

## 5. Windows: Segoe Fluent Icons 与 WinUI

Windows 11 原生应用优先 [Segoe Fluent Icons](https://learn.microsoft.com/windows/apps/design/iconography/segoe-fluent-icons-font) 和 WinUI 图标类型。Segoe Fluent Icons 是约 1 epx 的 monoline 系统图标字体，目标是 minimal、harmonious、evolved。

### 5.1 类型选择

| 需求 | WinUI 类型 | 规则 |
|---|---|---|
| 常见系统语义 | `SymbolIcon` / `SymbolIconSource` | 优先 `Symbol` 枚举，减少代码点依赖 |
| 字体中其他 glyph | `FontIcon` / `FontIconSource` | 使用 `SymbolThemeFontFamily`；不要把 PUA 代码点当跨平台协议 |
| 可复用资源 | `IconSource` + `IconSourceElement` | `IconSource` 可放入资源字典并在多处使用 |
| 自定义矢量 | `PathIcon` / `PathIconSource` | 只在系统字体无合适语义时使用 |
| 有意义的状态动效 | `AnimatedIcon` | 提供 fallback icon；动画必须对应状态或入口反馈 |
| 原色 SVG/图像 | `ImageIcon` | 不响应 Foreground 状态色，按钮状态需额外验证 |
| 位图 | `BitmapIcon` | 最后选择；缩放易模糊，默认会单色化非透明像素 |

- 推荐的清晰字号为 16、20、24、32、40、48、64；在真实 DPI/缩放下检查，不用任意字号假设仍会 pixel-crisp。
- Windows 10 旧版本可能回退到 Segoe MDL2 Assets；使用主题资源比硬编码字体名更稳妥。
- 方向图标使用官方 mirrored form 或布局方向处理；不要镜像不具方向性的图形。
- Segoe Fluent Icons 可用于设计和开发，但不能把该字体作为资产发布到其他平台。

### 5.2 工具

- [WinUI 3 Gallery](https://github.com/microsoft/WinUI-Gallery)：查看、搜索、复制图标和验证控件中的实际表现。
- [Windows icons API overview](https://learn.microsoft.com/windows/apps/develop/ui/controls/icons)：`IconElement` / `IconSource` 类型和控件接入。
- [AnimatedIcon](https://learn.microsoft.com/windows/apps/develop/ui/controls/animated-icon)：状态动画与 fallback。

## 6. 跨平台对齐方式

同一功能可以共享语义、标签和状态机，但每个平台分别选择字形：

| 决策 | Apple | Android/Material | Windows |
|---|---|---|---|
| 默认库 | SF Symbols | Material Symbols | Segoe Fluent Icons / WinUI |
| 默认状态图标 | outline；系统控件可自动选 fill | `FILL=0`，选中可用 `FILL=1` | 使用平台 glyph 与控件 selected state，不强行模拟 FILL 轴 |
| 字重对齐 | 匹配 SF 文字 weight | `wght` 与排版层级协调 | 使用系统 monoline 和推荐字号 |
| 小尺寸优化 | symbol scale 与系统配置 | `opsz` + 20/24dp 光学版本 | 16/20/24 等推荐字号 |
| 多层颜色 | Hierarchical/Palette/Multicolor | tint、FILL/grade 或自定义矢量 | Foreground、glyph layering、ImageIcon |
| 动效 | Symbol Effects | 状态轴或 Compose 动画 | AnimatedIcon |
| RTL | 系统本地化符号 | auto-mirrored/vector autoMirrored | mirrored glyph / flow direction |

禁止为了“品牌统一”让所有端使用同一个平台图标字体。正确的一致性是相同操作得到相同结果，而不是相同轮廓。

## 7. 无障碍与验收

- 图标按钮的 accessible name 描述动作，例如“删除文件”，不要描述形状“垃圾桶”。
- 相邻可见文字已完整表达含义时，避免读屏重复朗读装饰图标。
- 禁用、选中、错误、警告不能只靠 fill 或颜色；同时暴露语义状态。
- 测试浅色、深色、高对比度、动态字体、200% Windows 缩放、Android font/display scale 和 Apple Dynamic Type。
- 测试 RTL；确认只有方向性图标被镜像。
- 测试最低支持系统，确认新符号不存在时 fallback 不为空白方框。
- 截图对比只检查语义、光学重量和对齐，不要求三端像素相同。

## 8. 官方来源

- Apple [SF Symbols HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- Apple [SF Symbols App](https://developer.apple.com/sf-symbols/)
- Apple [Configuring and displaying symbol images](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui)
- Apple [Creating custom symbol images](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app)
- Material [Icons overview](https://m3.material.io/styles/icons/overview)
- Material [Designing icons](https://m3.material.io/styles/icons/designing-icons)
- Google [Material Symbols catalog](https://fonts.google.com/icons)
- Google [Material Symbols developer guide](https://developers.google.com/fonts/docs/material_symbols)
- Android [Icons in Compose](https://developer.android.com/develop/ui/compose/graphics/images/material)
- Microsoft [Icons in Windows apps](https://learn.microsoft.com/windows/apps/develop/ui/controls/icons)
- Microsoft [Segoe Fluent Icons](https://learn.microsoft.com/windows/apps/design/iconography/segoe-fluent-icons-font)

