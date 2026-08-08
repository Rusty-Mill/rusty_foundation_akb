# ADR-0016: Executable search uses explicit directory authority

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Shells and OS APIs search different directories, suffixes, registries, associations, and aliases. Ambient `PATH`, current directory, and platform defaults can change concurrently or be attacker-controlled. Folding search into spawn would make executable identity and authority ambiguous.

## Decision

Executable search is the independent `rm.process.executable-resolve` capability. It consumes an ordered list of explicit directory authorities plus explicit suffix/format policy and returns an auditable candidate for direct spawn. Ambient `PATH`, current directory, `PATHEXT`, App Paths, shell built-ins, and desktop associations are not base inputs; convenience layers may snapshot or model them explicitly.

Resolution remains advisory until launch and reports its lookup strength and replacement race.

## Consequences

- `spawn("tool")` without resolution policy is not a base operation.
- Shell-compatible search can be built as an explicit higher layer.
- Search results retain root/policy/evidence provenance.
- Strong identity policies may reject mechanisms unable to bind inspection to launch.

## Verification

Tests manipulate current directory, `PATH`, suffix policy, root order, links/reparse points, inaccessible candidates, concurrent replacement, and case behavior while confirming deterministic selection and disclosure.

