# 自适应布局与平台能力

把窗口、输入方式和系统能力当作设计输入。先判定能力，再选择布局和交互；不要把设备品牌、型号或一个固定分辨率当作能力代理。

## Android 能力矩阵

| 能力 | 首选判断 | 设计决策 |
|---|---|---|
| 窗口宽度 | `WindowSizeClass`：Compact / Medium / Expanded | bottom navigation、navigation rail、persistent navigation drawer 的切换 |
| 窗口高度 | 可用窗口高度和 `WindowInsets` | 工具栏、键盘、底部操作区是否需要滚动或折叠 |
| 折叠/双屏 | Jetpack WindowManager posture | 避开 hinge，分栏或跨屏展示，不把铰链当普通空白 |
| 方向 | 当前窗口 orientation | 横屏使用更宽的信息布局，不能只放大竖屏布局 |
| 输入 | touch、mouse、keyboard、stylus | 触控目标、悬停、右键、快捷键和焦点路径分别验证 |
| 系统栏 | `WindowInsets` 与 edge-to-edge 状态 | 内容、手势区和 transient system bar 不互相遮挡 |
| 颜色/主题 | Dynamic Color、深色模式、对比度偏好 | Material 语义色重新计算，不硬编码品牌色覆盖可读性 |

## iOS 能力矩阵

| 能力 | 设计决策 |
|---|---|
| size class / 窗口尺寸 | iPad、多窗口和横屏时重新组织导航与列数 |
| safe area / 键盘 | 内容和浮动操作避开系统区域，键盘出现时保持主要操作可达 |
| Dynamic Type | 文本放大时允许换行、滚动和布局重排，不裁切标题或按钮 |
| Reduce Motion | 关闭非必要位移、缩放和视差，保留状态变化与焦点反馈 |
| 指针/触控/VoiceOver | 保留可见焦点、语义标签、触控目标和辅助技术顺序 |
| Liquid Glass 可用性 | 仅在原生系统组件或明确支持的自定义路径中启用，其他情况退化到语义材质 |

## 能力抽象示例

```text
PlatformCapabilities
  windowClass: compact | medium | expanded
  input: touch | pointer | keyboard | stylus
  supportsDynamicColor: bool
  supportsLiquidGlass: bool
  supportsPredictiveBack: bool
  reduceMotion: bool
  highContrast: bool
```

能力对象只决定可用行为和 fallback，不应该携带品牌名。平台实现可以将它映射到 SwiftUI Environment、UIKit trait collection、Compose WindowSizeClass 或 AndroidX WindowManager。

## 语义效果映射

| 共享语义 | iOS 26+ | Android |
|---|---|---|
| `glass` | 系统 Liquid Glass 或 HIG 允许的自定义 glass effect | Material surface + 适量 tonal/elevation；不支持时不透明 surface |
| `elevated` | 系统层级、材质或阴影 | `surfaceContainer` / elevation / tonal elevation |
| `flat` | 内容层标准背景和分隔 | Material surface/container，不额外添加玻璃 |
| `primaryAction` | 系统 Button / 平台主操作样式 | Material 3 Button / FilledTonalButton 等按语义选择 |
| `navigation` | Tab bar、sidebar、toolbar 等平台导航 | NavigationBar、NavigationRail、NavigationDrawer 按窗口选择 |

映射允许外观不同，但必须保持状态名称、禁用规则、选择反馈、错误语义和可达性一致。

## 官方入口

- [Material 3 Adaptive](https://developer.android.com/develop/ui/compose/layouts/adaptive)
- [Window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes)
- [Support different screen sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-screen-sizes)
- [Jetpack WindowManager](https://developer.android.com/jetpack/androidx/releases/window)
- [Apple Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Apple Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Apple Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
