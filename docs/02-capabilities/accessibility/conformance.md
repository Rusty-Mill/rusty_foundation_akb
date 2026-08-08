# Accessibility conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| ACCESS-TREE-001 | TREE-0001–0005 | Generate role/state/action/name/relationship/geometry matrices; reject incomplete, contradictory, stale, and fabricated semantics |
| ACCESS-TREE-002 | TREE-0006–0010 | Exercise logical versus visual order, cycles, virtualization, identity replacement, focus uniqueness, and untrusted semantic escalation |
| ACCESS-TEXT-001 | TEXT-0001–0005 | Multilingual/bidi/emoji/combining text range navigation, chunking, selections, composition, edit/reflow transforms, invalidation, and native-unit mappings |
| ACCESS-TEXT-002 | TEXT-0006–0009 | Geometry round trips, offscreen/virtual fragments, embedded/generated content, password policy, and semantic attribute runs |
| ACCESS-EVENT-001 | EVENT-0001–0005 | Atomic update/query races, event storms/coalescing, live priorities/busy state, focus/active-descendant/caret separation, reset/resnapshot |
| ACCESS-ACTION-001 | EVENT-0006–0009 | Invoke every action through native AT paths under stale/disabled/unauthorized/destructive/cancelled/failing states; compare keyboard/pointer outcome |
| ACCESS-PREF-001 | PREF-0001–0006 | Toggle every supported OS preference during active UI; validate unknown states, revision delivery, semantic stability, and privacy |
| ACCESS-ADAPTER-001 | ADAPTER-0001–0006 | Inspect exact UIA/AT-SPI/macOS mappings, restart/disconnect adapters, invalidate cached objects/ranges, and rebuild root epoch |
| ACCESS-ADAPTER-002 | ADAPTER-0007–0009 | Cross-process request floods, recursion/oversize limits, diagnostic canaries, native inspection tools, and representative AT workflows |

## End-to-end scenarios

Required scenarios cover keyboard-only navigation; screen-reader browse/focus/forms modes; Braille/text range navigation where available; magnification/zoom; high contrast/forced colors; reduced motion; switch/voice/accessibility-generated input; focus restoration; dialogs/errors/progress/live logs; editable text and IME; virtualized lists/tables/trees; drag alternatives; timeout/cancellation; and recovery after adapter/application state churn.

Terminal evidence uses the terminal logical-state accessibility model: viewport/history reading, cursor and selection, output-storm coalescing, secure-input minimization, host control escape/return, and untrusted terminal annotation rejection. Pixel OCR or raw escape-sequence reparsing cannot satisfy it.

Conformance records OS/build, native accessibility API/provider, assistive technology/version/configuration, locale/input method, display/preferences, application/provider versions, scenario transcript, semantic/native snapshots, event trace, action outcomes, waivers, and privacy-safe artifacts.

