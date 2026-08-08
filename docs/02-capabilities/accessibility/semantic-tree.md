# `rm.accessibility.semantic-tree`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-ACCESSIBILITY-TREE-0001:** A semantic snapshot has an immutable tree revision, stable-within-document opaque node identities, one application/window root, parent/child order, and explicit ownership/label/description/control/flow relationships.

**RM-ACCESSIBILITY-TREE-0002:** Each node declares semantic role, localized name/description/help, value/range where relevant, states, supported actions, focusability/focus, selection, visibility/offscreen/occlusion knowledge, enabled/read-only/required/invalid status, sensitivity, language/direction, and geometry availability.

**RM-ACCESSIBILITY-TREE-0003:** Role and supported behavior are consistent: an actionable role exposes its required action/value/selection/text contracts, while unsupported operations remain unavailable. Custom roles preserve a nearest honest base semantic plus an extension description.

**RM-ACCESSIBILITY-TREE-0004:** Names and descriptions follow explicit precedence and source references. User-visible text is not duplicated into both name and description without policy, and placeholder/help/error text remains distinguishable.

**RM-ACCESSIBILITY-TREE-0005:** Geometry is typed in window-logical coordinates and tied to semantic, layout, and window-transform revisions. Nonvisual, virtualized, clipped, and offscreen nodes report those facts rather than fabricated rectangles.

**RM-ACCESSIBILITY-TREE-0006:** Semantic child order represents logical navigation/reading order. A different visual/z-order or DOM/storage order is related explicitly; cyclic ownership/label/control relationships are rejected.

**RM-ACCESSIBILITY-TREE-0007:** Virtualization may omit realized descendants only when the parent exposes count/range/placeholder information and a bounded realization/navigation contract. Offscreen does not imply absent from the semantic tree.

**RM-ACCESSIBILITY-TREE-0008:** Node identity survives compatible state/geometry changes but not semantic replacement. Removed identities never alias new nodes within the same document epoch.

**RM-ACCESSIBILITY-TREE-0009:** Snapshot production validates required names, state/role consistency, relationship targets, focus uniqueness, text-range ownership, action declarations, and sensitive-data policy before publication.

**RM-ACCESSIBILITY-TREE-0010:** Untrusted document/terminal/web content cannot assert privileged native roles, actions, trusted dialogs, security status, or host relationships without framework policy validation.

