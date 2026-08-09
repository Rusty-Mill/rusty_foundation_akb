# ADR-0156: Unsafe code is a scoped proof obligation

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Cross-platform native providers require FFI, raw handles, memory layout, callbacks, and platform contracts that safe Rust cannot express directly. Treating unsafe as forbidden is impractical; treating it as ordinary code hides soundness obligations.

## Decision

Crates deny unsafe by default. Permitted unsafe is isolated behind safe abstractions, explicitly budgeted/owned, documented per block and function, reviewed by specialists, and supported by tests/fuzz/model/audit evidence. Unsafe operations inside unsafe functions still require explicit unsafe blocks.

## Alternatives considered

- Ban unsafe everywhere: rejected because native capability backends require it.
- Allow unsafe wherever performance or convenience suggests: rejected because local reasoning and auditability collapse.
- Rely only on compiler acceptance: rejected because FFI and semantic invariants extend beyond compiler proof.

## Consequences

- Native backend work carries visible proof and review cost.
- Safe consumers cannot violate the underlying invariants.
- Performance-motivated unsafe needs equivalent benchmark evidence.
