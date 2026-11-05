# Web 组件地图

这是按任务组织的检索地图，不是“所有组件已实现”的目录。下面条目为场景级覆盖；浮层、反馈、表单、搜索和列表详情已在[重点交互模式](interaction-patterns.md)细化，其余实施前需读取对应官方文档。专业能力目前只提供选型入口。

## 导航、组织和操作

| 口语 / 中英文名称 | 适用 | 不要混用 |
|---|---|---|
| 去另一页 / Link 链接 | 导航，有真实地址，支持新标签页 | Button 用于动作，不用可点击 div 替代 |
| 执行 / Button 按钮、Icon button 图标按钮 | 提交、保存、触发操作；图标有可访问名称 | 不把导航伪装成无地址按钮 |
| 左边栏目 / Sidebar、Navigation rail | 产品级目的地 | 侧栏不必是模态 Drawer |
| 上一级路径 / Breadcrumb 面包屑 | 层级位置与祖先导航 | 不当作时间历史或流程进度 |
| 切换一块内容 / Tabs 标签页 | 同一语境下互斥内容面板 | 跳路由用导航；数据选项选择用 Radio/Select |
| 展开更多 / Disclosure、Accordion 折叠面板 | 次级详情、分组展开 | 不隐藏当前错误、关键操作 |
| 按步骤完成 / Stepper、Wizard 向导 | 真正有顺序或依赖的多步任务 | 简单表单不强制分步；步骤状态不是进度百分比 |
| 一排操作 / Toolbar 工具栏 | 相关高频命令 | 装饰按钮组不自动赋予 toolbar 角色 |
| 三个点、右键 / Menu、Context menu | 对象命令、操作选择 | 网页导航列表不默认使用 menu 角色；触摸有可见替代 |
| 快速命令 / Command palette | 搜索并执行命令或导航 | 与普通全文搜索分清结果语义 |

## 输入和选择

| 口语 / 中英文名称 | 适用 | 边界 |
|---|---|---|
| 填一项 / Text field、Textarea | 短文本或多行文本 | 保留 label，不用 placeholder 独自说明 |
| 多选勾选 / Checkbox | 独立布尔项、多选、批量全选的混合态 | 不用 Switch 表示待提交的多选清单 |
| 选一个 / Radio group | 少量互斥选项，需要同时比较 | 选项多才考虑 Select |
| 立刻开关 / Switch | 可理解的二元开关 | 保存时才生效需明确提交语义 |
| 下拉选项 / Select | 有限单选集合；原生 select 可满足时优先评估 | 不等同命令菜单 |
| 边输入边找 / Combobox、Autocomplete | 搜索候选、远程补全 | 区分只选已有值与允许自由输入，处理无结果和过期请求 |
| 选多项标签 / Multiselect、Token input | 多实体选择，可移除 | Chip 可能只展示状态，不天然可交互 |
| 拖动数值 / Slider、Range slider | 连续范围、近似探索 | 精确数值保留数字输入；验证上下界与步长 |
| 加减数量 / Number input、Stepper input | 精确数量和边界 | 不与流程 Stepper 混淆 |
| 选时间 / Date picker、Date range、Time picker | 日期、区间、日程 | 处理键盘输入、时区、语言、无效区间；不默认引入复杂日历 |
| 拖文件进来 / File input、Dropzone、Upload queue | 文件选择和上传任务 | 拖放之外保留选择按钮、取消、重试和校验 |
| 编辑格式 / Rich text editor、Code editor | 结构化内容或代码 | 专业库；纯备注优先 Textarea |

## 浮层与反馈

