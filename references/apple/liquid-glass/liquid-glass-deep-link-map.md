# Liquid Glass Deep Link Map

Use this reference when a task needs to explore Liquid Glass beyond the main adoption pages: related HIG pages, SwiftUI/UIKit/AppKit APIs, navigation surfaces, scroll-edge behavior, background extension, button styles, icon/widget implications, or platform-specific boundaries.

Read order:

1. `liquid-glass-adoption.md` for the strategy and cross-platform boundary.
2. `liquid-glass-controls.md` for control design decisions.
3. `liquid-glass-api-motion-color.md` for implementation recipes.
4. This file when you need to know which official Apple link to open next and how to classify it.

## Crawl Scope

Snapshot: 2026-07-14.

Source method: official Apple Developer/HIG pages and Apple documentation markdown endpoints, starting from:

- HIG Materials, especially Liquid Glass and Standard materials.
- HIG Color, especially Liquid Glass color and System colors.
- HIG Scroll views, Toolbars, Sidebars, Tab bars, Buttons, App icons, Icons, SF Symbols, Dark Mode, Accessibility.
- Technology overview: Liquid Glass and Adopting Liquid Glass.
- SwiftUI Landmarks Liquid Glass article and linked Landmarks subtopics.
- SwiftUI, UIKit, and AppKit APIs linked from the adoption and custom-view pages.

Classification rule:

- **Primary**: page directly defines Liquid Glass, its behavior, or its APIs.
- **Design support**: page is not only about glass, but changes how glass should be used in frontend design.
- **Implementation support**: API page needed for platform implementation or fallback.
- **Apple-specific**: useful as Apple platform knowledge, but do not generalize to cross-platform UI.
- **Low signal**: page mentions glass only through shared metadata, card thumbnails, or unrelated examples; route through the normal HIG category instead.

## Quick Routing

