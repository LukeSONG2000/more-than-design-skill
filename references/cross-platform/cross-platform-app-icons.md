# 跨平台 App Icon 设计、适配与交付

本文件处理代表应用本身的图标，包括 Apple Home Screen/Dock、Windows Shell、Android Launcher 和应用商店资产。界面中的操作图标见 [cross-platform-interface-icons.md](cross-platform-interface-icons.md)。

## 1. 先分清四类资产

| 资产 | 作用 | 是否可互相替代 |
|---|---|---|
| 品牌母版 | 定义核心轮廓、颜色、图层和渠道标识 | 只作为派生源，不直接假设可运行 |
| 平台 App Icon | Home Screen、Dock、Launcher、Start、Taskbar 等系统入口 | 必须按平台遮罩、图层和打包格式派生 |
| 商店图标 | App Store / Google Play / Microsoft Store 列表 | 与安装包图标分开验证，不能默认同一导出满足全部要求 |
| 应用内 Logo | 登录页、About、品牌页和 Web favicon | 使用透明品牌 SVG/平台合适资产，不反向消费系统实渲 App Icon |

SF Symbols、Material Symbols 和 Segoe Fluent Icons 是界面图标库，不是应用品牌母版。Apple 明确禁止把 SF Symbol 或近似图形用于 App Icon、Logo 或商标。

## 2. 共享品牌与平台派生

跨平台一致的是识别，不是外框：

- 保留核心轮廓、主要颜色、视觉重心和最关键的品牌特征。
- 为每个平台分别调整构图、安全区、背景、层次和小尺寸细节。
- 不把 Apple 的圆角、Liquid Glass 高光或展平预览图复制到 Windows/Android。
- 不把 Google Play 的 512px 商店图标直接当 Android Adaptive Icon 图层。
- 不把 Windows ICO 或带透明边距的 Dock runtime PNG 反向覆盖品牌母版。
- PROD/BETA/DEV 等渠道可共享主体，但渠道标识、包 ID、资源名和验证清单必须独立，防止跨渠道消费。

推荐源结构：

```text
app-icon/
  source/                 # 品牌矢量、图层和颜色定义
  apple/                  # .icon / asset catalog 输入
  windows/                # MSIX PNG、ICO、manifest mapping
  android/                # adaptive foreground/background/monochrome
  stores/                 # Play/App Store/Store listing exports
  in-app/                 # 透明 SVG 与必要位图派生
  manifest.json           # 源路径、尺寸、渠道、SHA-256 和生成工具版本
  verify.*                # 结构、尺寸、槽位和最终包检查
```

## 3. Apple App Icons

[Apple HIG App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) 以分层、未遮罩的源图作为当前 iOS、iPadOS、macOS 和 watchOS 的主要设计方式。

### 3.1 设计规范

- 使用简洁、易辨识且与产品核心用途相关的图形；不要直接放界面截图或复制标准 UI 控件。
- iOS、iPadOS、macOS、watchOS 提供背景层和一个或多个前景层。保持前景边缘明确，主要内容居中。
- 提供未预先裁圆角的图层：iOS/iPadOS/macOS 使用方形图层，watchOS/visionOS 仍提供方形图层由系统形成圆形，tvOS 使用矩形图层。
- 不在源图层烘焙系统会动态生成的圆角、层间阴影、高光、折射、模糊或 bevel。自定义效果会与系统 Liquid Glass 效果叠加，必须谨慎实测。
- Default、Dark、Clear、Tinted 外观保持同一核心特征，不在不同外观中更换主体导致用户无法识别。
- Dark 以默认版本为基础，避免过亮；Clear/Tinted 要在浅色和深色背景上验证可读性。
- 系统可生成未提供的外观，但品牌关键图标应预览系统生成结果，必要时提供受控变体。
- alternate app icons 仍需与产品相关，并分别满足审核与外观变体要求。

### 3.2 Icon Composer 和 Xcode

