# Filesystem foundations benchmark specification

| Field | Value |
|---|---|
| Status | Draft |
| Suite version | 0.1.0 |

## Principles

Compare equivalent guarantees, separate warm-cache and cold-cache behavior, record filesystem/mount/storage details, and report distributions plus throughput. Benchmarks do not weaken correctness, authority, or durability semantics.

## Catalog

| ID | Subject | Measures | Dimensions |
|---|---|---|---|
| BM-FS-PATH-001 | Path parsing and join | latency, allocations, bytes/s | component count, native encoding, grammar |
| BM-FS-RESOLVE-001 | Directory-relative open | latency, syscalls/native calls, allocations | depth, link policy, existing/create |
| BM-FS-RESOLVE-002 | Adversarial containment | throughput, retries, failure cost | concurrent rename/link mutation |
| BM-FS-FILE-001 | Positioned sequential I/O | throughput, CPU, allocations | sizes 4 KiB–16 MiB; sync/async |
| BM-FS-FILE-002 | Positioned random I/O | IOPS, latency distribution, queue depth | read/write mix and working set |
| BM-FS-FILE-003 | Async concurrency | throughput, tail latency, memory/op | queue depth 1–65K |
| BM-FS-FILE-004 | Cancel/complete race | cancel latency, retained memory, terminal mix | queue depth and device latency |
| BM-FS-META-001 | Handle metadata snapshot | latency, native calls, allocations | base and extended fields |
| BM-FS-REPLACE-001 | Atomic replacement | latency, sync cost, metadata cost | file size, backup, durability level |
| BM-FS-ERROR-001 | Error construction | latency, allocations, redaction cost | shallow/deep cause chains |

## Baselines

- Windows: idiomatic handle-relative or `CreateFileW` open policy, positioned overlapped I/O, handle metadata query, and `ReplaceFileW` where equivalent.
- Linux: `openat2`/`openat`, `pread`/`pwrite` or equivalent async path, `fstat`/`statx`, and `renameat2`/`renameat`.
- macOS: `openat`, `pread`/`pwrite` or equivalent async composition, `fstatat`/`fstat`, and `rename`/supported extension.

A faster baseline with weaker traversal, sharing, cancellation, metadata, atomicity, or durability semantics is reported separately and not used for overhead gating.

## Environment controls

Record storage medium/controller, filesystem and options, free space, encryption/compression, cache state, power policy, antivirus/indexing where relevant, network topology, queue scheduler, and background load. Cold-cache tests use a documented isolation method; unsupported cache dropping is not simulated by relabeling warm results.

## Structural budgets before baselines

- Path operations do not allocate when caller-provided capacity suffices.
- Positioned I/O adds no mandatory data copy beyond native buffer requirements.
- Async operations use bounded per-operation state and no dedicated thread per request.
- Metadata base queries avoid fetching unrequested expensive extensions.
- Atomic replacement does not copy file contents as a hidden fallback.
- Error construction cost is bounded and provider messages are captured lazily where practical.

Numeric regression budgets follow at least three representative baseline runs per platform/filesystem class and require an RFC.
