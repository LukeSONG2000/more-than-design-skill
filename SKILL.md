---
name: more-than-design-skill
description: Use with frontend-design for platform-aware UI across Android/Material, Windows/Fluent, Apple/HIG, and context-sensitive web; keep native behavior, visual style, and motion distinct.
license: MIT
version: 1.5.0
author: LukeSONG2000
category: productivity
tags:
  - frontend
  - docs
  - planning
  - analysis
metadata:
  version: 1.5.0
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

先确认目标平台、输入方式、窗口形态、技术栈及已有设计体系。只打开目标平台索引，再从索引选择当前任务需要的样式、组件、行为或动效文档。

| 目标 | 入口 | 范围 |
|---|---|---|
| Android | [Android / Material](references/android/index.md) | 原生组件、自适应窗口、折叠屏；样式与动效独立 |
| Windows | [Windows / Fluent](references/windows/index.md) | WinUI、桌面输入和窗口；原生与 Fluent Web 分别核对 |
| Apple 原生 | [Apple / HIG](references/apple/index.md) | 原生 HIG、系统能力、独立动效与 Liquid Glass 专项 |
| Web | [Web](references/web/index.md) | 先服从项目语境；Apple 风格 Web 参考不等于 Apple 原生或通用标准 |
| 选择平台、共享语义或图标映射 | [跨平台](references/cross-platform/index.md) | 只加载任务相关映射；移动端基线主要覆盖 iOS 与 Android |

Web 不固定套用一个体系。现有品牌、组件库和工作流优先；语境相同且无其他约束时，消费内容与创意产品偏向 Apple，企业生产力与桌面密集工作流偏向 Fluent，移动优先与动态主题偏向 Material。完整冲突处理仅在需要时读跨平台索引中的平台路由。

## 实施约束

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
