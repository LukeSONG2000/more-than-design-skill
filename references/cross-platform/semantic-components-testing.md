# 语义组件与跨平台测试矩阵

共享语义，分别实现组件。测试重点是用户任务、状态和可达性是否一致，而不是两个平台是否像素相同。

## 语义组件表

| 语义 | iOS | Android | 共享验收 |
|---|---|---|---|
| `PrimaryActionButton` | SwiftUI `Button` 或 UIKit 标准按钮 | Material 3 Button | 标签、启用状态、提交结果、焦点和反馈 |
| `DestructiveActionButton` | 系统 destructive role / confirmation | Material error/confirmation pattern | 二次确认、错误色不作为唯一信号 |
| `EmptyState` | SwiftUI 内容与可访问语义 | Compose 内容与 Material typography | 解释原因、下一步操作、读屏顺序 |
| `LoadingState` | ProgressView/系统状态 | Circular/LinearProgressIndicator | 不丢失上下文、可取消时提供取消 |
| `Navigation` | Tab bar/sidebar/navigation stack | NavigationBar/Rail/Drawer/NavHost | 路由结果、返回、恢复和深链一致 |
| `Glass` | 系统组件或受控 Liquid Glass | Material surface/elevation fallback | 层级、对比度、点击区域和状态一致 |
| `InterfaceIcon` | SF Symbols | Material Symbols | 共享语义/标签/状态，字形、weight、fill 和动效服从平台；Windows 使用 Segoe Fluent Icons，详见 [cross-platform-interface-icons](cross-platform-interface-icons.md) |
| `AppIcon` | Icon Composer/Xcode | Adaptive Icon + Play listing | 共享品牌识别，遮罩、图层、商店资产和最终系统表面分别验收；Windows 见 [cross-platform-app-icons](cross-platform-app-icons.md) |
| `OngoingActivity` | ActivityKit/WidgetKit Live Activity | 按能力选择持续/进度通知或 App 内状态 | 活动身份、进度、时效、必要动作和详情路由一致；系统呈现与结束摘要见 [apple-live-activities](../apple/apple-live-activities.md) |

## 测试矩阵

至少覆盖下列组合，不要求穷举全部 OEM：

- Android 最新稳定版与一个仍在支持的旧版本。
- 依据真实用户选择少量代表性 OEM/真机；问题记录必须包含设备、API、窗口、能力和库版本，不能只记录品牌。
- Compact、Medium、Expanded；面向桌面/超大屏时增加 Large、Extra large。覆盖竖屏、横屏、分屏和折叠姿态。
- 触控、键盘/鼠标、手写笔（项目支持时）；系统手势返回与三键导航（Android）。
- 浅色、深色、Dynamic Color、高对比度、超大字体、RTL 和系统字号变化。
- 弱网、后台恢复、进程重建、键盘出现/消失、系统栏变化和旋转。

Android 折叠屏项目默认以 Tier 2 Adaptive optimized 为交付基线；只有产品确实利用 posture、相机、拖放或多显示时才要求 Tier 1。额外覆盖 outer/inner、tabletop/book、单柔性屏/双屏/多铰链、FoldingFeature 的 occlusion/separation 组合、pane/navigation 切换、配置重建和 display-mode fallback，详见 [../android/android-foldable-adaptation.md](../android/android-foldable-adaptation.md)。

iPhone Duo 项目额外覆盖：外屏/内屏、闭合/展开/书本式/桌面式姿态、Split View、摄像头与折叠 reserved regions、四边不对称 safe area、横向/竖向系统栏、RTL、overflow/compression，以及 iOS 27.1 API 不可用时的普通 iPhone fallback。完整矩阵见 [../apple/iphone-duo-adaptation.md](../apple/iphone-duo-adaptation.md)。

## 两类验收

### 行为一致性

- 相同入口能完成相同任务，成功、失败、取消和禁用状态语义一致。
- 返回、深链、键盘、焦点、读屏顺序和状态恢复符合各平台规则。
- 新 API 不可用时 fallback 仍可完成核心任务，不把 unsupported 当成空白或死路。

### 视觉容差

- 允许导航结构、控件形状、字体渲染、阴影、材质和系统动画不同。
- 必须一致的是信息优先级、文案含义、状态区分、触控目标、对比度和关键操作位置的可发现性。
- 对截图比较先固定窗口和字体设置；不要用单一 iOS 截图作为 Android 的像素基准。
- 图标比较关注语义、视觉重量、baseline、RTL 和可访问名称，不要求 SF/Material/Segoe 轮廓相同。
- App Icon 必须区分源资产、生成产物、配置引用、最终包和实机表面；仓库存在文件或构建通过不能替代最终槽位验收。
- 持续活动区分普通更新与关键 alert、stale 与完成、结束与移除；Apple 锁屏/岛/配对设备的实际行为及其尺寸、背景、动画约束见 [../apple/apple-live-activities.md](../apple/apple-live-activities.md)。

## 交付记录模板

```text
平台/版本/设备：
窗口与输入：
共享语义：
平台原生实现：
能力判断与 fallback：
行为验收：通过 / 未通过
视觉容差说明：
无障碍验收：
已知平台差异：
```

## 官方入口

- [Android Adaptive Apps](https://developer.android.com/develop/adaptive-apps)
- [Adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)
- [Android accessibility](https://developer.android.com/guide/topics/ui/accessibility)
- [Material accessibility](https://m3.material.io/foundations/accessible-design/overview)
- [Android testing](https://developer.android.com/training/testing)
- [Apple accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Apple testing and Xcode](https://developer.apple.com/documentation/xcode)
- [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)
- [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/)
