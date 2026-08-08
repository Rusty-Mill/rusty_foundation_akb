# Specification-led roadmap

Dates are intentionally absent until scope and capacity are known. Progress is controlled by evidence-based exit criteria.

## Phase 0 — Foundation

- Charter, principles, glossary, architecture pyramid, governance, and repository strategy accepted.
- ADR/RFC processes operational.

## Phase 1 — Domain inventory and meta-model

- Decompose the initial taxonomy into capabilities.
- Define graph schema, capability specification format, and seed profiles.
- Record platform research without designing APIs prematurely.

## Phase 2 — Contracts and verification design

- Specify behavioral contracts for a thin vertical slice across all three platforms.
- Define conformance report and benchmark schemas.
- Establish security, compatibility, and quality review gates.

## Phase 3 — Reference vertical slice

- Through an accepted RFC, select a small capability set with meaningful async, sync, resource, and platform variance.
- Only then create implementation and verification workspaces.
- Prove native mapping, conformance portability, performance methodology, packaging, and update assumptions.

## Phase 4 — Core profiles

- Expand verified capabilities toward CLI, server, desktop, and constrained/headless profiles.
- Stabilize only capabilities supported by evidence on Windows, Linux, and macOS.

## Phase 5 — Ecosystem scale-out

- Add domain frameworks, tooling, distribution channels, and additional repositories only when explicit forcing functions appear.
- Operate compatibility, deprecation, supply-chain, and governance processes continuously.

## Immediate next decisions

1. Review [RFC-0001](../rfc/0001-capability-specification-system.md) and exercise its templates.
2. Select the first domain-analysis slice.
3. Define measurable criteria for the reference vertical slice.
4. Choose a machine-readable graph format only after two real capability specifications expose the requirements.
