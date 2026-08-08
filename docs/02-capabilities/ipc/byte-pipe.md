# `rm.ipc.byte-pipe` — Anonymous byte pipe

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | IPC |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server; optional Embedded/headless |

## Purpose

Create a local, anonymous, unidirectional, kernel-mediated byte stream as independently owned read and write endpoints with explicit buffering, backpressure, EOF, broken-peer, cancellation, and inheritance behavior.

## Requirements

- **RM-IPC-PIPE-0001:** Creation **MUST** return exactly one read-authority endpoint and one write-authority endpoint or fail without exposing indeterminate endpoints.
- **RM-IPC-PIPE-0002:** Endpoints **MUST** be non-inheritable/non-transferable by default; process inheritance requires an explicit allowlisted binding.
- **RM-IPC-PIPE-0003:** Reads and writes **MAY** complete with partial progress and **MUST** report exact transferred bytes.
- **RM-IPC-PIPE-0004:** A read **MUST** report EOF only after every write reference is closed and all previously accepted bytes are consumed.
- **RM-IPC-PIPE-0005:** A write with no remaining reader **MUST** return a typed broken-peer outcome; provider-native signals/exceptions **MUST NOT** terminate the host process unexpectedly through safe use.
- **RM-IPC-PIPE-0006:** Buffer capacity and requested size **MUST** be treated as provider claims/hints; the base contract **MUST NOT** promise a fixed capacity.
- **RM-IPC-PIPE-0007:** Backpressure **MUST** bound accepted-but-unread data and expose would-block or pending state without busy spinning.
- **RM-IPC-PIPE-0008:** Any non-interleaving/atomic-write guarantee **MUST** publish a scoped maximum request size and writer conditions; larger writes carry no message boundary.
- **RM-IPC-PIPE-0009:** Closing one endpoint **MUST NOT** close duplicates or the peer; duplication and transfer rules **MUST** preserve direction and authority.
- **RM-IPC-PIPE-0010:** Async operations **MUST** retain buffers and native state until terminal completion and **MUST NOT** occupy an executor worker solely to block where a native readiness/completion mechanism is available.
- **RM-IPC-PIPE-0011:** Sync operations **MUST** be available and **MUST NOT** create or nest a hidden async runtime.
- **RM-IPC-PIPE-0012:** Cancellation **MUST** distinguish requested, confirmed canceled, completed progress, and indeterminate provider outcome; accepted bytes are never rolled back.
- **RM-IPC-PIPE-0013:** Concurrent reads and concurrent writes **MUST** state ordering and interleaving; no fairness is assumed without evidence.
- **RM-IPC-PIPE-0014:** Error categories **MUST** distinguish closed endpoint, broken peer, would block, confirmed canceled, resource exhausted, access/transfer denied, and provider failure.
- **RM-IPC-PIPE-0015:** Diagnostics **MUST NOT** capture stream contents by default; byte counts and sanitized correlation are sufficient.

## Resource and direction model

Read endpoints cannot write and write endpoints cannot read through safe interfaces. Half-close is simply closing one direction because the base pipe is unidirectional. A duplex conversation uses two pipes or a future duplex capability and must close unused duplicate endpoints promptly so EOF remains observable.

## Async quality

| Quality | Meaning |
|---|---|
| Q0 — Sync only | Correct synchronous operations; async contract unavailable |
| Q1 — Adapted async | Async surface may use a bounded dedicated blocking facility disclosed by the provider |
| Q2 — Native readiness | Nonblocking endpoint integrated with native readiness notification |
| Q3 — Native completion | Native asynchronous completion with direct buffer lifecycle |

Async-first profiles require Q2 or Q3 unless they explicitly permit Q1 with worker and saturation budgets. A Windows provider using basic `CreatePipe` cannot claim overlapped completion merely because the handle type is pipe-like.

## Dependencies

No required capability dependency. Cancellation is optional. Process spawn may inherit a selected endpoint but does not own pipe semantics.

