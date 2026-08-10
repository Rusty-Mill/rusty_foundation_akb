# Platform and ecosystem research

Unlike most Rusty Mill domains, this framework is not primarily OS-mechanism-dependent — its native-platform research question is which Rust storage and vector-search ecosystem the implementation trial should evaluate, not Windows/Linux/macOS kernel variance.

## Platform variance

| Platform | State | Candidate mechanisms | Known variance |
|---|---|---|---|
| Windows | Native (expected) | SQLite embeds natively; no OS-specific mechanism identified | None recorded; unverified in Rust |
| Linux | Native (expected) | SQLite embeds natively | None recorded; unverified in Rust |
| macOS | Native (expected) | SQLite embeds natively | None recorded; unverified in Rust |

The Python implementation observes no platform-specific behavior (SQLite + FTS5, optional `sqlite-vec`). This is carried forward as an expectation, not a verified Rust finding, until the implementation trial reports.

## Ecosystem research questions for the trial

- Which Rust SQLite binding (e.g. `rusqlite`) supports FTS5 and a vector-search extension comparably to the Python `sqlite-vec` integration, including build/packaging behavior across the three target platforms.
- Whether the chosen crates require platform-specific build steps (native SQLite linkage, vendored vs. system library) that create packaging variance the Python implementation did not have.
- Which MCP-protocol crate (if any mature one exists) covers the Streamable HTTP transport the Python server uses, and whether that maps onto Rusty Mill's `networking`/`ipc` capabilities as designed or requires a capability gap to be filed.

## Status

No research has been executed against real Rust crates yet. This document records what the trial must investigate; treat every "expected" and "candidate" entry above as unverified until the trial's entry review cites concrete evidence.
