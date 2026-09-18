# More Than Design

面向前端与客户端开发的多平台官方设计规范 Skill。它与 `frontend-design` 同时使用，根据实际运行平台选择 Android/Material、Windows/Microsoft Fluent 或 Apple/HIG，并为 Web 按产品语境选择参考体系。

## 平台路由

| 目标 | 设计规范 | 开发文档 |
|---|---|---|
| Android 手机、平板、折叠屏 | [Android Mobile Design](https://developer.android.google.cn/design/ui/mobile)、[Material 3](https://m3.material.io/) | [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)、[Material 3 Develop](https://m3.material.io/develop) |
| Windows 桌面应用 | [Windows Design](https://learn.microsoft.com/en-us/windows/apps/design/)、[Fluent 2](https://fluent2.microsoft.design/) | [Windows development](https://developer.microsoft.com/zh-cn/windows/develop)、[WinUI 3](https://learn.microsoft.com/windows/apps/winui/winui3/) |
| Apple 生态 | [Apple Design / HIG](https://developer.apple.com/cn/design/) | [Apple Developer Documentation](https://developer.apple.com/documentation/) |
| Web | 结合品牌、工作流和现有组件库选择 | 项目技术栈优先，不伪装系统专属能力 |

Web 没有固定体系：消费、内容与创意产品倾向 Apple；企业生产力和桌面密集工作流倾向 Microsoft；移动优先、动态主题和跨窗口组件系统倾向 Material。条件相同且没有其他约束时，偏好为 Apple > Microsoft > Google。

## 使用原则

- 先判断目标平台、窗口、输入方式和技术栈，再查对应官方地图。
- 原生平台优先标准组件和系统行为；不以自绘近似替代系统菜单、导航、材质或返回逻辑。
- 样式与动效分开：颜色、字体、间距、shape、material 和 elevation 不与 motion 参数混写。
- 跨平台只迁移任务语义和通用原则，控件解剖、系统材质、导航和平台 API 保留在原平台。
- 每个分类条目链接到官方原文；二手文章仅可作为线索，不作为规范来源。
- 无障碍覆盖键盘、触摸、指针、屏幕阅读器、文字缩放、高对比度、深浅色和减少动态。

完整决策树见 [references/18-platform-routing.md](references/18-platform-routing.md)。

面向 iOS 26+ 与 Android 多 OEM 的共享语义、平台原生实现、自适应布局和测试策略见 [references/26-cross-platform-baseline.md](references/26-cross-platform-baseline.md)、[references/27-adaptive-platform-capabilities.md](references/27-adaptive-platform-capabilities.md) 和 [references/28-semantic-components-testing.md](references/28-semantic-components-testing.md)。

iPhone Duo 的双显示、折叠姿态、Reserved Region、Arrangement View、竖向系统栏、多场景与双前摄适配见 [references/29-iphone-duo-adaptation.md](references/29-iphone-duo-adaptation.md)。Duo 专有能力不能直接当作 Android/Web 的通用折叠屏 API。

Android 折叠屏的窗口容量、`FoldingFeature`、tabletop/book posture、canonical panes、adaptive navigation、显示模式和质量分级见 [references/30-android-foldable-adaptation.md](references/30-android-foldable-adaptation.md)，其中包含与 Apple Duo 的共享设计语义和不可一对一映射项。

跨平台界面图标按语义分别落到 SF Symbols、Material Symbols 和 Segoe Fluent Icons，见 [references/31-cross-platform-interface-icons.md](references/31-cross-platform-interface-icons.md)。跨平台 App Icon 的品牌母版、平台派生、商店资产、工具链与最终包验收见 [references/32-cross-platform-app-icons.md](references/32-cross-platform-app-icons.md)。

## 内容地图

### 跨平台图标系统

| 文件 | 内容 |
|---|---|
| [31-cross-platform-interface-icons.md](references/31-cross-platform-interface-icons.md) | Apple、Google/Material、Windows 原生界面图标库、API、状态与语义对齐 |
| [32-cross-platform-app-icons.md](references/32-cross-platform-app-icons.md) | Apple Icon Composer、Windows App Icon、Android Adaptive/Play Icon 的设计、适配、工具与验收 |

### Material & Google Design

| 文件 | 内容 |
|---|---|
| [19-google-android-map.md](references/19-google-android-map.md) | Android Mobile Design、Material 3 和开发入口的官方深度链接地图 |
| [20-material-foundations-styles.md](references/20-material-foundations-styles.md) | 无障碍、内容、Design Token、状态、布局、颜色、字体、elevation、shape、spacing、icon |
| [21-material-components-map.md](references/21-material-components-map.md) | Material 3 全组件 overview/guidelines/specs/accessibility 索引 |
| [22-material-motion.md](references/22-material-motion.md) | Motion physics、Expressive/Standard、Spatial/Effects、转场和 Web fallback |
| [30-android-foldable-adaptation.md](references/30-android-foldable-adaptation.md) | Android 折叠屏与 Adaptive Apps 专项，以及 Apple Duo 语义对齐 |

### Microsoft Design

| 文件 | 内容 |
|---|---|
| [23-microsoft-windows-map.md](references/23-microsoft-windows-map.md) | Windows Design、WinUI/Windows App SDK、Fluent 2 官方地图 |
| [24-fluent-foundations-components.md](references/24-fluent-foundations-components.md) | Windows/Fluent 原则、Token、颜色、材质、布局、排版、无障碍和组件索引 |
| [25-microsoft-motion.md](references/25-microsoft-motion.md) | Windows 原生 Motion 与 Fluent Web Motion 的独立规范 |

### Apple Design

- [Apple 官方覆盖地图](references/08-apple-docs-coverage.md)
- [Apple 官方深度链接地图](references/10-apple-official-docs-map.md)
- [HIG Foundations / Patterns](references/11-hig-foundations-patterns.md)
- [HIG Components / Inputs](references/12-hig-components-inputs.md)
- [平台、资源、字体和技术品牌](references/13-platform-resources-technologies.md)
- [iPhone Duo 折叠屏适配](references/29-iphone-duo-adaptation.md)
- [Liquid Glass adoption](references/14-liquid-glass-adoption.md)
- [Liquid Glass controls](references/15-liquid-glass-controls.md)
- [Liquid Glass API、Motion 与 Color](references/16-liquid-glass-api-motion-color.md)
- [Liquid Glass 官方深度链接地图](references/17-liquid-glass-deep-link-map.md)

### Apple.com 实现参考

`references/00–07` 和 `09` 保留原有 Apple.com/HIG 风格的哲学、Token、Web 组件、布局、无障碍、Tailwind、字体和动画模板。它们属于 Apple/Web 专项，不作为 Android 或 Windows 的默认数值。

## 安装

### Codex

```bash
git clone https://github.com/LukeSONG2000/more-than-design-skill.git \
  ~/.codex/skills/more-than-design-skill
```

### Claude Code

```bash
git clone https://github.com/LukeSONG2000/more-than-design-skill.git \
  ~/.claude/commands/more-than-design-skill
```

## 字体资源

仓库保留 [refinec/PingFangSC](https://github.com/refinec/PingFangSC) 的 PingFang SC fallback：非 Apple Web 使用 `woff2`，客户端可使用 `ttf`，Apple 设备优先系统字体。详细方案见 [references/06-fonts.md](references/06-fonts.md)。字体资源只服务 Apple 风格或明确需要统一中文观感的项目，不作为 Android/Windows 默认字体。

## 验证状态

- 新增平台资料中的官方链接已逐项访问验证。
- `skill-home validate --strict` 通过。
- `skill-home scan --strict` 通过。
- Codex、Agents frontend-design 触发描述和 Claude 镜像保持同步。

## 许可证与归属

代码和原创整理采用 MIT License。Apple、Google、Material、Microsoft、Windows、Fluent 及相关商标、设计资源和文档归各自权利人所有。本项目用于设计学习与开发参考，不代表任何平台官方产品或背书。
