# Anonymous byte-pipe conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| IPC-PIPE-001 | 0001, 0002 | Fault creation and inventory endpoint direction/inheritance; no partial endpoint exposure |
| IPC-PIPE-002 | 0003, 0007 | Exercise short/partial transfers, full buffers, would-block, readiness, and bounded memory |
| IPC-PIPE-003 | 0004, 0009 | Duplicate write ends across processes; verify EOF only after final close and buffered drain |
| IPC-PIPE-004 | 0005 | Close all readers during writes; verify typed broken peer and host process survival |
| IPC-PIPE-005 | 0006, 0008 | Measure capacity/atomicity claim boundaries with concurrent writers and tagged records |
| IPC-PIPE-006 | 0010, 0011 | Verify declared Q0–Q3 mechanism, buffer ownership, direct sync path, and no hidden runtime |
| IPC-PIPE-007 | 0012 | Race cancellation against partial progress, readiness, peer close, and normal completion |
| IPC-PIPE-008 | 0013 | Stress multiple readers/writers and validate only the declared ordering/interleaving/fairness |
| IPC-PIPE-009 | 0014, 0015 | Fault resource exhaustion/closed endpoints and scan every diagnostic sink for content canaries |
| IPC-PIPE-010 | 0002, 0004 | Race concurrent process launches and prove only allowlisted endpoints are inherited |

Reports bind claims to platform/version, provider/artifact, async quality, buffer hint/observed capacity, atomic-write scope, descriptor/handle flags, runtime integration, and test-suite version. Pipe contents and content-derived fingerprints are excluded.

