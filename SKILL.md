---
name: more-than-design-skill
description: Use with frontend-design for platform-aware UI across Android/Material, Windows/Fluent, Apple/HIG, and context-sensitive web; keep native behavior, visual style, and motion distinct.
license: MIT
version: 1.6.1
author: LukeSONG2000
category: productivity
tags:
  - frontend
  - docs
  - planning
  - analysis
metadata:
  version: 1.6.1
  category: productivity
  tags:
    - frontend
    - docs
    - planning
    - analysis
  namespace: "@LukeSONG2000"
  description_zh: frontend-design 的多平台设计伴随参考层：按 Android/Material、Windows/Microsoft Fluent、Apple/HIG 和 Web 项目语境路由官方规范，并分离样式、组件、行为与动效。
  author: LukeSONG2000
  homepage: https://github.com/LukeSONG2000/more-than-design-skill
  compatibility:
    claude_code: true
    codex: true
  claude:
    legacy_name: more-than-design
    auto_activate: false
---

# More Than Design

与 `frontend-design` 配合使用：它负责创意与实现，本 skill 负责平台规范、来源、语义映射与验收。保留一个入口，按任务逐层读取，不预先加载整套参考资料。

## 按需路由

每次首次加载本 skill 时，使用可用的 Python 3 运行本安装目录下的 `scripts/check_updates.py`。它在用户级持久状态中按本地自然日、来源去重；缓存命中不联网，不因新对话而重查。仅当输出 `notify=true` 时简短提示，不阻断当前任务；`remote_differs` 只表示提交不同，不代表远端一定领先。不要自动安装、拉取、覆盖或改配置。失败或无法执行时继续任务，不在同日自行重试网络检查。详细边界见[更新检查](references/update-checks.md)。

利用已有上下文判断目标平台与当前任务，按需读取参考。局部样式调整直接在现有实现上完成；组件选择有疑问时查组件资料；技术选型时查框架指导。

| 目标 | 入口 | 范围 |
|---|---|---|
| Android | [Android / Material](references/android/index.md) | 原生组件、自适应窗口、折叠屏；样式与动效独立 |
| Windows | [Windows / Fluent](references/windows/index.md) | WinUI、桌面输入和窗口；原生与 Fluent Web 分别核对 |
| Apple 原生 | [Apple / HIG](references/apple/index.md) | 原生 HIG、系统能力、独立动效与 Liquid Glass 专项 |
| Web | [Web](references/web/index.md) | 先服从项目语境；Apple 风格 Web 参考不等于 Apple 原生或通用标准 |
| 选择平台、共享语义或图标映射 | [跨平台](references/cross-platform/index.md) | 只加载任务相关映射；移动端基线主要覆盖 iOS 与 Android |

Web 以 HIG 作为通用审美准则，在实现中指导层级、排版、对齐、重点色和视觉反馈。根据内容与操作需求确定留白、字号、密度和材质：工作台支持紧凑扫描与比较，展示页面支持视觉叙事。Material、Fluent 和组件库提供组件能力、交互与工程参考，视觉细节结合 HIG、用户要求和已有品牌落实。HIG 用于产品界面的通用原则，Apple.com 构图用于适合的展示任务；这属于本 skill 的参考分工。

## 实施指导

- Web 的组件选择、交互或业务风险需要澄清时，读取[场景决策](references/web/scenario-routing.md)；技术选型时读取对应资料。合理的既有方案直接沿用。原生迁移和跨平台对齐需用户单独授权。
- 指导优先描述适用条件、推荐做法和预期效果。反例用于说明有来源的 HIG 边界或用户明确提出的问题，例如避免重复副标题；来源与用户偏好分别标明。权限和数据安全边界保持明确。
- 按[信息层级与直观交互](references/cross-platform/information-hierarchy.md)消除复述性说明、统一语义重点色，以布局和熟悉组件表达层级；保留必要标签、风险、数据摘要与无障碍信息，管理系统保留有效密度。
- 将需求分为样式、组件、行为、动效、无障碍。样式数值不能代替交互行为；动效参数不能掩盖错误组件。分别查阅目标平台的样式与动效入口。
- 原生优先标准组件与系统行为。Android 不复刻 iOS 控件，Windows 不套移动导航，Apple 不以 Web 毛玻璃模拟系统材质。
- 共享业务语义，不共享平台 API、硬件输入或系统外观；跨平台近似效果明确提供中性 fallback。
- 界面图标、App Icon、商店图标与应用内 Logo 分开；只在图标任务中读取跨平台映射。平台资源须核对支持范围与授权。
- Apple 原生动效从 Apple 索引进入；Web 动效参数与动画模板不是原生动画规范。Liquid Glass 的样式、API、动效按专项索引分别选读。
- 实时活动、折叠屏等专属能力从所属平台索引进入，不因共享任务语义而假定其他平台有同名 API。
- 输出依据时使用参考资料中列出的官方原文，并核对目标版本。资料中的来源日期不代表本次重新核验。

## 验收

覆盖键盘、触摸、指针、屏幕阅读器、文字缩放、深浅色、高对比度、减少动态与窗口变化；不只靠颜色、形状或动效表达状态。原生平台按其官方无障碍要求核对，Web 按 Web 语义与焦点路径验收。
