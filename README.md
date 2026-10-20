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

完整决策树见 [references/cross-platform/platform-routing.md](references/cross-platform/platform-routing.md)。

面向 iOS 26+ 与 Android 多 OEM 的共享语义、平台原生实现、自适应布局和测试策略见 [references/cross-platform/cross-platform-baseline.md](references/cross-platform/cross-platform-baseline.md)、[references/cross-platform/adaptive-platform-capabilities.md](references/cross-platform/adaptive-platform-capabilities.md) 和 [references/cross-platform/semantic-components-testing.md](references/cross-platform/semantic-components-testing.md)。

iPhone Duo 的双显示、折叠姿态、Reserved Region、Arrangement View、竖向系统栏、多场景与双前摄适配见 [references/apple/iphone-duo-adaptation.md](references/apple/iphone-duo-adaptation.md)。Duo 专有能力不能直接当作 Android/Web 的通用折叠屏 API。

Android 折叠屏的窗口容量、`FoldingFeature`、tabletop/book posture、canonical panes、adaptive navigation、显示模式和质量分级见 [references/android/android-foldable-adaptation.md](references/android/android-foldable-adaptation.md)，其中包含与 Apple Duo 的共享设计语义和不可一对一映射项。

跨平台界面图标按语义分别落到 SF Symbols、Material Symbols 和 Segoe Fluent Icons，见 [references/cross-platform/cross-platform-interface-icons.md](references/cross-platform/cross-platform-interface-icons.md)。跨平台 App Icon 的品牌母版、平台派生、商店资产、工具链与最终包验收见 [references/cross-platform/cross-platform-app-icons.md](references/cross-platform/cross-platform-app-icons.md)。

## 内容地图

统一入口为 [SKILL.md](SKILL.md)，按目标平台选择 [跨平台](references/cross-platform/index.md)、[Android](references/android/index.md)、[Windows](references/windows/index.md)、[Apple 原生](references/apple/index.md)或 [Web](references/web/index.md)。只加载本次任务需要的资料。

样式与动效分别路由。Apple 原生动效见[独立入口](references/apple/motion.md)，Liquid Glass 见[样式/API 索引](references/apple/liquid-glass/index.md)与[动效入口](references/apple/liquid-glass/motion.md)。跨平台基线、自适应能力、语义组件和测试三篇主要覆盖 iOS 与 Android OEM，并非完整 Windows 规范。

### 跨平台图标系统

| 文件 | 内容 |
|---|---|
| [references/cross-platform/cross-platform-interface-icons.md](references/cross-platform/cross-platform-interface-icons.md) | Apple、Google/Material、Windows 原生界面图标库、API、状态与语义对齐 |
| [references/cross-platform/cross-platform-app-icons.md](references/cross-platform/cross-platform-app-icons.md) | Apple Icon Composer、Windows App Icon、Android Adaptive/Play Icon 的设计、适配、工具与验收 |

### Material & Google Design

| 文件 | 内容 |
|---|---|
| [references/android/google-android-map.md](references/android/google-android-map.md) | Android Mobile Design、Material 3 和开发入口的官方深度链接地图 |
| [references/android/material-foundations-styles.md](references/android/material-foundations-styles.md) | 无障碍、内容、Design Token、状态、布局、颜色、字体、elevation、shape、spacing、icon |
| [references/android/material-components-map.md](references/android/material-components-map.md) | Material 3 全组件 overview/guidelines/specs/accessibility 索引 |
| [references/android/material-motion.md](references/android/material-motion.md) | Motion physics、Expressive/Standard、Spatial/Effects、转场和 Web fallback |
| [references/android/android-foldable-adaptation.md](references/android/android-foldable-adaptation.md) | Android 折叠屏与 Adaptive Apps 专项，以及 Apple Duo 语义对齐 |

### Microsoft Design

| 文件 | 内容 |
|---|---|
| [references/windows/microsoft-windows-map.md](references/windows/microsoft-windows-map.md) | Windows Design、WinUI/Windows App SDK、Fluent 2 官方地图 |
| [references/windows/fluent-foundations-components.md](references/windows/fluent-foundations-components.md) | Windows/Fluent 原则、Token、颜色、材质、布局、排版、无障碍和组件索引 |
| [references/windows/microsoft-motion.md](references/windows/microsoft-motion.md) | Windows 原生 Motion 与 Fluent Web Motion 的独立规范 |

### Apple Design

- [Apple 官方覆盖地图](references/apple/apple-docs-coverage.md)
- [Apple 官方深度链接地图](references/apple/apple-official-docs-map.md)
- [HIG Foundations / Patterns](references/apple/hig-foundations-patterns.md)
- [HIG Components / Inputs](references/apple/hig-components-inputs.md)
- [平台、资源、字体和技术品牌](references/apple/platform-resources-technologies.md)
- [Live Activities 实时活动](references/apple/apple-live-activities.md)：四种呈现、跨设备布局、生命周期、APNs、交互、动效和尺寸验收。
- [iPhone Duo 折叠屏适配](references/apple/iphone-duo-adaptation.md)
- [Liquid Glass adoption](references/apple/liquid-glass/liquid-glass-adoption.md)
- [Liquid Glass controls](references/apple/liquid-glass/liquid-glass-controls.md)
- [Liquid Glass API、Motion 与 Color](references/apple/liquid-glass/liquid-glass-api-motion-color.md)
- [Liquid Glass 官方深度链接地图](references/apple/liquid-glass/liquid-glass-deep-link-map.md)

