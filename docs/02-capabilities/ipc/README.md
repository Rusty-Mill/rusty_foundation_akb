# IPC foundations vertical slice

| Field | Value |
|---|---|
| Status | Draft domain analysis |
| Domain version | 0.1.1 |
| Accountable role | IPC capability owner |
| Purpose | Define local anonymous byte transport independently from files, process spawning, terminals, and message protocols |

## Initial boundary

The first IPC capability is a unidirectional anonymous byte pipe with one read end and one write end. It supports local producer/consumer composition and process standard-stream redirection.

Named endpoints, unrelated-process discovery, duplex channels, message boundaries, credential exchange, handle/descriptor passing, shared memory, remote transport, terminal semantics, and serialization protocols remain later capabilities.

```mermaid
flowchart LR
    Create["rm.ipc.byte-pipe"] --> Read["Owned read end"]
    Create --> Write["Owned write end"]
    Write -->|"bounded byte stream"| Read
    Read -.->|"optional inheritance"| Spawn["rm.process.spawn stdio binding"]
    Write -.->|"optional inheritance"| Spawn
    Cancel["rm.runtime.cancellation"] -.-> Read
    Cancel -.-> Write
```

## Documents

- [`rm.ipc.byte-pipe`](byte-pipe.md)
- [Platform research](platform-research.md)
- [Conformance specification](conformance.md)
- [Benchmark specification](benchmarks.md)
- [Assertion and benchmark traceability](traceability.md)
- [Dependency and profile composition](dependencies.md)
- [Cross-cutting review](cross-cutting.md)
- [Source review](source-review.md)
- [Ownership and bounded trial plan](ownership.md)
- [Experimental promotion review](promotion-review.md)
