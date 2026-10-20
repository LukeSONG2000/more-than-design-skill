# Apple Live Activities: 设计、生命周期与平台适配

核对日期：2026-10-12。主来源为 [HIG 实时活动](https://developer.apple.com/cn/design/human-interface-guidelines/live-activities/)及其链接的 ActivityKit/WidgetKit 文档。本文件提炼实现决策，不保存官方展示图。尺寸是当前文档的设计参考，实际呈现、可用 API 和设备联动要按目标 SDK、系统与设备核对。

## 目录与调用地图

| 任务 | 读取位置 | 官方入口 |
|---|---|---|
| 判断是否需要实时活动 | 适用场景与信息合同 | [HIG Best practices](https://developer.apple.com/cn/design/human-interface-guidelines/live-activities/#Best-practices) |
| 锁屏、Dynamic Island 布局 | 展示区、视觉样式、尺寸参考 | [HIG Presentation](https://developer.apple.com/cn/design/human-interface-guidelines/live-activities/#Presentation) |
| Apple Watch、CarPlay、Mac、StandBy | 设备联动与补充布局 | [Creating custom views](https://developer.apple.com/documentation/activitykit/creating-custom-views-for-live-activities) |
| 启动、更新、过期与结束 | 生命周期与数据更新 | [Displaying live data](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) |
| APNs 更新与远程启动 | 服务端更新约束 | [ActivityKit push notifications](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications) |
| 点按、暂停/继续、深链 | 交互与无障碍 | [Adding interactivity](https://developer.apple.com/documentation/widgetkit/adding-interactivity-to-widgets-and-live-activities)、[Launching your app](https://developer.apple.com/documentation/activitykit/launching-your-app-from-a-live-activity) |
| 内容变化和减少动态 | 动效 | [Animating data updates](https://developer.apple.com/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities) |
| Android、Windows、Web 对应设计 | 跨平台语义与实现边界 | [平台路由](../cross-platform/platform-routing.md)、[语义组件测试](../cross-platform/semantic-components-testing.md) |

## 1. 适用场景与信息合同

Live Activity 适用于有明确起止、需要在数小时内持续跟踪的任务或事件，例如订单配送、比赛、出行、计时或训练。只展示能让人快速判断当前情况的信息；详情留在对应 App 页面。广告、推广、无期限信息流和无关更新不属于这种体验。

设计时先确定以下信息，之后再压缩为不同展示区：

| 信息 | 决策 |
|---|---|
| 活动身份 | 稳定的订单/赛事/任务 ID 与简短名称，让用户知道正在跟踪什么 |
| 当前状态 | 准备、进行、暂停、完成或失败；用文本/符号表达，不能仅靠颜色 |
| 关键变化量 | ETA、剩余时间、比分或进度，选择最有用的一项 |
| 时效 | 上次更新与过期判定；过期后表达“信息待更新”，不能继续暗示实时 |
| 直接操作 | 与活动有关的必要动作，HIG 优先建议一个交互元素，而非工具栏 |
| 详情目的地 | 活动对应的页面，包含活动 ID，避免让用户重新查找 |
| 结束摘要 | 最终结果与需要保留多久；结束活动和移除摘要是不同动作 |

以上字段是跨平台工程整理建议，不是 Apple 指定的数据模型。平台实现见第 9 节。

## 2. 展示区与系统行为

Apple 要求提供 Compact、Minimal、Expanded 和 Lock Screen 四种呈现。系统决定何时显示哪种组合，App 不能承诺始终占据 Dynamic Island 或自行选择全局优先级。

| 展示区 | 系统行为 | 布局决策 |
|---|---|---|
| Compact | 单个活动时，leading/trailing 分列摄像头两侧 | 两侧组成同一条信息；颜色和排版一致，宽度平衡；缩短单位和精度，避免额外摄像头侧 padding；两侧深链指向同一页面 |
| Minimal | 多活动时，系统可显示两个极简视图，一个连接岛、一个分离 | 用极少空间保留识别和动态状态；能显示剩余时间/进度时，优于只有静态 Logo |
| Expanded | 长按 compact/minimal 展开；关键 alert 更新也可触发 | 保留各项相对位置，使用 leading/trailing/center/bottom 区域；围绕摄像头合理绕排；必要时用 priority 或 `belowIfTooWide` |
| Lock Screen | 锁屏横幅；无 Dynamic Island 的设备在 alert 更新时可短暂显示为系统横幅 | 与 expanded 保持信息关系，设计专用任务布局；不要直接复制通知样式 |

对 Dynamic Island 外壳的扩展、收缩、呈现仲裁和系统尺寸使用原生 ActivityConfiguration/DynamicIsland。不能将 Web 胶囊动画的时长或弹簧视为原生参数。

## 3. 视觉样式与布局

### 排版、标识与边距

- 重要文字优先中等或更粗字重及易读字号，减少小号细节；处理长名称、本地化、RTL 和动态字体。
- 保持 App 的视觉识别；需要标志时使用不带额外容器的 Logo mark，不能放完整 App Icon。图标分别查 [SF Symbols](../cross-platform/cross-platform-interface-icons.md)与 [App Icon](../cross-platform/cross-platform-app-icons.md)。
- 圆角内元素保持同心边距，内圆角随容器和间距协调，可参考 `ContainerRelativeShape`。内容分组使用内嵌形状或明显分隔线，不画到岛的外缘。
- Lock Screen 标准布局边距为 **14pt**。图形或按钮可按内容适当收紧，仍要保持安全和清晰。
- 随内容量改变锁屏/expanded 的高度；信息少时不要用固定大面板，信息增多时再扩展。

### 颜色与材质

- Dynamic Island 的 compact、minimal、expanded 使用系统黑色不透明背景，**不能自定义背景色**。以文字、符号和对象的颜色表达品牌，检查黑底对比。
- `keylineTint(_:)` 控制深色环境下岛的细边线颜色，不是玻璃 tint 或背景填色。
- Lock Screen 可以用 `activityBackgroundTint(_:)` 设置背景；谨慎处理色彩和不透明度，检查浅/深色、复杂壁纸和 Always-On。
- 检查系统生成的关闭按钮颜色；需要时用 `activitySystemActionForegroundColor(_:)` 调整。
- 降低亮度时通过 `isLuminanceReduced` 适配颜色与资产。不能仅在正常亮度截图上验收。
- 不把应用内 Liquid Glass 控件参数直接套到 Live Activity。此处遵循 ActivityKit/WidgetKit 的系统呈现约束。

### 隐私

锁屏、Always-On 和其他设备上的内容可能被旁人看到。敏感内容使用无害摘要、隐私标记/遮蔽和用户可配置显示策略；详情在 App 中查看。相关视图 redaction 机制查 [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension)，不要把仅有深链等同于隐私保护。

## 4. 设备联动与补充布局

实时活动从 iPhone/iPad 发起，系统可延伸到以下位置。设备联动受配对、系统支持与用户配置影响，并非另建一个原生 macOS ActivityKit 活动。

| 位置 | 默认呈现与适配 | 交互限制 |
|---|---|---|
| iPhone/iPad | Lock Screen；支持设备的 Dynamic Island；alert 横幅 | 四种基础呈现都需要提供；无岛设备仍要可用 |
| iPhone StandBy | minimal 点按后进入放大约 2 倍的锁屏布局；自定义背景可延伸全屏 | 保持标准边距，避免边缘裁切；检查放大资产和夜间红色 tint |
| 配对 Mac 菜单栏 | 复用 compact/minimal/expanded，不另改其几何 | 点按通过 iPhone Mirroring 打开 iPhone App；不能当成 Mac 原生 App 的入口 |
| 配对 Apple Watch Smart Stack | 默认组合 compact leading/trailing；可提供专门的小尺寸布局 | Watch App 的打开方式需配置；未提供 Watch App 时可显示打开 iPhone App 的入口 |
| CarPlay Dashboard | 默认组合 compact leading/trailing，或使用 small 布局 | Live Activity 的按钮/toggle 被系统禁用；点按只有 App 支持 CarPlay 时才能打开对应 App |

`ActivityFamily` 与 `@Environment(\.activityFamily)` 可区分 `.small`/`.medium`。通过 `supplementalActivityFamilies([.small, .medium])` 声明支持的补充布局，并按部署目标判断 API 可用性：

- `.small`：为 Apple Watch/CarPlay 提供更适合的小布局；不能仅按屏幕宽度识别运行平台。
- `.medium`：锁屏等常规呈现，包括按环境优化 StandBy 的布局。
- Apple Watch 的自定义 small 布局也会被用于 CarPlay。驾驶相关任务优先保留可读的及时内容，不能让被禁用的按钮成为理解状态的前提。
- Watch 目标的 `Supports Launch for Live Activity Attribute Types` 构建设置决定哪些 ActivityAttributes 可打开 Watch App；不应只凭有 Watch target 就假设跳转已经生效。
- tvOS、visionOS 不支持 Live Activities；兼容 iPhone/iPad App 在 visionOS 上请求也会失败。

## 5. 生命周期与数据更新

### 原生实现职责

| 层 | 职责/关键 API |
|---|---|
| App / ActivityKit | `ActivityAttributes` 描述静态属性，`ContentState: Codable & Hashable` 描述变化状态；`ActivityContent` 携带 `staleDate`、`relevanceScore` |
| Widget extension / SwiftUI | `ActivityConfiguration` 定义锁屏内容与 `DynamicIsland` 四种基础呈现；可与 widgets 共享视图，但不用 widget timeline 更新活动 |
| 能力与授权 | `NSSupportsLiveActivities`；`ActivityAuthorizationInfo().areActivitiesEnabled` 与 `activityEnablementUpdates`；启动失败时保留 App 内状态入口 |
| 生命周期 | `Activity.request`、`update`、`end`；观察 `activityUpdates`、`activityStateUpdates`、`contentUpdates`；重启时用 `Activity.activities` 对账 |
| 服务端 | APNs ActivityKit 通知负责远程 start/update/end；订阅对应凭据更新，处理轮换、失效与过期 |

React Native、Flutter 或 Web 容器也需要原生 widget extension 和 ActivityKit 接入。JS 负责传业务状态与处理路由，不能以 App 内普通视图替代系统实时活动。

### 起止与时效

- 在用户能理解的时机启动，例如已下单、已发起出行或已关注赛事；活动详情里提供关闭/取消跟踪入口，可用 App Shortcut 暴露明确启动动作。
- 普通 App 内请求通常需要前台；`LiveActivityIntent`、ActivityKit push 是官方另行支持的启动路径。不同路径按具体 API 检查条件，不依赖后台常驻。
- 仅在状态或内容改变时推送数据。倒计时可使用系统渲染的日期/时间文本，而不是每秒发 APNs；计时到零后的业务完成仍需要明确更新/结束。
- 设置 `staleDate`，用 `context.isStale` 显示失去时效的信息。stale 不等于任务结束，不应继续呈现未经验证的“实时”数值。
- 活动运行最多 **8 小时**；结束后的锁屏摘要最多再保留 **4 小时**，即最多 12 小时可见，不代表 12 小时都可更新。
- 任务结束立刻调用 `end` 并提交最终状态；结束后从 Dynamic Island/CarPlay 移除。HIG 说明锁屏、Mac 菜单栏与 Watch Smart Stack 可保留结束摘要最多 4 小时。
- 使用 `ActivityUIDismissalPolicy.default`、`.immediate`、`.after(date)` 选择摘要移除策略；HIG 通常建议 15-30 分钟足够，按实际任务价值选择，不视为强制时长。
- 多事件优先考虑一个活动中的聚合布局；确需多个时，以 `relevanceScore` 指示本 App 活动相对重要性。这不保证压过其他 App 或改变系统总体仲裁。
- 区分业务取消、活动结束、用户移除 UI、数据过期；系统移除实时活动并不自动取消服务器上的订单/任务。

### 工程约束

- 静态属性与动态状态的合计数据量不得超过 **4KB**；不在状态中塞图片二进制或完整业务对象。
- Live Activity 自己的沙箱不能联网或接收定位更新，变化由 App 或 APNs 提供。不能使用 widget timeline/扩展网络轮询维持其状态。
- 使用适配展示区和屏幕比例的图片；过大的图像可能导致启动失败。点与像素按目标 scale 区分，不把 45pt 误写为所有设备上的 45px。
- 活动并发数量由系统多种因素决定，包括已安排的活动；不写固定“最多 N 个”的产品承诺。
- App 重建/重启后对账现有 activities，更新仍有关联的活动，结束失去业务关联的活动。

官方主文还提供安排指定日期启动和 `ActivityStyle.transient` 路径。安排启动需要 alert 配置；transient 可在锁屏、收起或点按岛外等情况下结束。它们是单独的原生能力，实施时核对对应 overload 的 SDK availability，不从框架的基础版本推断所有新 API 均可用。

API 路由：[Activity](https://developer.apple.com/documentation/activitykit/activity)、[ActivityContent](https://developer.apple.com/documentation/activitykit/activitycontent)、[ActivityUIDismissalPolicy](https://developer.apple.com/documentation/activitykit/activityuidismissalpolicy)、[指定日期启动](https://developer.apple.com/documentation/activitykit/activity/request(attributes:content:pushType:style:alertConfiguration:startDate:))、[ActivityStyle.transient](https://developer.apple.com/documentation/activitykit/activitystyle/transient)。

## 6. 服务端更新约束

依据 [ActivityKit push notifications](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications)：

- `apns-push-type` 使用 `liveactivity`；单活动请求的 `apns-topic` 使用 `<bundleID>.push-type.liveactivity`。通知更新凭据、远程启动凭据与广播 channel 按各自 API 处理。
- payload 的 `timestamp`、`event`、`content-state` 分别描述时序、start/update/end 和可解码状态；end 也提交最终 state。start 还需要 `attributes-type`、`attributes` 和 alert。
- 数据编码必须匹配 ContentState 和系统默认解码策略；`stale-date`、`dismissal-date`、`relevance-score` 对应时效、结束摘要和本 App 相对重要性。
- 普通更新优先评估 `apns-priority=5`；需要及时关注的关键更新再评估 `10`。高优先级受预算和节流影响，不承诺固定刷新频率或必达。
- 确需高频更新时核对 `NSSupportsLiveActivitiesFrequentUpdates`、`frequentPushesEnabled` 及变更流，服务端跟随用户设置降频。
- 关键 alert 会唤醒屏幕/产生系统提醒；同一事件避免重复发普通推送和 Live Activity alert。
- 离线、乱序和活动已结束时均可能收不到有效更新；恢复后与业务状态对账。广播频道适合多人跟踪同一事件，按官方 APNs 广播能力配置，不当作任意活动的默认实现。

## 7. 交互与无障碍

### 打开详情

- 整体入口用 `widgetURL(_:)`，expanded 内多个详情目的地可用 `Link`。compact 两侧保持同一个目的地。
- 在同一 view hierarchy 放多个 `widgetURL` 的行为未定义。跨呈现可有明确路由，但不要给同一树叠加互相竞争的根 URL。
- App 接收 URL 或 `NSUserActivityTypeLiveActivity` 后定位到对应活动；测试冷启动、登录后恢复和活动已结束时的落点。

### 直接执行

- Expanded/Lock Screen 可使用基于 App Intent 的 `Button`/`Toggle`；Live Activity 动作采用 `LiveActivityIntent`，媒体动作按官方要求使用对应 intent 协议。
- 打开页面用 Link/URL；按钮执行暂停、继续等实际功能。Toggle 反映持续开/关状态，不能以短暂 pressed 外观表示完成。
- intent 可在 App 进程执行，不假设 Widget extension 和 App 共享运行时内存。执行结果要更新业务状态和 Live Activity，失败时反馈正确状态。
- 锁定设备上的动作受系统认证/解锁控制；CarPlay 的 Live Activity 控件不会执行动作。

### 可访问性

- 所有呈现都补齐 `accessibilityLabel`、必要的 `accessibilityValue` 和动作名称；组合图形、数值与单位，避免装饰项重复朗读。
- 动态图片/SF Symbol 状态变化时同步更新可访问描述，不保留旧标签。
- 文字缩写和精度减少后仍保留可理解含义；状态不得仅依赖颜色、动画或细边线。

## 8. 动效

动效与第 3 节的视觉 token 分开。官方区分系统展示转场与视图内容更新：

- 系统控制岛的展开/收缩和设备呈现；内容更新可使用支持的 SwiftUI transition/contentTransition/animation。
- 数据变化动画最长 **2 秒**。重点数值可用 `.numericText()`，布局变化尽量保持已有元素连续移动；多项更新避免碰撞或同时争抢注意力。
- Always-On 降低亮度时系统不执行动画；同时处理 `isLuminanceReduced` 与 Reduce Motion，让静态结果保留全部信息。
- iOS 16 上 `.animation`/`withAnimation` 等自定义 timing 被忽略，系统使用自身 timing，仍支持部分内建 transition。支持更多 SwiftUI 动画的系统依照专门的 WidgetKit 动画文档处理。
- 需要取消局部更新动画时使用文档支持的 identity transition/`animation(nil, value:)` 路径；该渲染环境不支持用 `Transaction.animation` 取消动画。
- 不用无限循环、手写帧动画或周期性伪更新吸引注意；计时文本的系统更新也不代表扩展持续运行。

来源差异：ActivityKit 主教程的动画段仍有未注明版本的“忽略 animation modifiers”说法；[WidgetKit 动画专题](https://developer.apple.com/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities)明确将该限制限定到 iOS 16 及更早版本。这里保留版本区分，实施时以目标系统和专门文档为依据。Web 参考见 [../web/apple-style-motion-templates.md](../web/apple-style-motion-templates.md)，其中前端时长不是 Apple 原生规范。

## 9. 跨平台语义与实现边界

| 可共享 | Apple 原生落点 | Android / Windows / Web 对应策略 |
|---|---|---|
| 有起止的持续任务、身份、关键进度 | ActivityKit 状态与四种呈现 | Android 按系统支持选择持续/进度通知等入口；Windows 使用适当系统通知或 App 内任务状态；Web 使用持续状态区 |
| 详情深链、必要直接动作 | widgetURL/Link/App Intent | 使用目标平台支持的路由和命令，保持活动 ID 和操作结果一致 |
| stale、完成摘要、用户停止跟踪 | staleDate、end、dismissal policy | 共享状态意义；保留时间和可见位置按平台及产品决定 |
| 一眼可读、低干扰、隐私 | 黑底岛、锁屏、设备联动 | 共享信息优先级，按实际背景、输入和目标平台做可访问性设计 |

Dynamic Island 外壳/摄像头绕排、ActivityFamily、Watch 联动、iPhone Mirroring、CarPlay 禁用规则以及 8h/4h 限制均为 Apple 系统特性，不是跨平台硬编码规范。其他平台的对应入口不等于 Apple Live Activity；一次性 toast 不足以承载需持续跟踪的活动。

## 10. 尺寸参考

以下均为 **pt**，来自本次 HIG Specifications 快照。系统可缩放，应用布局由系统确定；这些值用于预览和边界测试，不作为固定 frame 或未来设备枚举。

| iPhone 屏幕 | Compact 每侧 | Minimal | Expanded / Lock Screen |
|---|---|---|---|
| 430x932 | 62.33x36.67 | 宽 36.67-45，高 36.67 | 宽 408，高 84-160 |
| 393x852 | 52.33x36.67 | 宽 36.67-45，高 36.67 | 宽 371，高 84-160 |

文档中的岛外圆角参考为 44pt；compact/minimal 整体宽度示例为 230/250pt，expanded 为 371/408pt。不要将每侧内容宽度与整岛宽度混淆；文档设备表不是设备 capability 检测方法。超出 160pt 高度的普通呈现可能被截断。

| iPad 屏幕（按官方表原值） | Lock Screen |
|---|---|
| 1366x1024 | 宽 500，高 84-160 |
| 1194x834、1012x834、1080x810、1024x768 | 宽 425，高 84-160 |

Mac 按 HIG 使用 iOS 尺寸参考。Watch Smart Stack 参考：

| Watch 尺寸 | 40mm | 41mm | 44mm | 45mm | 49mm |
|---|---|---|---|---|---|
| 内容 | 152x69.5 | 165x72.5 | 173x76.5 | 184x80.5 | 191x81.5 |

CarPlay 内容检查 240x78、240x100、170x78；Smart Display Zoom 模拟器覆盖宽屏 1920x720、竖屏 900x1200、标准 800x480。这些是 CarPlay 专属验证场景。

## 11. 验收与辅助工具

- 用 Apple Design Resources 模板和 Xcode previews 覆盖四种基础呈现，检查长文案、RTL、图片 scale、边距和品牌 mark；不在技能包内复制展示图。
- 用 Simulator/真机检查有岛/无岛、浅/深色、壁纸、Always-On、StandBy 放大/夜间、VoiceOver、Reduce Motion。普通前台截图不能证明锁屏或低亮度正确。
- 实际执行开始、关键更新、过期、暂停/继续、失败、结束与摘要移除；另测关闭授权、离线、App 重启、多个活动仲裁和冷启动深链。
- 面向 Apple Watch/Mac/CarPlay 时分别测试配对和实际入口；CarPlay 检查按钮禁用以及支持/不支持 CarPlay 的 App 打开行为。
- APNs 使用 [Push Notifications Console](https://developer.apple.com/documentation/usernotifications/testing-notifications-using-the-push-notification-console) 或官方测试流程；Console 排错可关注 `liveactivitiesd`、`apsd`、`chronod`。模拟器推送测试还需满足官方 Mac/系统条件。
- 报告记录系统、设备、呈现、任务状态、授权与配对条件；区分布局预览通过、数据更新通过、锁屏/其他设备实际呈现通过。

## 12. 必要官方来源

除调用地图中的主题页，按需要继续查：

- [ActivityKit](https://developer.apple.com/documentation/activitykit)：总入口与平台支持。
- [Adding accessible descriptions](https://developer.apple.com/documentation/activitykit/adding-accessible-descriptions-to-widgets-and-live-activities)：动态图形与状态标签。
- [Linking to specific app scenes](https://developer.apple.com/documentation/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity)：URL 层级与 App 接收。
- [ActivityFamily](https://developer.apple.com/documentation/widgetkit/activityfamily)、[activityFamily environment](https://developer.apple.com/documentation/swiftui/environmentvalues/activityfamily)：补充尺寸家族与可用性。
- [Displaying dynamic dates](https://developer.apple.com/documentation/widgetkit/displaying-dynamic-dates)：系统更新的时间文本。
- [Apple Design Resources](https://developer.apple.com/design/resources/)：默认边距和文本模板。
- [Live Activities essentials, WWDC26](https://developer.apple.com/videos/play/wwdc2026/223/)：HIG 当前列出的教学入口。
- [Supercharge your app for CarPlay, WWDC25](https://developer.apple.com/videos/play/wwdc2025/216/)、[What’s new in widgets, WWDC25](https://developer.apple.com/videos/play/wwdc2025/278/)：补充设备联动。

HIG 页末列出的 2025-12-16 更新加入/扩展了 macOS 与 CarPlay 指导；这里以本次读取内容为准，不把旧“只有锁屏/灵动岛”的概述作为完整范围。