### Apple.com 实现参考

[Web 索引](references/web/index.md)保留原有 Apple 风格哲学、Token、Web 组件、布局、Tailwind 和独立动画资料，不作为 Apple 原生、Android 或 Windows 的默认数值。Web 无障碍可用于一般 Web 项目；PingFang 字体是按需特殊资源。

## 安装

### Codex

```bash
git clone https://github.com/LukeSONG2000/more-than-design-skill.git \
  ~/.codex/skills/more-than-design-skill
```

### Claude Code

```bash
git clone https://github.com/LukeSONG2000/more-than-design-skill.git \
  ~/.claude/skills/more-than-design-skill
```

### 本地开发源与符号链接（可选）

需要共同维护 Codex / Claude 安装时，可在自己的工作区保留唯一源码，再链接标准安装入口。以下为 macOS / Linux 示例；按实际工作区设置 `SOURCE`。若入口已存在，先检查归属并自行备份，不覆盖现有文件；旧 `commands` 路径仅用于已有兼容配置，不是新安装位置。

```bash
SOURCE="$HOME/Workspace/more-than-design/repos/more-than-design-skill"
mkdir -p "$(dirname "$SOURCE")" "$HOME/.codex/skills" "$HOME/.claude/skills"
if [ ! -e "$SOURCE" ] && [ ! -L "$SOURCE" ]; then
  git clone https://github.com/LukeSONG2000/more-than-design-skill.git "$SOURCE"
fi
for TARGET in "$HOME/.codex/skills/more-than-design-skill" "$HOME/.claude/skills/more-than-design-skill"; do
  if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
    printf '保留已有入口，请检查归属：%s\n' "$TARGET"
  elif [ -f "$SOURCE/SKILL.md" ]; then
    ln -s "$SOURCE" "$TARGET"
  fi
done
```

## 字体资源

仓库保留 [refinec/PingFangSC](https://github.com/refinec/PingFangSC) 的 PingFang SC fallback：非 Apple Web 使用 `woff2`，客户端可使用 `ttf`，Apple 设备优先系统字体。详细方案见 [references/web/pingfang-fonts.md](references/web/pingfang-fonts.md)。字体资源只服务 Apple 风格或明确需要统一中文观感的项目，不作为 Android/Windows 默认字体。

## 分发与验证

- 本次集成验证发现 `skill-home v0.2.20 export -p claude` 仅输出 SKILL/scripts，遗漏本结构的 42 篇嵌套 references；该版本不能直接用于本仓的完整导出。这不影响标准 clone／symlink 安装，也不表示其他 CLI 版本行为相同。
- 需要独立导出目录时，使用本仓递归导出脚本（Python 标准库，无需修改全局 CLI）。`--output` 必填，须为源目录之外的新目录；已存在的目标会被拒绝，不覆盖文件。默认 light，排除字体目录与展示图；明确需要完整字体资源时添加 `--include-fonts`。导出不代表安装、上传或发布。

```bash
python3 scripts/export_skill.py --output ../more-than-design-export
```

- 平台资料提供官方来源和核对日期；Live Activities 已于 2026-10-12 对照中英文 HIG 与必要的 ActivityKit/WidgetKit 文档补全。
- 当前结构整理仍使用版本 `1.4.1`，不表示已提交、发布或同步其他安装渠道。
- GitHub 完整仓库保留字体文件与许可证；轻量发布包排除字体二进制、展示图、Git 元数据和本地安装目录。轻量包的字体文档仍保留，使用字体时从完整仓库获取并核对授权。
- 本地结构校验检查 Markdown 链接、锚点、裸文件引用、平台路由和孤立资料，不访问外网。依赖见 [scripts/requirements-validation.txt](scripts/requirements-validation.txt)，从仓库根目录运行以下命令。
- 分发前另运行 `skill-home validate . --strict`、`skill-home scan . --strict` 并检查最终包清单；各安装渠道同步由维护者独立完成，不以源码通过校验替代同步验收。

```bash
python3 -m venv ../.venv-more-than-design-validation
../.venv-more-than-design-validation/bin/python -m pip install -r scripts/requirements-validation.txt
../.venv-more-than-design-validation/bin/python scripts/validate_structure.py
```

## 许可证与归属

代码和原创整理采用 MIT License。Apple、Google、Material、Microsoft、Windows、Fluent 及相关商标、设计资源和文档归各自权利人所有。本项目用于设计学习与开发参考，不代表任何平台官方产品或背书。
