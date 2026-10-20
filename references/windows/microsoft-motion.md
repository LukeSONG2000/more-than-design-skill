# Microsoft Motion

Windows 原生 Motion 与 Fluent Web Motion 共享“功能、自然、一致、克制”的目标，但实现层不同。WinUI 标准控件和系统转场优先由平台负责；Web 使用 Fluent Motion 原则和浏览器可访问性。视觉样式、材质和组件见 [fluent-foundations-components.md](fluent-foundations-components.md)。

## 目录

- [官方入口](#官方入口)
- [Windows 原生 Motion](#windows-原生-motion)
- [Windows timing 与 easing](#windows-timing-与-easing)
- [Windows 原生转场](#windows-原生转场)
- [Fluent Web Motion](#fluent-web-motion)
- [动效编舞](#动效编舞)
- [系统控件与自定义动画](#系统控件与自定义动画)
- [减少动态与无动画](#减少动态与无动画)
- [跨平台边界](#跨平台边界)
- [验收清单](#验收清单)

## 官方入口

| 内容 | 官方来源 | 用途 |
|---|---|---|
| Windows signature motion | [Windows motion](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/motion) | Windows 11 原生原则、curve、duration、控件与页面转场 |
| Fluent 2 motion | [Fluent motion](https://fluent2.microsoft.design/motion/) | Web/跨平台的功能性动效、transition 和可访问性 |
| Windows animation overview | [Animations overview](https://learn.microsoft.com/en-us/windows/apps/design/motion/) | Windows app 动画模式和开发路线 |
| WinUI animations | [Animations in XAML](https://learn.microsoft.com/en-us/windows/apps/develop/motion/xaml-animation) | 原生 API、theme transitions、theme animations 和 connected animations |
| Accessibility | [Windows accessibility](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview) | 键盘、Narrator、个性化与高对比度验收 |

## Windows 原生 Motion

[Windows motion](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/motion) 将平台动效描述为 connected、consistent、responsive、delightful、resourceful：

- **Connected**：保持来源、目标与层级连续，减少用户重新定位。
- **Consistent**：同一类进入、退出、层级与控件状态使用一致模式。
- **Responsive**：输入后立即反馈，不因长动画阻断连续操作。
- **Delightful**：微交互可增加质感，但不能持续争夺注意力。
- **Resourceful**：优先系统/WinUI 已实现的动画，避免重复维护与高绘制成本。

原生实现先使用 WinUI controls 和 theme transitions。它们会随平台更新，并处理输入、焦点、窗口与系统设置；入口见 [Animations in XAML](https://learn.microsoft.com/en-us/windows/apps/develop/motion/xaml-animation)。

## Windows timing 与 easing

下表来自当前 [Windows signature motion](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/motion)。这些是 Windows 原生参考，不是 Web、Android 或 Apple 的通用 Token。

| 模式 | Curve | Duration | 属性/要求 |
|---|---|---|---|
| Direct entrance / Fast in | `cubic-bezier(0, 0, 0, 1)` | `167 / 250 / 333ms` | position、scale、rotation；按距离与规模选择 |
| Existing elements / Point to point | `cubic-bezier(0.55, 0.55, 0, 1)` | `167 / 250 / 333ms` | 已在屏幕内元素的位置、缩放、旋转 |
| Direct exit / Fast out | `cubic-bezier(0, 0, 0, 1)` | `167ms` | position、scale、rotation，官方要求总是配合 fade out |
| Gentle exit / Soft out | `cubic-bezier(1, 0, 1, 1)` | `167ms` | position、scale；较柔和离场 |
| Bare minimum / Fade | `linear` | `83ms` | 仅 opacity；不用于空间移动 |

### Strong entrance

[Windows motion](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/motion) 还给出三关键帧的 elastic strong entrance：

| Keyframe | Curve | Duration |
|---|---|---:|
| 1 | `cubic-bezier(0.85, 0, 0, 1)` | `167ms` |
| 2 | `cubic-bezier(0.85, 0, 0.75, 1)` | `167ms` |
| 3 | `cubic-bezier(0.85, 0, 0, 1)` | `333ms` |

Strong entrance 只用于需要明确强调的重要进入，不应成为所有卡片和按钮的默认。高频生产力操作优先 direct entrance 或控件内置反馈。

## Windows 原生转场

[Windows animation guidance](https://learn.microsoft.com/en-us/windows/apps/design/motion/) 与 [Animations in XAML](https://learn.microsoft.com/en-us/windows/apps/develop/motion/xaml-animation) 的常见模式：

| 模式 | 用途 | 原则 |
|---|---|---|
| Page transition | 同一 surface 内页面切换 | 方向与应用信息流一致，进入/退出成对，导航与标题保持稳定 |
| Connected animation | 同一对象在列表与详情间延续 | 只连接用户关注的共享对象，目标不存在时安全降级 |
| Content transition | 当前容器内部内容/状态改变 | 不制造新页面层级，保持焦点和容器尺寸可预测 |
| Popup/flyout transition | 临时层出现和消失 | 来源、定位与 dismiss 关系清晰，优先系统 flyout/menu |
| Reposition | 布局变化或集合重排 | 帮助追踪对象，不延迟后续输入 |
| Pointer/press feedback | hover、press、release | 立即、短促，交给标准控件处理 |

原生页面和控件应使用 WinUI 提供的 theme transitions/animations；自定义曲线只有在系统模式无法表达任务关系时才加入。不要在系统 `MenuFlyout`、`ContentDialog`、`NavigationView` 等标准控件外再包一层冲突动画。

## Fluent Web Motion

[Fluent 2 motion](https://fluent2.microsoft.design/motion/) 要求动画 functional、natural、consistent、appealing：

- **Functional**：解释状态、方向、层级和操作结果。
- **Natural**：持续时间短且与距离/尺寸匹配；大、远、复杂的变化可以更慢。
- **Consistent**：同类元素复用同一 motion Token 和 transition pattern。
- **Appealing**：适度强化品牌和完成感，不影响高频任务。

Linear easing 只适合持续恒速旋转等没有自然加减速的运动。进入、退出和空间移动应使用相应 Fluent curve/Token，并从当前 [Fluent motion](https://fluent2.microsoft.design/motion/) 页面取值，避免复制过期版本。

### Fluent transition patterns

| 模式 | 场景 | 实现要点 |
|---|---|---|
| Enter / exit | 元素加入或移出当前上下文 | 立即反馈；退出通常更快，不妨碍下一个操作 |
| Elevation | 元素从 surface 升起或落回 | shadow/material/position 同步，避免只有阴影漂移 |
| Top-level fade | 顶层区域或目的地切换 | 不暗示父子 push，保持导航稳定 |
| Container transform | 来源容器转成目标容器 | 保持边界和共享内容连续，避免重复对象同时可见 |

这些模式来自 [Fluent motion](https://fluent2.microsoft.design/motion/)；具体组件若已有内置动画，以 [Fluent React components](https://fluent2.microsoft.design/components/web/react) 的实现为准。

## 动效编舞

- 先动画主因果对象，再让次要元素短暂跟随；来源见 [Fluent motion](https://fluent2.microsoft.design/motion/)。
- stagger 用于建立阅读层级，不对长列表逐项延迟，避免用户等待。
- 同一操作中只保留一个主要空间方向；背景、标题、按钮同时反向运动会破坏定位。
- 进入前确定焦点去向，退出后恢复触发点或下一个逻辑目标。
- 对窗口 resize、snap 和 density 变化，布局应立即可用；只对可追踪对象做短 reposition。
- Web 动画优先 `transform` 与 `opacity`，显式列出属性，禁止 `transition: all`。

## 系统控件与自定义动画

| 场景 | 首选 | 何时自定义 |
|---|---|---|
| WinUI button、menu、dialog、navigation、tab、selection | WinUI 内置状态/transition，见 [Controls](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/) | 官方控件无法表达产品特有内容关系时，仅补外围内容动画 |
| Mica/Acrylic/flyout | 系统材料和系统呈现，见 [Windows materials](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/materials) | 不自定义材质内部光学运动 |
| Fluent React components | 组件内置状态，见 [Fluent React](https://fluent2.microsoft.design/components/web/react) | 页面层级、数据重排和产品专属 transition |
| 自绘 Canvas/WebGL | 产品自定义，但遵守 focus/DOM 替代和减少动态 | 必须提供可访问结构、暂停和低动态模式 |

不要用自定义 spring 模拟 Windows 系统 menu、flyout 或 selection，再声称是原生效果。标准组件由平台负责的材质和动画应保持系统所有权。

## 减少动态与无动画

[Fluent motion](https://fluent2.microsoft.design/motion/) 要求支持 no motion/减少动态设置：

- 取消大位移、视差、连续旋转、缩放、弹性和自动播放。
- 保留操作结果，可改为短淡化、即时状态切换或静态替代。
- 不闪烁，不用快速动画传达必须读取的信息。
- 将动画限制在当前焦点附近，避免周边内容持续移动。
- 非视觉替代可通过文本、状态、声音/公告（在用户允许时）表达。

Windows 原生应尊重系统动画偏好并使用系统控件；Web 使用 `prefers-reduced-motion`：

```css
@media (prefers-reduced-motion: reduce) {
  .fluent-transition {
    animation: none;
    transition: opacity 80ms linear;
    transform: none;
  }
}
```

无动画模式不能隐藏 loading/error/success。状态仍需文本、图标、ARIA live region 或可读布局；Web 无障碍基础见 [Fluent accessibility](https://fluent2.microsoft.design/accessibility/)，Windows 原生见 [Accessibility overview](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessibility-overview)。

## 跨平台边界

| 内容 | 适用性 | 处理方式 |
|---|---|---|
| 功能、自然、一致、减少动态 | Universal | 原则可迁移；来源 [Fluent motion](https://fluent2.microsoft.design/motion/) |
| Windows curve/duration 与 WinUI theme animations | Windows-only / adapted | Windows 原生直接使用；Web/Android/Apple 不作为默认 Token；来源 [Windows motion](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/motion) |
| Fluent transition patterns | Web/Microsoft ecosystem | Fluent Web 可直接参考，其他平台换成原生转场；来源 [Fluent motion](https://fluent2.microsoft.design/motion/) |
| 系统 menu/flyout/material 动效 | Windows-only | 由 WinUI/系统负责，不跨平台模拟；来源 [WinUI controls](https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/) |

## 验收清单

- 是否明确这是 Windows 原生 Motion 还是 Fluent Web Motion？
- WinUI 标准组件是否保留平台内置状态和转场？
- 进入、屏内移动、退出是否使用正确曲线，而不是统一 `ease`？
- Direct exit 是否按官方要求结合 fade out？
- Strong entrance 是否只用于低频重点时刻？
- 动画是否可中断、不阻塞连续键盘/指针操作？
- 焦点、tab order 和 UI Automation/ARIA 是否不依赖动画完成？
- Windows 系统动画偏好与 Web `prefers-reduced-motion` 是否都已测试？
- 材质、颜色和 shadow 是否在样式文件定义，而非混入 motion Token？
