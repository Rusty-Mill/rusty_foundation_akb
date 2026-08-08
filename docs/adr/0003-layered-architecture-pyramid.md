# ADR-0003: Layered architecture pyramid

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

A platform-scale ecosystem can become tightly coupled when applications, services, and common APIs reach into backend or OS details.

## Decision

Adopt seven layers: OS backends, backend contracts, capability framework, common APIs, platform services, domain frameworks, and applications. Dependencies flow downward through the adjacent layer. Mechanism belongs below policy.

## Alternatives considered

- Unrestricted dependency graph: flexible but erodes replaceability and portability.
- Separate service per domain: adds deployment and distributed-systems costs without an initial forcing function.
- Single monolithic API/backend: simple initially but couples evolution and platform details.

## Consequences

- Interfaces and ownership boundaries must be explicit.
- Cross-layer convenience is implemented through composition at the appropriate upper layer.
- Exceptions require an ADR and a migration path.

## Verification

Future workspaces will enforce allowed dependency direction through metadata and CI architecture checks.
