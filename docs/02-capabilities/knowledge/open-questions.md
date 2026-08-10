# Open questions

- Is an existing, running, externally-relied-upon implementation a sufficient forcing function to justify a domain framework ahead of the roadmap's Phase 5 default, or should this wait? (RFC-0003, unresolved pending review.)
- Should `rm.knowledge.*` eventually expose one broad capability or several narrower ones mirroring the four Python tool groups (lookup, validate, search, cross-cutting)?
- Which storage and vector-search crates are credible implementation-trial candidates, and what does "equivalent" mean for hybrid-ranked results where fusion scores are float-sensitive across implementations?
- Does the MCP transport belong under the `networking` capability, the `ipc` capability, or does Rusty Mill need a new capability for the Model Context Protocol specifically? No existing capability currently names MCP.
- How should the multi-domain hosting requirement (ADR-0165) interact with Rusty Mill's profile model — is "hosts N knowledge domains" a framework configuration concern or does it need profile-level representation?
- What happens to the existing Python `knowledge-mcp` server if the trial fails or is inconclusive? RFC-0003 deliberately does not authorize retiring it; a future decision must address this regardless of trial outcome.
- Should ingestion (PDF pipelines, Claude-assisted extraction) be in scope for the Rust trial, or is it acceptable for the trial to consume a pre-ingested fixture and defer ingestion tooling to a later phase?
