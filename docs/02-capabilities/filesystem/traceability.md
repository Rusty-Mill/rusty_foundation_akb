# Filesystem assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Filesystem foundations](README.md)

Stable semantic assertions identify portable propositions; the existing `CT-FS-*` and `BM-FS-*` identifiers remain suite-local procedures and workloads.

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.filesystem.directory@1` | `directory.md` | Verify separated authority, rename-stable anchoring, lifecycle, lossless enumeration, mutation behavior, identity, disclosure, and namespace synchronization. |
| `rm.assertion.filesystem.resolve@1` | `resolve.md` | Verify directory-relative authority, typed policy, R-level containment, race resistance, access non-escalation, cleanup, and redacted diagnostics. |
| `rm.assertion.filesystem.file@1` | `file.md` | Verify owned resources, positioned partial I/O, overflow, concurrency, buffer lifetime, cancellation truth, sync completeness, size change, durability, and errors. |
| `rm.assertion.filesystem.metadata@1` | `metadata.md` | Verify explicit subjects, per-field availability, kind/size/time semantics, scoped identity, immutable snapshots, path races, and native extensions. |
| `rm.assertion.filesystem.atomic-replace@1` | `atomic-replace.md` | Verify authority, same-filesystem eligibility, atomic visibility, metadata/identity/backup policy, failure truth, commit cancellation, and durability composition. |
| `rm.assertion.filesystem.durability@1` | `durability-model.md` | Verify D-level scope, retrieval metadata, namespace sync, cache/ordering evidence, failure/cancellation truth, and remote acknowledgement boundaries. |
| `rm.assertion.filesystem.dependencies@1` | `dependencies.md` | Verify exact capability edges, direction, conditions, profile resolution, and graph/profile separation. |
| `rm.assertion.filesystem.quality-review@1` | `cross-cutting.md` | Verify all six quality dimensions have exact requirements, methods, limitations, and claim boundaries. |
| `rm.assertion.filesystem.source-review@1` | `source-review.md` | Verify source authority/status, reviewed propositions, provider applicability, mutable-source binding, and invalidation triggers. |
| `rm.assertion.filesystem.ownership@1` | `ownership.md` | Verify accountable roles, provider coverage, bounded trial nonclaims, stop conditions, cleanup, and retained evidence. |
| `rm.assertion.filesystem.promotion-boundary@1` | `promotion-review.md`, `traceability.md` | Verify traceability invariants and planning eligibility remain separate from maturity, implementation authority, provider choice, and observed evidence. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.filesystem.path-operations@1` | `RM-FILESYSTEM-BENCH-0001`, `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008` | BM-FS-PATH-001 | Same native value, grammar, component count, capacity policy, output semantics, and allocation boundary. |
| `rm.benchmark.filesystem.resolve@1` | `RM-FILESYSTEM-BENCH-0002`, `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008` | BM-FS-RESOLVE-001 | Same authority, policy, R-level, object/create/access semantics, filesystem state, and success oracle. |
| `rm.benchmark.filesystem.adversarial-resolve@1` | `RM-FILESYSTEM-BENCH-0003`, `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008` | BM-FS-RESOLVE-002 | Same mutation schedule, containment/object oracle, retry policy, fixtures, and terminal-result accounting. |
| `rm.benchmark.filesystem.file-io@1` | `RM-FILESYSTEM-BENCH-0004`, `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008` | BM-FS-FILE-001–004 | Same offsets, sizes, queue depths, buffers, cache state, cancellation points, partial-progress oracle, and sync/async guarantees. |
| `rm.benchmark.filesystem.metadata@1` | `RM-FILESYSTEM-BENCH-0005`, `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008` | BM-FS-META-001 | Same subject, base/extension field set, availability obligations, fixture state, and query boundary. |
| `rm.benchmark.filesystem.atomic-replace@1` | `RM-FILESYSTEM-BENCH-0006`, `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008` | BM-FS-REPLACE-001 | Same source/destination relation, metadata/backup policy, commit oracle, failure injection, and D-level. |
| `rm.benchmark.filesystem.durability@1` | `RM-FILESYSTEM-BENCH-0006`, `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008` | BM-FS-DURABILITY-001–002 | Same D-level, failure model, content/namespace workload, cache/device boundary, batching, and post-restart oracle. |
| `rm.benchmark.filesystem.errors@1` | `RM-FILESYSTEM-BENCH-0007`, `RM-FILESYSTEM-BENCH-0008`, `RM-FILESYSTEM-BENCH-0009` | BM-FS-ERROR-001 | Same semantic category, native evidence, redaction policy, causal depth, lazy-message policy, and correctness gate. |

**RM-FILESYSTEM-TRACE-0001:** Every filesystem capability requirement MUST map to a stable semantic assertion and an executable case or review method before Experimental promotion.

**RM-FILESYSTEM-TRACE-0002:** Windows, Linux, and macOS case adapters MUST preserve semantic assertion identity while reporting provider, OS, filesystem, mount/volume, storage, and policy details separately.

**RM-FILESYSTEM-TRACE-0003:** Namespace visibility, file-content completion, file durability, namespace durability, device-stable persistence, and remote acknowledgement MUST remain separate oracles.

**RM-FILESYSTEM-TRACE-0004:** Legacy `CT-FS-*` and `BM-FS-*` identities remain suite-local and MUST map to stable semantic identities before comparison or promotion use.
