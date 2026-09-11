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

## 测试矩阵

至少覆盖下列组合，不要求穷举全部 OEM：

- Android 最新稳定版与一个仍在支持的旧版本。
- Pixel、Samsung、Xiaomi，以及一台 OPPO 或 vivo 设备；发现问题后记录能力和系统版本，而不是只记录品牌。
- Compact、Medium、Expanded 窗口；竖屏、横屏、分屏和折叠姿态（项目支持时）。
- 触控、键盘/鼠标、手写笔（项目支持时）；系统手势返回与三键导航（Android）。
- 浅色、深色、Dynamic Color、高对比度、超大字体、RTL 和系统字号变化。
- 弱网、后台恢复、进程重建、键盘出现/消失、系统栏变化和旋转。

## 两类验收

### 行为一致性

- 相同入口能完成相同任务，成功、失败、取消和禁用状态语义一致。
- 返回、深链、键盘、焦点、读屏顺序和状态恢复符合各平台规则。
- 新 API 不可用时 fallback 仍可完成核心任务，不把 unsupported 当成空白或死路。

### 视觉容差

- 允许导航结构、控件形状、字体渲染、阴影、材质和系统动画不同。
- 必须一致的是信息优先级、文案含义、状态区分、触控目标、对比度和关键操作位置的可发现性。
- 对截图比较先固定窗口和字体设置；不要用单一 iOS 截图作为 Android 的像素基准。

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

- [Android adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive)
- [Android accessibility](https://developer.android.com/guide/topics/ui/accessibility)
- [Material accessibility](https://m3.material.io/foundations/accessible-design/overview)
- [Android testing](https://developer.android.com/training/testing)
- [Apple accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Apple testing and Xcode](https://developer.apple.com/documentation/xcode)
