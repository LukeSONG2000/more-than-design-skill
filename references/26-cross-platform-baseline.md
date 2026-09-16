# 跨平台基线：iOS 26+ 与 Android OEM

本文件处理同一产品同时面向 iOS 26+ 与 Android 多厂商设备时的架构和设计决策。它是平台能力参考，不是把 SwiftUI 逐项翻译成 Android UI 的规则。

## 总体原则

- 追求体验等价，不追求像素级一致。相同任务、信息层级、状态和结果应可理解；布局、导航、返回手势和系统组件按平台习惯实现。
- 共享产品语义与设计令牌，平台分别原生实现。共享状态、事件、文案、图标语义、颜色/间距/字体令牌、网络与数据层；不要强行共享 View 或 Composable 的实现。
- Liquid Glass 是 iOS 平台能力，不是跨平台基础材质。跨平台层只抽象 `glass`、`elevated`、`flat` 等语义效果；Android 映射到 Material surface、elevation 和 dynamic color，缺少模糊能力时使用不透明 surface fallback。
- 组件命名表达任务语义，例如 `PrimaryActionButton`、`DestructiveActionButton`、`EmptyState`、`LoadingState`；iOS 映射 SwiftUI/UIKit，Android 映射 Jetpack Compose/Material 3。

## 推荐分层

```text
shared/
  domain/             # 业务模型、用例、状态机
  data/               # 网络、缓存、持久化
  design-tokens/      # 语义色、字号、间距、shape、状态
  navigation-model/   # 路由意图和参数，不包含平台导航实现
  localization/       # 文案、格式化和 RTL 资源
iosApp/
  SwiftUI/Components/ Screens/ Navigation/
  PlatformEffects/    # Liquid Glass、系统材质、手势和安全区
androidApp/
  Compose/Components/ Screens/ Navigation/
  PlatformEffects/    # Material 3、动态颜色、WindowInsets、返回行为
```

共享层输出状态和事件；平台层决定控件、布局、导航、材质和输入行为。小型项目可以使用独立共享业务模块，不必为了形式引入完整 Kotlin Multiplatform。

## 平台基线

### iOS 26+

- SwiftUI 为首选 UI 实现，优先标准控件、系统导航、系统手势和 Dynamic Type。
- Tab bar、菜单、工具栏、标准按钮等优先交给系统实现；Liquid Glass 的系统外观和形变不要用自定义弹簧参数模拟。
- 自定义玻璃只在确有需要时使用，并遵守 HIG 的功能层与内容层边界；提供旧系统或非 Apple 平台 fallback。
- 将 `safeArea`、size class、键盘、指针、VoiceOver、Reduce Motion 和高对比度作为能力输入，而不是固定设备型号判断。

### iPhone Duo / iOS 27.1

- iOS 26+ 仍是通用 Apple UI 与 Liquid Glass 基线；Duo 的 Reserved Region、Arrangement View、竖向系统栏、Hinge、scene accessory 和双前摄能力按 iOS 27.1 SDK 单独判断。
- 共享层只表达 `foldAvoidance`、`dualPane`、`secondaryDisplay` 等任务语义。Apple 层按 [29-iphone-duo-adaptation.md](29-iphone-duo-adaptation.md) 实现，Android 层使用 Material Adaptive 与 Jetpack WindowManager。
- Duo 布局使用当前窗口的 size class、safe area 和 reserved regions，不按设备名称或 orientation 分支；新 API 不可用时退回普通可调整尺寸 iPhone 布局。

### Android 多 OEM

- Jetpack Compose + Material 3/Material 3 Adaptive 为首选；传统 Views 只在现有代码或平台 API 需要时使用。
- `compileSdk`/`targetSdk` 跟随最新稳定版本；`minSdk` 依据真实覆盖率决定。新 API 先做 capability check，再进入 fallback。
- 使用 AndroidX、WindowManager/Adaptive 布局、WindowInsets、系统返回和动态颜色；不要按 Samsung、Xiaomi、OPPO、vivo 等品牌写分支。
- 不把 Android 复制成 iOS：Material 的 top app bar、navigation bar/rail、FAB、list 和 surface 层级应按 Android 语义选择。
- 折叠屏先按当前 window size class 建立可调整尺寸基线，再用 `FoldingFeature` 与 posture 做针对性增强；详细规则和 Apple Duo 语义对齐见 [30-android-foldable-adaptation.md](30-android-foldable-adaptation.md)。

## 不推荐的路线

- 不把 Liquid Glass、SF Symbols、Dynamic Island、UIKit 菜单或 SwiftUI 视图当成 Android/Web 的共同基础。
- 不用“SwiftUI 翻译成 Android UI”的第三方方案作为核心架构，除非项目很小且已接受生态、调试和长期维护风险。
- 不用品牌判断代替能力判断；OEM 差异应通过 AndroidX、WindowSizeClass、系统能力和集中式 fallback 处理。

## 交付检查

设计说明应分别写清：共享语义、iOS 原生映射、Android 原生映射、无法等价的差异、fallback 和验证范围。若一个值只对 iOS Liquid Glass、Android dynamic color 或某个系统 API 有意义，应留在对应平台层。

## 官方入口

- [Apple Design](https://developer.apple.com/cn/design/)
- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- [Android Mobile Design](https://developer.android.google.cn/design/ui/mobile)
- [Material 3](https://m3.material.io/)
- [Jetpack Compose Material 3](https://m3.material.io/develop/android/jetpack-compose)
- [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)
- [Window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes)
- [AndroidX WindowManager](https://developer.android.com/jetpack/androidx/releases/window)
- [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)
