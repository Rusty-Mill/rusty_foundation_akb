# Platform and ecosystem research

Unlike most Rusty Mill domains, this framework is not primarily OS-mechanism-dependent — its native-platform research question is which Rust storage and vector-search ecosystem the implementation trial should evaluate, not Windows/Linux/macOS kernel variance. This revision replaces the prior all-"Unevaluated" state with real, cited crate research (2026-08-10). **Research is not selection**: nothing below is a dependency decision, and TRIAL-0003's Repository/Bounds/Cross-cutting gates are unaffected by this document alone, per [RM-KNOWLEDGE-OWNER-0003](ownership.md).

## Platform variance

| Platform | State | Candidate mechanisms | Known variance |
|---|---|---|---|
| Windows | Native (expected) | SQLite embeds natively via `libsqlite3-sys`'s `bundled` build | Not yet built/tested on Windows under this trial; expected to work, per `libsqlite3-sys`'s standard cross-platform bundled-SQLite build |
| Linux | Native (expected) | Same | Not yet built/tested under this trial |
| macOS | Native (expected) | Same | Not yet built/tested under this trial |

The Python implementation observes no platform-specific behavior. Everything below is a *researched candidate*, not a built-and-verified result — no crate listed here has been compiled, linked, or exercised under this trial's own authority.

## Storage and full-text search: `rusqlite`

[`rusqlite`](https://github.com/rusqlite/rusqlite) (MIT license) is the standard ergonomic Rust binding to SQLite. Its `Cargo.toml` exposes no dedicated `fts5` Cargo feature — FTS5 is a compile-time property of the underlying SQLite C library, not a Rust-side flag. Confirmed via `libsqlite3-sys/build.rs` (the sibling crate `rusqlite` depends on for its `bundled` feature): the bundled build passes `-DSQLITE_ENABLE_FTS5` to the C compiler alongside FTS3, JSON1, and RTree, so `rusqlite = { features = ["bundled"] }` transitively yields a SQLite binary with FTS5 compiled in. FTS5 virtual tables are then created and queried via ordinary SQL (`CREATE VIRTUAL TABLE ... USING fts5(...)`), not a Rust API surface — this matches the Python implementation's own use of FTS5 via raw SQL.

**Candidate:** `rusqlite = { version = "0.40", features = ["bundled"] }` (0.40.1 was current as of this research; bundled SQLite version 3.53.2 as of that release). Cross-platform by construction — `bundled` avoids depending on a system SQLite install, which the Windows/Linux/macOS parity goal needs.

Sources: [rusqlite README](https://raw.githubusercontent.com/rusqlite/rusqlite/master/README.md), [rusqlite Cargo.toml feature list](https://raw.githubusercontent.com/rusqlite/rusqlite/master/Cargo.toml), [libsqlite3-sys build.rs FTS5 flag](https://github.com/rusqlite/rusqlite/blob/master/libsqlite3-sys/build.rs).

## Vector search: `sqlite-vec`

[`sqlite-vec`](https://github.com/asg017/sqlite-vec) (MIT/Apache-2.0 dual, matching this ecosystem's own licensing convention) provides FFI bindings to the `sqlite-vec` C extension — a small, dependency-free vector-search SQLite extension supporting float/int8/binary vectors in `vec0` virtual tables, running anywhere SQLite runs including WASM. It is the direct successor to `sqlite-vss`, which the Python `knowledge-mcp` server's own dependency (`sqlite-vec`, same project, Python bindings) already uses — so this is the same underlying extension, not a different vector-search approach, which matters for `RK-004`'s "equivalent hybrid retrieval" hypothesis.

**Candidate:** `sqlite-vec` crate, version `0.1.10-alpha.4` as of this research — explicitly **pre-1.0/alpha**, disclosed as such by its own crates.io listing, not softened here. Registration is via `sqlite3_auto_extension()` against the same SQLite connection `rusqlite` opens, not a separate crate integration layer.

Sources: [sqlite-vec crates.io API](https://crates.io/api/v1/crates/sqlite-vec), [sqlite-vec Rust usage guide](https://alexgarcia.xyz/sqlite-vec/rust.html), [sqlite-vec GitHub](https://github.com/asg017/sqlite-vec).

## MCP transport: `rmcp`

[`rmcp`](https://github.com/modelcontextprotocol/rust-sdk) is the **official** Rust SDK for the Model Context Protocol (Apache-2.0 license), published by the `modelcontextprotocol` GitHub organization itself — resolving `RK-005`'s open question in favor of "an existing crate covers this," rather than exposing a genuine taxonomy gap. It supports building both MCP servers and clients, with multiple transports: stdio (child-process launch), Streamable HTTP (server exposed as a mountable Tower service; SSE handled automatically for server-pushed notifications), and an in-process/worker transport for embedding or tests. This covers the Python `knowledge-mcp` server's own Streamable HTTP/ASGI transport directly.

**Version discrepancy, disclosed rather than resolved:** two sources disagreed during this research. A GitHub README search result cited `rmcp = { version = "0.8.0", features = ["server"] }`; the crates.io API's `max_version` field reported `3.1.2` for the same crate/repository (`modelcontextprotocol/rust-sdk` in both cases). This document does not guess which is current — a future trial revision must re-verify the exact version and changelog before citing it as a dependency candidate, since a jump from `0.x` to `3.x` (if real) likely carries breaking changes.

Sources: [rmcp crates.io API](https://crates.io/api/v1/crates/rmcp), [rmcp README](https://github.com/modelcontextprotocol/rust-sdk/blob/main/crates/rmcp/README.md), [modelcontextprotocol/rust-sdk repository](https://github.com/modelcontextprotocol/rust-sdk).

## Ecosystem research questions still open for the trial

- Re-verify `rmcp`'s exact current version and whether the SDK's stable-MCP-spec compatibility claims (2026-07-28 spec, backward-compatible to 2025-11-25) hold as of the trial's actual start date — this research is a point-in-time snapshot, not a standing guarantee.
- Whether `sqlite-vec`'s pre-1.0/alpha status is an acceptable trial dependency given [RM-DEV-PROFILE](../../05-governance/software-development/repository-profile.md)-style dependency-policy expectations, or whether a more mature (if less directly Python-equivalent) alternative should be evaluated instead.
- Whether `rusqlite`'s `bundled` feature's build-time C compilation (rather than dynamic linking to a system SQLite) creates CI/packaging cost across three platforms that the Python implementation, using a system or wheel-bundled SQLite, did not have to consider.
- Whether `rmcp`'s Streamable HTTP server-as-Tower-service design maps cleanly onto `networking`/`ipc` as currently scoped (both Draft), or exposes the kind of gap `RK-005` originally worried about at a different layer (the HTTP/Tower composition itself, not MCP-the-protocol).

## Status

This document now reflects real, cited, point-in-time research — not "Unevaluated" placeholders. It remains **research, not selection**: no crate above has been added to any `Cargo.toml`, compiled, or exercised, and this document alone does not change TRIAL-0003's Repository, Bounds, Verification, or Cross-cutting gate states.