| 口语 / 中英文名称 | 适用 | 边界 |
|---|---|---|
| 中间弹窗 / Dialog | 独立短任务 | Modal 描述阻断背景的行为，不是外形名 |
| 危险确认 / Alert dialog | 重要消息需要立即决定 | Esc/取消不执行危险操作；并非必须禁用 Esc |
| 从边上出来 / Drawer、Sheet | 侧边或底部容器 | 位置不能决定模态性；不同库同名行为可能不同 |
| 底下拉起来 / Bottom sheet | 触摸主导的上下文任务 | 不固定 30/60/80%，不等同所有 Drawer |
| 按钮旁小面板 / Popover | 锚定的短内容或编辑 | HTML popover 不自动具备菜单或对话框语义 |
| 悬停解释 / Tooltip | 简短补充，键盘也可触达 | 不装交互表单，不作为必要说明唯一入口 |
| 悬停预览 / Hover card | 可选上下文预览 | 触屏有点击替代，必要内容仍可直接访问 |
| 操作成功 / Toast、Snackbar | 非阻断反馈；后者常带操作 | 术语因库而异；重要结果不能只靠短暂提示 |
| 持续提醒 / Banner、Inline alert | 页级或区块级问题 | 按紧迫性选择播报，不把全部消息设为 assertive |
| 字段下报错 / Field error | 输入错误持续定位 | 关联字段，修正后清除；不定时消失 |

## 数据、布局和任务状态

| 口语 / 中英文名称 | 适用 | 边界 |
|---|---|---|
| 一行行记录 / List、Table | 浏览记录、跨行比较精确数据 | 静态表格不加复杂 grid 键盘模型 |
| 像表格软件 / Data grid | 单元格编辑、范围选择、密集操作 | 选用成熟库并验证虚拟化/焦点/授权 |
| 文件层级 / Tree、Treegrid | 真层级与展开导航、层级表格 | 扁平集合不要人为嵌套 |
| 卡片列表 / Card collection | 视觉对象和少量摘要 | 不把所有页面区块套卡片，密集比较优先表格 |
| 看趋势 / Chart、KPI、Sparkline | 趋势、构成、关键数值 | 单位、基线、摘要与可访问数据；颜色不独自编码 |
| 翻页 / Pagination、Load more、Infinite feed | 有界结果、连续浏览 | 精确定位与返回恢复常适合分页；无限滚动要能到页脚 |
| 看板 / Kanban | 工作阶段与流转 | 拖动必须有非拖动替代和权限/失败回滚 |
| 日程 / Calendar、Timeline | 时间定位与跨度 | 与日期选择器分开，专业交互另行核验 |
| 一边列表一边详情 / Master-detail、Split pane | 持续比较、编辑与上下文保留 | 窄屏转页或面板，不能丢草稿 |
| 加载中 / Skeleton、Spinner、Progress | 初始占位、短等待、可测进度 | 未知进度不伪造百分比，Skeleton 预留稳定布局 |
| 没数据 / Empty state、No results | 初次使用、空集合、无筛选结果 | 区分加载、无权限和失败；给适当恢复动作 |
| 操作失败 / Error state、Retry | 可恢复失败、离线 | 说明影响，重试不重复扣款或重复提交 |
| AI 对话 / Conversation、Composer、Streaming result | 对话、生成、工具执行 | 区分生成与执行成功，提供停止、失败恢复和必要的操作确认 |

## 官方查找入口

核对日期：2026-11-03。以下是行为和实现检索入口，地图中的场景推荐为本 skill 归纳，不表示这些来源逐条规定相同选型。

- [APG Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/)：语义、焦点和键盘模式。
- [React Aria](https://react-aria.adobe.com/)：无样式行为组件与国际化。
- [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction)：原语、复合组件和行为契约。
- [shadcn/ui Components](https://ui.shadcn.com/docs/components)：可维护源码的组件与组合模式；读取所选组件实际底层依赖，不假定全部相同。
- [Ant Design](https://ant.design/components/overview/)：企业 Web 组件入口。
- [LearnUI](https://learnui.qiaomu.ai/)：视觉术语发现。不可将示例尺寸或 Prompt 当作通用规范。