[Icon Composer](https://developer.apple.com/icon-composer/) 从一套分层设计生成 iPhone、iPad、Mac 和 Apple Watch 图标，并允许按平台调整 composition：

1. 导入和组织独立图层，不导入已展平的系统实渲截图。
2. 定义背景、图层组合和平台构图。
3. 调整 translucency、refraction、specular highlight 和 shadow；优先系统默认，只做有意图的变化。
4. 逐一预览 iOS/macOS/watchOS 以及 Default、Dark、Mono、Clear、Tinted。
5. 将 `.icon` 文件直接加入 Xcode；扁平导出只用于营销或沟通，不作为原生分层源。
6. 在 Simulator 和真机上验证 Home Screen、App Library、Settings、Spotlight、Dock、Finder 和窗口环境。

tvOS 与 visionOS 的分层图标继续通过 Xcode asset catalog/image stack 配置；不要假设 `.icon` 覆盖所有 Apple 平台。

### 3.3 Apple 工程边界

- `.icon` 是可继续编辑和编译的权威工程；兼容 ICNS/PNG 是派生产物。
- macOS 应用若在运行时设置 Dock 图标，runtime PNG 的边距合同与 `.icon` 图层合同分开。不要把为 Dock 光学对齐而缩放过的 PNG 导回 `.icon`。
- 核对 Xcode target、asset catalog、bundle 信息和最终 `.app`；资源存在于仓库不等于打包链路正在消费。

## 4. Windows App Icons

Windows App Icon 会出现在 Start、All apps、Taskbar、Search、标题栏、通知、Open with、Task Manager、Jump List、Settings 和 Share 等多个位置，因此需要多尺寸、多缩放和多消费槽位。

### 4.1 设计规范

- 用一个简单、清晰、持久的隐喻表达应用核心价值；避免把多个功能堆成拼贴。
- 先在 48x48 网格中校准轮廓、重心和空间利用，再针对小尺寸做 optical correction。
- 使用尽量少的层级和清晰的轮廓。层内阴影可帮助区分对象，但避免过重透视和不必要复杂度。
- 透明背景通常能更自然地适应 Windows 主题；必须使用底板时，为浅色/深色环境提供经过验证的版本。
- Windows 11 不再要求单独的高对比度 App Icon 资产，但图标仍需在高对比度和放大环境下可辨认。

### 4.2 构建与打包

- WinUI/UWP/MSIX 按 manifest 槽位提供 `AppList`、`Square44x44Logo`、`Square150x150Logo`、StoreLogo、SplashScreen 等所需资产，并使用 `scale-*`、`targetsize-*` 和主题限定符。
- Windows 在 125%、150%、250%、300% 等中间缩放选择最接近资源；提供更多原生尺寸可减少系统缩放。
- Win32/WPF/Electron 等链路使用包含多帧的 ICO，并分别核对 EXE、窗口、Taskbar、安装器、卸载器和快捷方式 `IconLocation`。
- Windows 11 不使用旧 Live Tile 呈现，但 Microsoft Store 发布仍可能要求特定 tile/package 资产；以当前 manifest 和发布校验为准。
- 不要只替换网页 favicon 或 public PNG 就宣称桌面 App Icon 已更新。

### 4.3 工具

- [Windows app icon design](https://learn.microsoft.com/windows/apps/design/iconography/app-icon-design)：隐喻、形状、颜色、层次、阴影和透视。
- [App icon construction](https://learn.microsoft.com/windows/apps/design/iconography/app-icon-construction)：尺寸、缩放、manifest 和命名限定符。
- [Visual Studio asset generation](https://learn.microsoft.com/windows/apps/design/iconography/visual-studio-asset-generation)：从源图生成初始资产集。官方也提醒自动缩放不如逐尺寸手工校准。
- Visual Studio Manifest Designer：检查 `Package.appxmanifest` 的 Visual Assets 和生成结果。

## 5. Android App Icons

Android 必须区分 APK/AAB 中的 Launcher Icon 与 Google Play 商店列表图标。

### 5.1 Adaptive Launcher Icon

[Adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive) 由系统/OEM Launcher 应用不同遮罩和动态效果：

- 彩色版本至少有 foreground 和 background 两层，优先使用矢量。
- 支持主题图标时提供 monochrome 单层；Android 13+ 可按壁纸和主题着色。
- 每层画布为 108x108dp；不会被常见遮罩裁切的安全区为居中的 66x66dp。
- 外围每侧 18dp 留给遮罩与 parallax/pulse 等系统效果。
- 主 Logo 建议至少 48x48dp 且不超过 66x66dp。
- 图层边缘清晰，不预加外轮廓 mask 或背景投影。
- 在 `mipmap-anydpi-v26` 的 `<adaptive-icon>` 中声明 background、foreground 和 monochrome。
- `AndroidManifest.xml` 的 `android:icon` 与 `android:roundIcon` 都要指向预期资源；是否共用 adaptive 定义由项目和 OEM 矩阵决定，最终必须检查 merged manifest 和构建包。
- 不为深色模式制作一套预渲染的 `-night` 品牌 Launcher Icon。主题图标由 monochrome 和 Launcher 负责；品牌彩色版在明暗模式保持身份一致。

### 5.2 Google Play 商店图标

[Google Play icon specification](https://developer.android.com/distribute/google-play/resources/icon-design-specifications) 只针对商店列表，不是 Launcher Icon：

- 512x512px、32-bit PNG、sRGB、最大 1024KB。
- 上传完整正方形；Google Play 动态应用约为图标尺寸 20% 的圆角和外部阴影。
- 不预先裁圆角，不添加外部投影。可以保留图形内部有意义的光影。
- 品牌图形按 keyline 光学放置，不强制把有明确轮廓的 Logo 拉伸成全出血。
- 尽量使用合适的品牌背景而不是透明底，避免透出 Play UI 背景。
- 不使用排名、优惠、安装诱导、Play 计划或其他误导性文字/标识。

### 5.3 Android Studio 工具

[Image Asset Studio](https://developer.android.com/studio/write/create-app-icons) 可生成 Adaptive + Legacy Launcher Icon 和通知图标：

- Launcher 选择 foreground/background，预览不同 mask，并输出密度和 API 版本资源。
- 通知图标是独立的单色资产，不应直接缩小彩色 Launcher Icon。
- Clip Art 可使用 Material 图标，但品牌 App Icon 应使用自己的品牌源。
- 自动生成后仍需检查安全区、monochrome、round slot、资源名和最终 APK/AAB，不能只验收 IDE 预览。

## 6. 跨平台派生矩阵

| 共享输入 | Apple 输出 | Windows 输出 | Android 输出 |
|---|---|---|---|
| 核心品牌矢量和图层 | `.icon` / asset catalog layers | MSIX 多尺寸 PNG + 多帧 ICO | adaptive foreground/background/monochrome |
| 平台构图 | Icon Composer per-platform composition | 48 grid + 小尺寸 optical correction | 108dp canvas + 66dp safe zone |
| 外形 | 系统圆角/圆形/平台 mask | Shell/资产本身与透明底策略 | OEM Launcher mask |
| 明暗与个性化 | Default/Dark/Clear/Tinted | theme-qualified assets 或透明底 | 彩色恒定 + monochrome themed icon |
| 商店资产 | App Store/Xcode 流程 | StoreLogo/Store listing | 独立 512px Play PNG |
| 应用内品牌 | 透明 SVG/平台图像，不用实渲 App Icon | 同左 | 同左 |

不要要求三端图标的实际像素边界相同。验收品牌轮廓、视觉重心、色彩识别和各平台上的光学尺寸。

## 7. 可复现的资产流程

1. 锁定品牌母版和渠道映射；记录源文件、颜色、图层和 SHA-256。
2. 每个平台只从母版或明确的平台源工程派生，禁止从另一平台的展平产物二次生成。
3. 生成产物清单，包含尺寸、格式、alpha bounds、资源名、目标槽位和工具版本。
4. 运行结构验证：尺寸、色域、文件大小、图层、安全区、ICO frames、manifest/asset catalog 引用。
5. 运行打包验证：读取最终 `.app`、MSIX/EXE/installer、APK/AAB merged manifest 和资源表。
6. 运行实际界面验证，不把构建成功或仓库存在文件当成视觉验收。
7. App Icon、应用内 Logo、Web favicon 和商店图标分别记录通过/未覆盖。

## 8. 最终表面验收

| 平台 | 至少检查 |
|---|---|
| iOS/iPadOS | Home Screen、App Library、Spotlight、Settings、浅/深/清透/着色外观、不同壁纸 |
| macOS | Dock、Finder、Launchpad、About、浅/深色、运行时 Dock 更新与打包应用一致性 |
| Windows | Start、All apps、Taskbar、Search、窗口、Explorer、通知、安装器、卸载器、快捷方式；100%-400% 代表缩放 |
| Android | 多种 OEM mask、标准/圆形入口、themed icon 开关、浅/深壁纸、Recents、Splash、低版本 fallback |
| 商店 | App Store / Microsoft Store / Google Play 独立预览、政策和上传校验 |

测试报告必须区分：源资产正确、生成产物正确、配置引用正确、最终包正确、真机/实机表面正确。任一项通过都不能替代其余门禁。

## 9. 常见错误

- 把 SF Symbol、Material Symbol 或 Segoe glyph 当应用 Logo。
- 把 Apple Icon Composer 展平预览图用于 Android/Windows 或应用内 Logo。
- 给 Apple/Android 源图预裁圆角或烘焙系统阴影。
- 只替换源码图片，不检查 target、manifest、EXE、shortcut 或最终包。
- Android 将 Play 512px 图标与 Adaptive Icon 混为同一资产。
- Android 标准槽、round slot、monochrome 或渠道资源指向错误。
- Windows 只提供一个大 PNG，由系统机械缩放全部尺寸。
- 通过截图判断实现正确，却未记录主题、DPI、Launcher、设备和包版本。

## 10. 官方来源

- Apple [App icons HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons)
- Apple [Icon Composer](https://developer.apple.com/icon-composer/)
- Apple [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)
- Apple [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)
- Microsoft [App icons](https://learn.microsoft.com/windows/apps/design/iconography/app-icons)
- Microsoft [App icon design](https://learn.microsoft.com/windows/apps/design/iconography/app-icon-design)
- Microsoft [App icon construction](https://learn.microsoft.com/windows/apps/design/iconography/app-icon-construction)
- Microsoft [Visual Studio asset generation](https://learn.microsoft.com/windows/apps/design/iconography/visual-studio-asset-generation)
- Android [Adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive)
- Android [Create app icons / Image Asset Studio](https://developer.android.com/studio/write/create-app-icons)
- Google Play [Icon design specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications)