| Need | Open these official pages | Then use local refs |
|---|---|---|
| Decide whether glass belongs in the UI | HIG Materials, Adopting Liquid Glass | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| Pick regular vs clear glass | HIG Materials, `Glass.regular`, `Glass.clear` | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| Add custom glass to a SwiftUI control | Applying Liquid Glass to custom views, `glassEffect`, `GlassEffectContainer` | [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| Use native Liquid Glass tab navigation | Adopting Liquid Glass navigation, `UITabBar`, `UITabBarItem` | [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| Use native Liquid Glass segmented selection | Adopting Liquid Glass controls, HIG Segmented controls, `UISegmentedControl` | [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| Use native Liquid Glass menu transitions | `UIButtonConfiguration.glassButtonConfiguration`, `UIButton.menu`, `UIMenu`, WWDC25 Meet Liquid Glass, WWDC25 What's new in UIKit | [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| Match Apple's SwiftUI `View styles` Liquid Glass list | SwiftUI View styles, Styling views with Liquid Glass group | [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| Design toolbar/tab/sidebar glass | HIG Toolbars, Tab bars, Sidebars, Adopting Liquid Glass navigation/toolbars | [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| Protect readability while scrolling | HIG Scroll views, `scrollEdgeEffectStyle`, `safeAreaBar`, UIKit/AppKit scroll edge APIs | [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| Extend media under a sidebar/inspector | Adopting Liquid Glass navigation, Landmarks background extension, `backgroundExtensionEffect`, UIKit/AppKit background extension views | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| Tune color and Dark Mode | HIG Color, HIG Dark Mode, semantic color APIs | 原生：[Liquid Glass 采用策略](liquid-glass-adoption.md)、[颜色与深色模式](liquid-glass-api-motion-color.md#color-and-dark-mode)；仅 Web 可选：[Apple 风格 Token](../../web/apple-style-tokens.md) |
| Separate Apple-only from transferable | Platform considerations in Adopting Liquid Glass, HIG platform docs | [apple-official-docs-map](../apple-official-docs-map.md), [platform-resources-technologies](../platform-resources-technologies.md), this file |

## Primary Liquid Glass Links

| Official page | Category | Cross-platform use |
|---|---|---|
| https://developer.apple.com/documentation/technologyoverviews/liquid-glass | Primary overview | Use as the top-level concept map: hierarchy, harmony, consistency, Landmarks, HIG, videos |
| https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass | Primary adoption guide | Audit controls, navigation, toolbars, windows, modals, layout, search, platforms, performance |
| https://developer.apple.com/cn/design/human-interface-guidelines/materials#Liquid-Glass | Primary HIG material rule | Treat glass as a functional layer for controls/navigation; do not use it as content decoration |
| https://developer.apple.com/design/human-interface-guidelines/materials#Standard-materials | Design support | Use standard materials for content-layer structure under Liquid Glass |
| https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color | Design support | Tint sparingly; prefer one prominent material-tinted action; test against resting content |
| https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views | Primary implementation guide | Custom shapes, interactivity, containers, unions, morph transitions, performance |
| https://developer.apple.com/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass | Primary case study | Extract real placement patterns: sidebar content, toolbar grouping, custom badges, app icon layers |

## SwiftUI View Styles Coverage

Apple's SwiftUI `View styles` page contains a `Styling views with Liquid Glass` group. If the user provides a screenshot of that group, verify against this matrix.

| Screenshot item | Official URL | Covered locally | Note |
|---|---|---|---|
| View styles | https://developer.apple.com/documentation/swiftui/view-styles | This file, [apple-official-docs-map](../apple-official-docs-map.md) | Top-level SwiftUI page; use as an index, not as implementation guidance by itself |
| Applying Liquid Glass to custom views | https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Main custom Liquid Glass implementation article |
| Landmarks: Building an app with Liquid Glass | https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Case study for background extension, toolbar grouping, badges, app icon layers |
| `glassEffect(_:in:)` | https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:) | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Applies glass to a view; default shape is `DefaultGlassEffectShape` |
| `glassEffectID(_:in:)` | https://developer.apple.com/documentation/swiftui/view/glasseffectid(_:in:) | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Stable identity for morphing effects |
| `glassEffectTransition(_:)` | https://developer.apple.com/documentation/swiftui/view/glasseffecttransition(_:) | [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Associates transition behavior with glass effects |
| `glassEffectUnion(id:namespace:)` | https://developer.apple.com/documentation/swiftui/view/glasseffectunion(id:namespace:) | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Combines related effects into a shared resting material shape |
| `interactive(_:)` | https://developer.apple.com/documentation/swiftui/glass/interactive(_:) | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Configures glass for touch/pointer reaction |
| `GlassEffectContainer` | https://developer.apple.com/documentation/swiftui/glasseffectcontainer | [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Groups multiple glass shapes and enables morphing/performance optimization |
| `GlassEffectTransition` | https://developer.apple.com/documentation/swiftui/glasseffecttransition | [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Defines add/remove transition behavior |
| `GlassButtonStyle` | https://developer.apple.com/documentation/swiftui/glassbuttonstyle | [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Concrete style type behind standard glass buttons; prefer `.buttonStyle(.glass)` in guidance |
| `GlassProminentButtonStyle` | https://developer.apple.com/documentation/swiftui/glassprominentbuttonstyle | [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Concrete prominent style type; prefer `.buttonStyle(.glassProminent)` and one primary action |
| `DefaultGlassEffectShape` | https://developer.apple.com/documentation/swiftui/defaultglasseffectshape | [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), [liquid-glass-deep-link-map](liquid-glass-deep-link-map.md) | Default glass effect shape; Apple defines it as a capsule |

Coverage rule: when an item is a concrete SwiftUI type (`GlassButtonStyle`, `GlassProminentButtonStyle`, `DefaultGlassEffectShape`), keep it in API routing. For cross-platform work, translate the behavior and constraints rather than naming the type as a design-system requirement.

## HIG Design Support Links

| Page | Why it matters for Liquid Glass | Route |
|---|---|---|
| https://developer.apple.com/design/human-interface-guidelines/color | Glass can inherit background color and must work in light, dark, and increased contrast contexts | 原生：[采用策略](liquid-glass-adoption.md)、[颜色与深色模式](liquid-glass-api-motion-color.md#color-and-dark-mode)；仅 Web 可选：[Apple 风格 Token](../../web/apple-style-tokens.md) |
| https://developer.apple.com/design/human-interface-guidelines/dark-mode | Glass is adaptive; custom colors need light/dark/high-contrast variants | 原生：[颜色与深色模式](liquid-glass-api-motion-color.md#color-and-dark-mode)；仅 Web 可选：[Apple 风格 Token](../../web/apple-style-tokens.md) |
| https://developer.apple.com/design/human-interface-guidelines/accessibility | Reduced transparency, increased contrast, reduced motion, VoiceOver labels | [accessibility](../../web/accessibility.md), [liquid-glass-adoption](liquid-glass-adoption.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| https://developer.apple.com/design/human-interface-guidelines/scroll-views | Defines scroll-edge effects for content moving behind floating controls | [hig-components-inputs](../hig-components-inputs.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md), this file |
| https://developer.apple.com/design/human-interface-guidelines/toolbars | Toolbars adopt glass; group related actions; prefer standard components and concentric custom corners | [hig-components-inputs](../hig-components-inputs.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| https://developer.apple.com/design/human-interface-guidelines/tab-bars | Tab bars float above content, can use glass, and need color contrast against content | [hig-components-inputs](../hig-components-inputs.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| https://developer.apple.com/design/human-interface-guidelines/sidebars | Sidebar glass needs legible content and may use background extension for adjacent media | [hig-components-inputs](../hig-components-inputs.md), [platform-resources-technologies](../platform-resources-technologies.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| https://developer.apple.com/design/human-interface-guidelines/buttons | Button color/background collisions matter more when controls sit on glass | [apple-style-components](../../web/apple-style-components.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| https://developer.apple.com/design/human-interface-guidelines/sheets | Inset/rounded sheets can show content peeking through; task focus may require more opacity | [hig-components-inputs](../hig-components-inputs.md), [liquid-glass-controls](liquid-glass-controls.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| https://developer.apple.com/design/human-interface-guidelines/action-sheets | Action sheets originate from invoking controls; map to anchored contextual menus on Web | [hig-components-inputs](../hig-components-inputs.md), [liquid-glass-controls](liquid-glass-controls.md) |
| https://developer.apple.com/design/human-interface-guidelines/lists-and-tables | Content-layer surfaces need padding/row rhythm, not permanent glass backgrounds | [hig-foundations-patterns](../hig-foundations-patterns.md), [hig-components-inputs](../hig-components-inputs.md), [liquid-glass-api-motion-color](liquid-glass-api-motion-color.md) |
| https://developer.apple.com/design/human-interface-guidelines/app-icons | Liquid Glass-era app icons are layered and dynamic; Apple-specific export flow | [platform-resources-technologies](../platform-resources-technologies.md), [liquid-glass-adoption](liquid-glass-adoption.md), [cross-platform-app-icons](../../cross-platform/cross-platform-app-icons.md), this file |
| https://developer.apple.com/design/human-interface-guidelines/icons | Toolbars/menus should use clear standard icons and accessible labels | [hig-foundations-patterns](../hig-foundations-patterns.md), [hig-components-inputs](../hig-components-inputs.md), [liquid-glass-controls](liquid-glass-controls.md) |
| https://developer.apple.com/design/human-interface-guidelines/sf-symbols | Apple-only symbol resource; use native semantic mappings off Apple platforms | [platform-resources-technologies](../platform-resources-technologies.md), [cross-platform-interface-icons](../../cross-platform/cross-platform-interface-icons.md) |

Low-signal examples: HIG input pages can mention glass through page-level related cards, but if the page's main topic is gestures, game controllers, or generic touch behavior, keep it in `../hig-components-inputs.md` unless the task is explicitly about glass overlays for those inputs.

## SwiftUI API Map

| API/page | Use | Cross-platform translation |
|---|---|---|
| https://developer.apple.com/documentation/SwiftUI/View/glassEffect(_:in:) | Apply glass behind a view inside a shape | One composited glass surface after final padding/shape styles |
| https://developer.apple.com/documentation/swiftui/defaultglasseffectshape | Default shape for glass effects | Capsule/pill default; change shape only when the component geometry needs it |
| https://developer.apple.com/documentation/SwiftUI/Glass | Variant namespace | Material token family |
| https://developer.apple.com/documentation/SwiftUI/Glass/regular | Readable default glass | Default translucent control material |
| https://developer.apple.com/documentation/SwiftUI/Glass/clear | Highly translucent media glass | Use only over rich media; add dimming for bright backgrounds |
| https://developer.apple.com/documentation/SwiftUI/Glass/interactive(_:) | Touch/pointer reaction | Press/hover/focus feedback on custom glass controls |
| https://developer.apple.com/documentation/SwiftUI/GlassEffectContainer | Group multiple glass shapes and improve rendering | Shared wrapper/layer for related glass controls |
| https://developer.apple.com/documentation/SwiftUI/View/glassEffectUnion(id:namespace:) | Merge multiple resting shapes | Shared background spanning related controls |
| https://developer.apple.com/documentation/SwiftUI/View/glassEffectID(_:in:) | Stable identity for morphs | Matched-element IDs in animation code |
| https://developer.apple.com/documentation/SwiftUI/GlassEffectTransition | Entry/exit transition model | Matched geometry for nearby elements; materialize/fade for distant elements |
| https://developer.apple.com/documentation/SwiftUI/View/glassEffectTransition(_:) | Apply a transition to a glass effect | Pair add/remove states with stable IDs |
| https://developer.apple.com/documentation/SwiftUI/PrimitiveButtonStyle/glass | Standard glass button | Prefer native/design-system button before custom blur |
| https://developer.apple.com/documentation/SwiftUI/PrimitiveButtonStyle/glassProminent | Prominent glass button | One prominent action per local group |
| https://developer.apple.com/documentation/SwiftUI/PrimitiveButtonStyle/glass(_:) | Configurable glass button style | Custom variant only after hierarchy and contrast checks |
| https://developer.apple.com/documentation/swiftui/glassbuttonstyle | Concrete standard glass button style type | Document API parity; guide implementers to the semantic `.glass` style |
| https://developer.apple.com/documentation/swiftui/glassprominentbuttonstyle | Concrete prominent glass button style type | Document API parity; keep prominent glass scarce |
| https://developer.apple.com/documentation/SwiftUI/Material | Standard material, not Liquid Glass | Content-layer blur/vibrancy fallback |

### SwiftUI Navigation And Layout

| API/page | Use | Cross-platform translation |
|---|---|---|
| https://developer.apple.com/documentation/SwiftUI/View/scrollEdgeEffectStyle(_:for:) | Configure scroll edge readability | Use a top/bottom scrim or blur edge where content scrolls under chrome |
| https://developer.apple.com/documentation/SwiftUI/ScrollEdgeEffectStyle | Scroll edge style family | Automatic first; hard for dense controls; soft only after testing |
| https://developer.apple.com/documentation/SwiftUI/View/safeAreaBar(edge:alignment:spacing:content:) | Place custom bars in safe areas | Sticky safe-area-aware toolbars |
| https://developer.apple.com/documentation/SwiftUI/View/backgroundExtensionEffect() | Extend media under sidebar/inspector | Mirror/blur adjacent media, not readable content |
| https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable | Let tab navigation become sidebar | Responsive top-level nav: bottom tabs on phone, sidebar on tablet/desktop |
| https://developer.apple.com/documentation/SwiftUI/TabBarMinimizeBehavior | Let tab bar recede on scroll | Collapsible bottom nav only when recovery is obvious |
| https://developer.apple.com/documentation/SwiftUI/TabView | Top-level tabs | Keep primary navigation separate from content layer |
| https://developer.apple.com/documentation/SwiftUI/NavigationSplitView | Sidebar/detail/inspector layout | Multi-pane enterprise layouts with responsive columns |
| https://developer.apple.com/documentation/SwiftUI/View/inspector(isPresented:content:) | Inspector side panel | Contextual detail side panel, not a generic modal |
| https://developer.apple.com/documentation/SwiftUI/ToolbarSpacer | Split toolbar groups | Use fixed gaps between related action groups |
| https://developer.apple.com/documentation/SwiftUI/SpacerSizing/fixed | Fixed toolbar spacing | Keep grouped controls visually separate |
| https://developer.apple.com/documentation/SwiftUI/ToolbarContent/hidden(_:) | Hide toolbar item itself | Avoid empty invisible controls in toolbars |
| https://developer.apple.com/documentation/SwiftUI/Shape/rect(corners:isUniform:) | Corner shape API | Concentric rounding in nested controls |
| https://developer.apple.com/documentation/SwiftUI/ConcentricRectangle | Concentric container/control geometry | Radius should relate to container/window shape |

### SwiftUI Search And Focus

| API/page | Use | Cross-platform translation |
|---|---|---|
| https://developer.apple.com/documentation/SwiftUI/TabView | Contains semantic search tabs in tab navigation | Put search in the expected nav region by device class |
| https://developer.apple.com/documentation/SwiftUI/View/focusable(_:) | tvOS/focusable custom controls | Only use focus-glass behavior for TV/kiosk/keyboard contexts |
| https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/isFocused | Focus state | Drive subtle focus rings/states, not pointer-only hover |

## UIKit API Map

| API/page | Use | Cross-platform translation |
|---|---|---|
| https://developer.apple.com/documentation/UIKit/UIGlassEffect | UIKit custom Liquid Glass effect | Custom native-client glass only; do not use to explain standard `UITabBar`, `UISegmentedControl`, or `UIMenu` behavior |
| https://developer.apple.com/documentation/UIKit/UIVisualEffectView | Container for visual effects | Required host for UIKit visual effects; add subviews to `contentView` |
| https://developer.apple.com/documentation/UIKit/UITabBar | Native tab navigation control | Use for top-level tab navigation; UIKit owns Liquid Glass material/selection behavior |
| https://developer.apple.com/documentation/UIKit/UITabBarItem | Native tab bar item | Provide title, normal image, selected image, badge/accessibility semantics |
| https://developer.apple.com/documentation/UIKit/UISegmentedControl | Native segmented control | Use for local mode switches; UIKit owns Liquid Glass track, selected platter, press feedback, and switching animation |
| https://developer.apple.com/documentation/UIKit/UISegmentedControl/selectedSegmentTintColor | Selected segment tint | Optional public tint API; does not expose internal selected platter geometry or animation |
| https://developer.apple.com/documentation/UIKit/UIButton/Configuration-swift.struct/glass() | Standard glass button | Base glass button style |
| https://developer.apple.com/documentation/UIKit/UIButton/Configuration-swift.struct/prominentGlass() | Prominent glass button | Primary action material tint |
| https://developer.apple.com/documentation/UIKit/UIButton/Configuration-swift.struct/clearGlass() | Clear glass button | Media/rich-background controls |
| https://developer.apple.com/documentation/UIKit/UIButton/Configuration-swift.struct/prominentClearGlass() | Prominent clear button | Rare emphasized media control |
| https://developer.apple.com/documentation/UIKit/UIButtonConfiguration | Objective-C button configuration namespace | Use when bridging UIKit from Objective-C/React Native plugins |
| https://developer.apple.com/documentation/UIKit/UIButtonConfiguration/glassButtonConfiguration | Objective-C/UIKit glass button configuration | Native RN/plugin bridges that instantiate `UIButtonConfiguration` directly |
| https://developer.apple.com/documentation/UIKit/UIButtonConfiguration/plainButtonConfiguration | Transparent button configuration | Title/picker menu triggers with app-owned collapsed text/chevron layout |
| https://developer.apple.com/documentation/UIKit/UIButton/menu | Button-owned menu | Attach command hierarchy to the trigger so UIKit presents it from the button |
| https://developer.apple.com/documentation/UIKit/UIControl/showsMenuAsPrimaryAction | Primary-action menu trigger | Tap/touch shows the control's context menu as the primary action |
| https://developer.apple.com/documentation/UIKit/UIMenu | Menu/submenu container | Preserve nested command hierarchy, inline groups, images, and selected states |
| https://developer.apple.com/documentation/UIKit/UIAction | Leaf command element | Preserve action title, image, state, attributes, and selection callback |
| https://developer.apple.com/documentation/UIKit/UIMenu/Options-swift.struct/displayInline | Inline menu section | Flatten grouped commands with separators instead of deeper submenus |
| https://developer.apple.com/documentation/UIKit/UIMenu/Options-swift.struct/singleSelection | Single-selection menu | Use for picker-like command groups with one selected item |
| https://developer.apple.com/documentation/UIKit/UIMenuElementState/on | Selected/checkmark state | Preserve the selected item semantically instead of drawing a custom checkmark only |
| https://developer.apple.com/documentation/UIKit/UIMenuElementAttributes/disabled | Disabled menu item | Keep unavailable commands visible but disabled when discoverability matters |
| https://developer.apple.com/documentation/UIKit/UIMenuElementAttributes/destructive | Destructive menu item | Use semantic destructive styling for irreversible or risky actions |
| https://developer.apple.com/documentation/UIKit/UIBlurEffect | Standard material fallback | Blur effect below content layer or for legacy material |
| https://developer.apple.com/documentation/UIKit/UIVibrancyEffect | Foreground vibrancy | Keep icons/text vivid above blur |
| https://developer.apple.com/documentation/UIKit/UIVisualEffectView | Container for visual effects | Native fallback; not equivalent to full Liquid Glass |
| https://developer.apple.com/documentation/UIKit/UIScrollEdgeElementContainerInteraction | Scroll-edge registration for custom elements | Custom toolbar/scrim interaction with scrolling content |
| https://developer.apple.com/documentation/UIKit/UIScrollEdgeEffect/Style-swift.class | Scroll edge style | Automatic/hard/soft mapping to edge scrims |
| https://developer.apple.com/documentation/UIKit/UIBackgroundExtensionView | Extend background under sidebars/inspectors | Mirrored/blurred media extension |
| https://developer.apple.com/documentation/UIKit/UITabBarController/Mode-swift.enum/tabSidebar | Tab bar to sidebar adaptation | Responsive navigation by width/device class |
| https://developer.apple.com/documentation/UIKit/UITabBarController/MinimizeBehavior | Tab bar minimization | Scroll-aware nav compaction |
| https://developer.apple.com/documentation/UIKit/UISplitViewController | Sidebar/detail/inspector layout | Multi-pane responsive layout |
| https://developer.apple.com/documentation/UIKit/UISplitViewController/Column/inspector | Inspector column | Detail tool panel on large screens |
| https://developer.apple.com/documentation/UIKit/UICornerConfiguration-swift.struct | Corner style | Concentric/radius consistency |
| https://developer.apple.com/documentation/UIKit/UIView/cornerConfiguration-7l0ja | View corner configuration | Avoid unrelated radius values inside rounded containers |
| https://developer.apple.com/documentation/UIKit/UISearchTab | Semantic search tab | Separate search affordance in top-level navigation |
| https://developer.apple.com/documentation/UIKit/UIFocusItem | tvOS focus participation | Apple TV/kiosk only unless target has focus navigation |

### UIKit Native Menu Route

Use this route when a button opens a menu, picker, command list, or nested action set on iOS/iPadOS 26+. Officially, Liquid Glass menu motion is a system behavior: the menu opens from the triggering bubble, and larger menu glass gets the system's thicker material treatment. In implementation terms, bridge the trigger as a native `UIButton`, assign a `UIMenu`, and set `UIControl.showsMenuAsPrimaryAction` when tap should open the menu.

Trigger choice:

- Icon-only triggers can use a glass button configuration.
- Title/picker triggers can stay visually quiet with a plain button configuration plus an app-owned centered title/chevron layout; UIKit still owns the expanded menu.
- Both routes should assign the menu to the button instead of showing a custom overlay from JavaScript.

Transfer boundary:

- iOS/iPadOS 26+ native apps or React Native/Flutter plugins can use this route directly.
- Web, Android, and older iOS should preserve menu semantics with an anchored fallback, not attempt a pixel-perfect Liquid Glass clone.
- SwiftUI custom glass APIs such as `GlassEffectContainer`, `glassEffectID`, and `glassEffectTransition` are for custom view groups; they are not the first choice when a standard system menu already models the interaction.

### UIKit Native Tab Bar Route

Use this route when the component is top-level app navigation. A real `UITabBar` with `UITabBarItem` objects lets UIKit own the Liquid Glass background, selected platter, press feedback, selected-item transition, VoiceOver semantics, and platform adaptation. The app supplies titles, SF Symbols, selected images, selected/unselected tint, item positioning, selected item, and callbacks.

Do not describe a native `UITabBar` implementation as a `UIGlassEffect` recreation. `UIGlassEffect` belongs to custom glass containers such as search/refresh/input surfaces that standard UIKit components do not cover.

### UIKit Native Segmented Control Route

Use this route for local mode switching or short mutually exclusive filters, not for global navigation. HIG says segmented controls are linear sets of segments that act like buttons, usually equal width, and should keep control type and content style consistent. In the Liquid Glass adoption guide, segmented controls are part of the standard controls whose updated appearance and dimensions should be reviewed without hard-coding layout metrics.

Implementation guidance:

- Bridge as `UISegmentedControl` on iOS/iPadOS 26+ when Liquid Glass is enabled.
- Use `momentary = NO` for persistent selections; use momentary only for action groups without a retained selection.
- Use `apportionsSegmentWidthsByContent = NO` for balanced equal-width choices with similar labels.
- Synchronize selection through `selectedSegmentIndex`; emit `UIControlEventValueChanged` back to the client layer.
- Avoid setting custom background, shadows, internal glass layers, or manual spring animation in the native route.

Adjustable public surface: overall frame, segment widths/content policy, selected index, `selectedSegmentTintColor`, title attributes, and content position offsets.

Not independently adjustable in the native route: selected platter width/height, glass blur/refraction intensity, shadow height, edge relief, and selection animation parameters. Use a custom fallback only when those internals must be controlled, and label it as fallback rather than native Liquid Glass.

## AppKit API Map

| API/page | Use | Cross-platform translation |
|---|---|---|
| https://developer.apple.com/documentation/AppKit/NSGlassEffectView | AppKit Liquid Glass surface | Native macOS glass only |
| https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/glass | Glass button style | Native macOS button analog |
| https://developer.apple.com/documentation/AppKit/NSVisualEffectView | Standard material view | macOS material fallback |
| https://developer.apple.com/documentation/AppKit/NSVisualEffectView/BlendingMode-swift.enum | Within-window/behind-window blending | Choose whether material samples app content or window background |
| https://developer.apple.com/documentation/AppKit/NSVisualEffectView/Material-swift.enum | Standard material variants | Semantic material selection |
| https://developer.apple.com/documentation/AppKit/NSBackgroundExtensionView | Background extension | Mirrored/blurred media under sidebars |
| https://developer.apple.com/documentation/AppKit/NSScrollEdgeEffectStyle | Scroll edge style | Edge readability model |
| https://developer.apple.com/documentation/AppKit/NSSplitViewController | Multi-pane layout | Desktop sidebar/detail patterns |
| https://developer.apple.com/documentation/AppKit/NSSplitViewItem/init(inspectorWithViewController:) | Inspector item | Desktop inspector side panel |
| https://developer.apple.com/documentation/AppKit/NSToolbarItem/Identifier/space | Toolbar spacing | Fixed grouping separators |
| https://developer.apple.com/documentation/AppKit/NSToolbarItem/isHidden | Hide toolbar item | Avoid blank item slots |

## Color And Semantic System APIs

Use this section when glass surfaces need light/dark/high-contrast behavior or native-client semantic colors.

| Platform | Pages | Use |
|---|---|---|
| HIG | https://developer.apple.com/design/human-interface-guidelines/color#System-colors | Prefer semantic color roles instead of hardcoded RGB on glass |
| SwiftUI | https://developer.apple.com/documentation/SwiftUI/Color | Map foregrounds, separators, accents, and backgrounds to semantic tokens |
| UIKit | https://developer.apple.com/documentation/UIKit/UIColor | Use `label`, `secondaryLabel`, `systemBackground`, `separator`, grouped backgrounds |
| AppKit | https://developer.apple.com/documentation/AppKit/NSColor | Use `labelColor`, `controlBackgroundColor`, `windowBackgroundColor`, separator and selection colors |

Cross-platform rule: define custom tokens for default, dark, increased contrast, reduced transparency, and disabled states. Do not rely on a single translucent fill plus white text.

## Landmarks Topic Map

| Landmarks topic | What to extract | Cross-platform use |
|---|---|---|
| https://developer.apple.com/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass | Overall app structure and sequence | Use as case study, not a template to copy |
| https://developer.apple.com/documentation/SwiftUI/Landmarks-Applying-a-background-extension-effect | Edge-to-edge media next to sidebar/inspector | Background/media extension only |
| https://developer.apple.com/documentation/SwiftUI/Landmarks-Extending-horizontal-scrolling-under-a-sidebar-or-inspector | Horizontal collections interacting with side panels | Let carousels visually continue under chrome while keeping controls readable |
| https://developer.apple.com/documentation/SwiftUI/Landmarks-Refining-the-system-provided-glass-effect-in-toolbars | Toolbar grouping | Split actions by semantic group, not by equal spacing |
| https://developer.apple.com/documentation/SwiftUI/Landmarks-Displaying-custom-activity-badges | Custom badges and morphing groups | Compact status/action clusters with stable IDs |
| https://developer.apple.com/documentation/SwiftUI/Landmarks-Creating-Liquid-Glass-effects-in-custom-views | Custom view glass effects | Use only for functional controls and badges |

If a Landmarks page is not available from the public data endpoint, use the sample archive `LandmarksBuildingAnAppWithLiquidGlass.zip` as secondary confirmation when available. This archive was used during research but is not bundled; obtain it from the official Landmarks source above rather than assuming a machine-specific download path.

## Platform-Specific Boundaries

| Surface | Classification | Rule for cross-platform frontend |
|---|---|---|
| iOS / iPadOS / macOS bars, tabs, sidebars | Platform-informed transferable | Translate hierarchy, grouping, safe area, and contrast; do not clone exact OS chrome |
| watchOS | Apple-specific / low transfer | Liquid Glass changes are minimal and tied to standard watch controls |
| tvOS | Scenario inspiration | Focus-driven glass is useful for TV/kiosk UIs; not for ordinary Web hover states |
| visionOS | Mostly Apple-specific | Use depth/readability principles only when building spatial or layered interfaces |
| App icons and Icon Composer | Apple-specific / brand-gated | Use layered artwork concepts; do not copy Apple masks/assets or require Icon Composer off Apple platforms |
| SF Symbols | Apple resource / license-sensitive | Use symbol sizing/weight principles; use licensed icon sets outside Apple surfaces |
| Widgets | Platform-specific | Use glanceable hierarchy; do not generalize tinted/clear widget appearance to dense app pages |

## Transferable Design Rules

1. Separate **content layer** and **functional layer** before choosing any blur.
2. Use Liquid Glass only for controls, navigation, inspectors, media controls, status clusters, sheets/popovers, or direct-manipulation highlights.
3. Use standard material or solid surfaces for app backgrounds, content cards, dense tables, and text panels.
4. Choose regular glass by default; choose clear glass only over visually rich media and test with bright backgrounds.
5. Add scroll-edge treatment only when content actually scrolls under floating controls.
6. Group toolbar actions by function and separate groups with fixed spacing.
7. Make corner radii concentric with their containers.
8. Use one prominent tinted glass action per local region.
9. Provide semantic colors for light, dark, increased contrast, and reduced transparency.
10. Do not animate glass continuously; animate geometry, opacity, scale, radius, and state identity.
11. Use stable IDs for morphing groups; otherwise use simple fade/materialize.
12. Test with reduced motion, reduced transparency, keyboard focus, pointer, touch, and busy media backgrounds.

## Code Sketches

### Responsive Top-Level Navigation

Use this as a conceptual SwiftUI mapping for Apple-native work, then translate to responsive Web navigation.

```swift
TabView {
    Tab("Library", systemImage: "books.vertical") {
        LibraryView()
    }

    Tab("Search", systemImage: "magnifyingglass", role: .search) {
        SearchView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.tabBarMinimizeBehavior(.onScrollDown)
```

Frontend translation: bottom nav on small screens, sidebar on wide screens, explicit search placement, and scroll-aware compaction only if the user can easily recover navigation.

### Scroll Edge For Custom Chrome

```css
.scroll-shell {
  position: relative;
  overflow: auto;
}

.floating-toolbar {
  position: sticky;
  top: 0;
  z-index: 10;
  backdrop-filter: blur(18px) saturate(1.35);
  background: color-mix(in srgb, Canvas 68%, transparent);
}

.floating-toolbar::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: -18px;
  height: 18px;
  pointer-events: none;
  background: linear-gradient(to bottom, color-mix(in srgb, Canvas 42%, transparent), transparent);
}
```

Use only when scrolling content passes beneath the toolbar. This is not a decorative shadow.

### Background Extension

```css
.split-view {
  display: grid;
  grid-template-columns: minmax(220px, 280px) 1fr;
}

.sidebar {
  position: relative;
  backdrop-filter: blur(22px) saturate(1.3);
  background: color-mix(in srgb, Canvas 70%, transparent);
}

.sidebar::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--adjacent-media-preview);
  background-size: cover;
  filter: blur(18px);
  opacity: .22;
  z-index: -1;
}
```

Use mirrored or sampled media only as a background impression. Do not move readable text or essential controls under the sidebar.

## Verification Checklist

- [ ] Official source link is primary or design/implementation support, not low-signal metadata.
- [ ] Apple-only APIs are labeled as Apple-only before suggesting a cross-platform implementation.
- [ ] Liquid Glass is not used for content cards, dense forms, or generic decoration.
- [ ] A standard-material or solid fallback exists for reduced transparency and unsupported browsers.
- [ ] 原生动效从[独立动效入口](motion.md)与 [API 动效章节](liquid-glass-api-motion-color.md#motion-and-transition)核对；仅 Web 近似实现使用 [Web 动效参数](../../web/apple-style-motion.md)与 [Web 模板](../../web/apple-style-motion-templates.md)。
- [ ] 原生颜色与材质按上方 HIG 来源、[控件与材质](liquid-glass-controls.md)、[材质层级](liquid-glass-api-motion-color.md#material-hierarchy)和[颜色章节](liquid-glass-api-motion-color.md#color-and-dark-mode)核对；[Apple 风格 Token](../../web/apple-style-tokens.md)仅供 Web 可选参考，不作为原生默认数值。
- [ ] HIG pages that are mainly about input/platform behavior route to [hig-components-inputs](../hig-components-inputs.md) or [platform-resources-technologies](../platform-resources-technologies.md), not Liquid Glass, unless the task explicitly needs glass there.

## Source Links

- https://developer.apple.com/cn/design/human-interface-guidelines/materials#Liquid-Glass
- https://developer.apple.com/design/human-interface-guidelines/materials#Standard-materials
- https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color
- https://developer.apple.com/design/human-interface-guidelines/scroll-views
- https://developer.apple.com/design/human-interface-guidelines/toolbars
- https://developer.apple.com/design/human-interface-guidelines/tab-bars
- https://developer.apple.com/design/human-interface-guidelines/sidebars
- https://developer.apple.com/documentation/technologyoverviews/liquid-glass
- https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
- https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views
- https://developer.apple.com/documentation/swiftui/view-styles
- https://developer.apple.com/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass
- https://developer.apple.com/documentation/SwiftUI/View/glassEffect(_:in:)
- https://developer.apple.com/documentation/SwiftUI/GlassEffectContainer
- https://developer.apple.com/documentation/SwiftUI/GlassEffectTransition
- https://developer.apple.com/documentation/swiftui/glassbuttonstyle
- https://developer.apple.com/documentation/swiftui/glassprominentbuttonstyle
- https://developer.apple.com/documentation/swiftui/defaultglasseffectshape
- https://developer.apple.com/documentation/UIKit/UIGlassEffect
- https://developer.apple.com/documentation/UIKit/UIVisualEffectView
- https://developer.apple.com/documentation/UIKit/UITabBar
- https://developer.apple.com/documentation/UIKit/UITabBarItem
- https://developer.apple.com/documentation/UIKit/UISegmentedControl
- https://developer.apple.com/documentation/UIKit/UISegmentedControl/selectedSegmentTintColor
- https://developer.apple.com/documentation/UIKit/UIButtonConfiguration
- https://developer.apple.com/documentation/UIKit/UIButtonConfiguration/glassButtonConfiguration
- https://developer.apple.com/documentation/UIKit/UIButtonConfiguration/plainButtonConfiguration
- https://developer.apple.com/documentation/UIKit/UIButton/menu
- https://developer.apple.com/documentation/UIKit/UIControl/showsMenuAsPrimaryAction
- https://developer.apple.com/documentation/UIKit/UIMenu
- https://developer.apple.com/documentation/UIKit/UIAction
- https://developer.apple.com/documentation/UIKit/UIContextMenuInteraction
- https://developer.apple.com/documentation/UIKit/UIMenu/Options-swift.struct/displayInline
- https://developer.apple.com/documentation/UIKit/UIMenu/Options-swift.struct/singleSelection
- https://developer.apple.com/documentation/UIKit/UIMenuElementState/on
- https://developer.apple.com/documentation/UIKit/UIMenuElementAttributes/disabled
- https://developer.apple.com/documentation/UIKit/UIMenuElementAttributes/destructive
- https://developer.apple.com/documentation/AppKit/NSGlassEffectView
- https://developer.apple.com/videos/play/wwdc2025/219/
- https://developer.apple.com/videos/play/wwdc2025/243/
