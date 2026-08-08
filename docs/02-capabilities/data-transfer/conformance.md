# Clipboard and drag-and-drop conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| TRANSFER-OFFER-001 | OFFER-0001–0004 | Multi-item/multi-format fixtures enumerate without side effects; request exact formats with every size/deadline/cancellation/destination policy |
| TRANSFER-OFFER-002 | OFFER-0005–0010 | Partial streams, source exit, stale generation, conversion loss/failure, encoding/control text, path/URL authority, secret preview/log canaries |
| TRANSFER-CLIP-001 | CLIPBOARD-0001–0004 | General/primary channels, replacement/ownership/source-exit races, lazy/system-persisted content, exact generation reads, lock/logout/remote transitions |
| TRANSFER-CLIP-002 | CLIPBOARD-0005–0009 | Deny polling/history/background access, stress UI-thread lazy providers, persistence/sync/clear nonclaims, keyboard/AT copy-paste outcomes |
| TRANSFER-DRAG-001 | DRAG-0001–0004 | Pointer/keyboard/AT initiation; enter/update/leave/drop across windows/scales; format/action changes; prove no hover materialization |
| TRANSFER-DRAG-002 | DRAG-0005–0009 | Copy/move/link commit, target/source exit, every cancellation/failure stage, rollback, accessible feedback, malicious target/source |
| TRANSFER-PROMISE-001 | PROMISE-0001–0007 | Traversal/reserved/collision/symlink fixtures, large/multi-item partial writes, integrity, atomic publication, metadata/quarantine, scanning isolation, move acknowledgement |

## Interoperability matrix

Fixtures cover plain Unicode text/newlines/NUL/control characters, HTML/rich text with hostile markup, URLs, images and malformed metadata, file lists/references, large binary streams, custom versioned types, empty/multiple items, promised files/directories, and unavailable converters. Each is tested Rusty Mill-to-native, native-to-Rusty Mill, and Rusty Mill provider-to-provider on Windows, Wayland, X11 where supported, and macOS.

Terminal paste tests require explicit user action/policy, bracketed-paste mode revision, control/newline review, maximum size, backpressure, secure-input suppression, and no duplicate text/key delivery. Accessibility tests cover nonpointer drag operation/target selection, insertion feedback, progress, cancellation, and result announcements.

