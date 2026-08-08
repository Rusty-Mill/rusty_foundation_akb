# ADR-0011: Restricted execution is a platform service

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Creating a least-authority child crosses process creation, credentials, inherited resources, filesystem/network policy, sandboxing, IPC, readiness, observability, and lifecycle supervision. Treating “sandbox” as a single capability or boolean would hide composition, platform variance, and dangerous launch windows.

## Decision

Restricted execution is a platform service that composes narrower capabilities and policies. It accepts an immutable isolation manifest, denies unlisted authority, requires atomic-or-suspended setup before child code runs, and returns verified enforcement disclosures. Authority attenuation remains the smaller `rm.security.attenuate` capability.

## Consequences

- Process spawning can remain independently useful without claiming isolation.
- Isolation profiles can require outcomes while providers disclose different native compositions.
- Launch must include a restriction-verification and readiness handshake.
- Some macOS restrictions fixed at signing or packaging constrain runtime construction and must be resolved before launch.
- Degraded isolation requires prior manifest permission; silent weakening is prohibited.

## Verification

Conformance attempts handle/descriptor leakage, environment and current-directory inheritance, launch-before-restriction races, descendant escape, unauthorized network/filesystem access, cancellation during setup, and supervisor failure.

