# Accessibility platform research

**Status:** Research evidence; normative conclusions live in contracts and ADRs.

## Windows: UI Automation

UI Automation exposes a tree of elements with control types, properties, patterns, and events. Text/TextRange patterns expose semantic streams, selections, ranges, attributes, embedded objects, geometry, and invalidation. Cross-process query cost and virtualized items make bounded snapshots, chunked text retrieval, caching, and explicit realization necessary.

Primary sources: [UI Automation provider overview](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-providersoverview), [control patterns](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-controlpatterns-overview), [Text and TextRange](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-about-text-and-textrange-patterns), [UI Automation events](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-eventsoverview), [virtualized items](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-implementingvirtualizeditem).

## Linux: AT-SPI

AT-SPI exposes accessible objects and interfaces for component geometry, actions, text/editable text, selections, values, tables, images, documents, and relationships over a process boundary. Roles, states, interfaces, hierarchy, text attributes/bounds, and actions are distinct, supporting a semantic model plus adapter rather than a visual-node dump.

Primary sources: [`Atspi.Accessible`](https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/class.Accessible.html), [`Atspi.Text`](https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/iface.Text.html), [`org.a11y.atspi.Action`](https://gnome.pages.gitlab.gnome.org/at-spi2-core/devel-docs/doc-org.a11y.atspi.Action.html), [AT-SPI interfaces](https://gnome.pages.gitlab.gnome.org/at-spi2-core/devel-docs/).

## macOS Accessibility

AppKit accessibility exposes elements through roles, attributes/properties, parameterized attributes, actions, notifications, relationships, text ranges, and geometry. Native controls often supply semantics automatically; custom controls implement accessibility protocols. The platform adapter must operate on main/UI actor constraints without making those constraints the portable application model.

Primary sources: [Accessibility for macOS](https://developer.apple.com/accessibility/macos/), [`NSAccessibility`](https://developer.apple.com/documentation/appkit/nsaccessibility), [`NSAccessibilityElement`](https://developer.apple.com/documentation/appkit/nsaccessibilityelement), [accessibility notifications](https://developer.apple.com/documentation/appkit/nsaccessibility/notification).

## Web mapping evidence

WAI-ARIA defines roles, states, properties, relationships, actions, and live regions mapped by browsers into platform accessibility APIs. It is useful evidence and vocabulary, not Rusty Mill's universal native schema; native UIA, AT-SPI, and macOS contracts retain important differences.

Primary sources: [WAI-ARIA](https://www.w3.org/TR/wai-aria/), [Core Accessibility API Mappings](https://www.w3.org/TR/core-aam/), [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/).

## Derived portability conclusions

| Concern | Portable rule |
|---|---|
| Semantic state | Application/framework-owned immutable snapshot |
| Native vocabulary | Adapter mapping with variance, not universal API union |
| Text | Revisioned semantic ranges with checked native unit conversion |
| Actions | Requests through ordinary domain command path |
| Virtualization | Navigable placeholder/count/realization contract |
| Events | Ordered semantic changes with bounded coalescing/resnapshot |

