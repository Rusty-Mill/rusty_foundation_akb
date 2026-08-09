# ADR-0134: Workflow replay reconstructs decisions and never repeats effects implicitly

## Status

Accepted

## Context

Durable workflow engines often execute orchestration code again to rebuild state after restart. If that code reads mutable external state or directly performs I/O, replay can diverge or repeat messages, charges, writes, credentials, approvals, and other effects. Describing replay as re-execution obscures this critical boundary.

## Decision

Rusty Mill defines workflow replay as deterministic reconstruction of orchestration decisions from authenticated committed history and immutable definition/runtime generations. Time, randomness, identifiers, external results, and version choices are recorded inputs. Replay emits expected commands for comparison but cannot invoke activities, providers, policy, messaging, or domain effects without a separately authorized repair/simulation operation.

## Consequences

- Orchestration code has explicit deterministic restrictions.
- Activities own external I/O and effect contracts.
- Conformance injects environmental variance and detects command divergence.
- Repair appends evidence or creates a linked run rather than altering history silently.
