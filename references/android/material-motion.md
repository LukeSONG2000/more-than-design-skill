# Material 3 Motion

本文件只处理 Material 动效。颜色、字体、shape、spacing 与 elevation 见 [material-foundations-styles.md](material-foundations-styles.md)；组件角色和状态见 [material-components-map.md](material-components-map.md)。

## 目录

- [官方入口](#官方入口)
- [Motion physics system](#motion-physics-system)
- [Expressive 与 Standard](#expressive-与-standard)
- [Spatial 与 Effects](#spatial-与-effects)
- [平台实现](#平台实现)
- [Web 曲线 fallback](#web-曲线-fallback)
- [转场模式](#转场模式)
- [编舞与中断](#编舞与中断)
- [可访问性](#可访问性)
- [验收清单](#验收清单)

## 官方入口

| 内容 | 官方来源 | 用途 |
|---|---|---|
| Motion physics system | [How it works](https://m3.material.io/styles/motion/overview/how-it-works) | 当前 Material 3 Expressive 的物理模型、scheme 和 Token 分类 |
| Motion specs | [Specs](https://m3.material.io/styles/motion/overview/specs) | Compose/Views/Web 支持状态与 Web 曲线转换表 |
| Legacy easing/duration | [Easing and duration](https://m3.material.io/styles/motion/easing-and-duration) | 仍用于部分过渡和不支持 spring 的 fallback |
| Transition patterns | [Transition patterns](https://m3.material.io/styles/motion/transitions/transition-patterns) | container、forward/backward、lateral、top-level、enter/exit 等模式 |
| Android predictive back | [Predictive back](https://developer.android.google.cn/design/ui/mobile/guides/patterns/predictive-back) | 系统返回手势的进度驱动与预览 |

## Motion physics system

[Material motion physics](https://m3.material.io/styles/motion/overview/how-it-works) 在 2025 年引入，以 spring physics 为大多数组件动效的当前模型。它用 stiffness、damping 和 initial velocity 描述运动，让动画可响应中断、手势与目标变化，而不是只按固定时长播放。

关键原则：

- 动效解释状态、空间关系和操作结果，不是附加装饰。
- 用户输入驱动的动画应可中断并从当前速度/位置继续。
- 使用系统/组件提供的 motion Token，不在各页面手写相似但不同的 spring。
- spring composite Token 把 damping 和 stiffness 组合为可复用值；官方说明见 [Motion specs](https://m3.material.io/styles/motion/overview/specs)。
- legacy easing、duration 和 path Token 不属于新 physics system 的主要参数，但仍为兼容和 transition 使用。

## Expressive 与 Standard

[How it works](https://m3.material.io/styles/motion/overview/how-it-works) 提供两种 motion scheme：

| Scheme | 用途 | 特征 | 避免 |
|---|---|---|---|
| Expressive | 关键时刻、重要转换、能强化个性和空间连续性的动作 | 更有弹性，spatial 运动可适度 overshoot | 所有微交互都弹跳，或在高频生产力操作中拖慢节奏 |
| Standard | 工具性、高频、需要克制和稳定反馈的动作 | 最小化 bounce，仍保持自然减速和连续性 | 退化成机械 linear 或完全没有状态反馈 |

选择 scheme 看任务频率和注意力成本，不按页面“风格”一刀切。一次流程内可让主要容器使用 expressive、次要 effects 使用 standard，但应复用官方 Token，保持节奏一致。

## Spatial 与 Effects

新体系区分两种 Token 类型，来源见 [How it works](https://m3.material.io/styles/motion/overview/how-it-works)：

| 类型 | 属性 | 运动特征 | 规则 |
|---|---|---|---|
| Spatial | position、rotation、size、corner/shape 等空间属性 | 可以 overshoot，表达质量、连接和形变 | 保持内容可读；目标变化时连续接管，不跳帧重启 |
| Effects | color、opacity 等视觉效果属性 | 不应 overshoot 到无效颜色或 opacity 范围 | 与 spatial 同步但通常更短，避免幽灵残影 |

每类均有 fast、default、slow 速度级别。速度由空间距离、尺寸变化、层级和操作重要性决定；不要仅因设备性能任意缩短，性能问题应先减少同时动画的元素和绘制成本。

## 平台实现

[Motion specs](https://m3.material.io/styles/motion/overview/specs) 当前说明：

| 平台 | 官方状态 | 使用方式 |
|---|---|---|
| Jetpack Compose | Available | 使用内置 Material 3 组件和 spring Token |
| Android Views / MDC-Android | Available，但未自动加入所有组件 | 使用内置 spring Token，并核对组件实际实现 |
| Web | Compatible | 能用 spring 时使用 spring；仅对不可中断、非手势动画使用官方拟合曲线 |

Android 系统转场、Predictive Back 和标准组件动效优先交给系统/库。自定义动画不应覆盖系统手势进度或制造第二套返回逻辑；参考 [Predictive back](https://developer.android.google.cn/design/ui/mobile/guides/patterns/predictive-back)。

## Web 曲线 fallback

下表来自 [Material motion specs](https://m3.material.io/styles/motion/overview/specs) 的 Web spring-to-curve 转换。它只适用于**不会被中断且不直接跟随手势**的动画；交互式动画应使用真正的 spring 或进度驱动实现。

| Motion Token | `cubic-bezier()` | Duration |
|---|---|---:|
| Expressive fast spatial | `0.42, 1.67, 0.21, 0.90` | `350ms` |
| Expressive default spatial | `0.38, 1.21, 0.22, 1.00` | `500ms` |
| Expressive slow spatial | `0.39, 1.29, 0.35, 0.98` | `650ms` |
| Expressive fast effects | `0.31, 0.94, 0.34, 1.00` | `150ms` |
| Expressive default effects | `0.34, 0.80, 0.34, 1.00` | `200ms` |
| Expressive slow effects | `0.34, 0.88, 0.34, 1.00` | `300ms` |
| Standard fast spatial | `0.27, 1.06, 0.18, 1.00` | `350ms` |
| Standard default spatial | `0.27, 1.06, 0.18, 1.00` | `500ms` |
| Standard slow spatial | `0.27, 1.06, 0.18, 1.00` | `750ms` |
| Standard fast effects | `0.31, 0.94, 0.34, 1.00` | `150ms` |
| Standard default effects | `0.34, 0.80, 0.34, 1.00` | `200ms` |
| Standard slow effects | `0.34, 0.88, 0.34, 1.00` | `300ms` |

CSS 示例只表达 Token，不应散落到业务选择器：

```css
:root {
  --md-motion-expressive-spatial-default:
    500ms cubic-bezier(0.38, 1.21, 0.22, 1);
  --md-motion-standard-effects-fast:
    150ms cubic-bezier(0.31, 0.94, 0.34, 1);
}

.container-change {
  transition:
    transform var(--md-motion-expressive-spatial-default),
    border-radius var(--md-motion-expressive-spatial-default),
    opacity var(--md-motion-standard-effects-fast);
}
```

不要使用 `transition: all`；空间属性和 effects 应显式分开，才能使用不同 Token 和 reduced-motion 替代。

## 转场模式

[Material transition patterns](https://m3.material.io/styles/motion/transitions/transition-patterns) 当前列出以下语义模式：

| 模式 | 适用关系 | 实现要点 |
|---|---|---|
| Container transform | 一个可见容器转变为后继容器 | 保持共享内容/边界连续，避免同时交叉淡化所有内容 |
| Forward/backward | 同一任务层级的前进与返回 | 方向成对，返回应恢复来源上下文 |
| Lateral | 同级内容或目的地之间移动 | 不暗示父子层级；顶层导航仍服从组件规范 |
| Top level | 顶层目的地切换 | 保持导航稳定，内容变化不应模拟层级 push |
| Enter/exit | 元素加入或离开当前结构 | entrance 与 exit 的注意力权重不同，移除后焦点要可预测 |
| Skeleton loaders | 内容结构可预测但数据尚未就绪 | 骨架应匹配最终布局，避免无意义无限闪烁 |

官方当前注明 transitions 仍使用 legacy easing/duration，并会继续更新；实现前同时核对 [Transition patterns](https://m3.material.io/styles/motion/transitions/transition-patterns) 与 [Easing and duration](https://m3.material.io/styles/motion/easing-and-duration)。不要用 spring-to-curve 表替换所有系统转场。

## 编舞与中断

- 一个动作只设一个主要视觉因果链，次要元素跟随而不是同时抢注意力；原则来源 [Motion physics](https://m3.material.io/styles/motion/overview/how-it-works)。
- 多元素 stagger 应短且有阅读顺序；列表每项长延迟会阻塞操作。
- 目标改变时，从当前状态和速度继续；不要先跳回初态再重播。
- 手势驱动部分使用手势 progress，释放后才交给 spring 收敛。
- 动画不得改变 DOM/语义焦点顺序；视觉移动结束后焦点仍应对应逻辑位置。
- 大范围 blur、filter 和阴影动画可能昂贵，优先 transform/opacity，shape morph 只在必要范围使用。

## 可访问性

[Material accessibility principles](https://m3.material.io/foundations/overview/principles) 要求界面支持不同感知和输入需求。Motion 验收至少包括：

- 系统减少动态开启时，取消大位移、旋转、视差、弹跳和自动播放；保留即时或短淡化的状态确认。
- 不以动画方向作为唯一导航线索；同时提供标题、焦点和结构变化。
- 避免闪烁、快速循环和无法暂停的背景动效。
- loading/progress 向辅助技术提供状态，不能只呈现视觉动画；参考 [Progress indicators accessibility](https://m3.material.io/components/progress-indicators/accessibility)。
- Web 使用 `prefers-reduced-motion`，Android 使用系统 animator duration/无动画偏好并测试 TalkBack。

```css
@media (prefers-reduced-motion: reduce) {
  .container-change {
    transition: opacity 100ms linear;
    transform: none;
  }
}
```

## 验收清单

- 是否先选组件/转场语义，再选 expressive 或 standard？
- spatial 与 effects 是否使用不同 Token，且没有 `transition: all`？
- Android 系统组件和 Predictive Back 是否由系统/官方库负责？
- 手势动画是否可中断并连续接管？
- Web 曲线是否只用于不可中断、非手势 fallback？
- transition 是否仍按当前 [官方 transition 文档](https://m3.material.io/styles/motion/transitions/transition-patterns) 实现？
- reduced motion 是否保留操作结果而移除大幅运动？
- 动效是否没有遮挡内容、改变布局命中区或破坏焦点？
