# ADR-0044: In-process native plugins are fully trusted components

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native dynamic libraries execute in the host address space and can access ambient privileges, corrupt memory, violate ABI contracts, deadlock, crash, or bypass manifest-declared limits. Signing establishes origin/integrity under policy but not containment.

## Decision

In-process native plugins are permitted only as fully trusted host components under explicit ABI/build and loader policy. Plugins requiring security isolation, independent recovery, or narrow authority use a restricted process or pinned component runtime with mediated capabilities.

## Consequences

- The architecture does not market code signing or loader namespaces as a sandbox.
- Third-party ecosystems default toward isolated hosting despite boundary overhead.
- Native in-process conformance includes host-wide residual-risk disclosure.

