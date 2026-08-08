# ADR-0086: Deployment plans are immutable generation-bound authority

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Package resolution can change as repositories, installed state, pins, architecture, policy, disk, sessions, and native managers change. Allowing a privileged executor to re-resolve or reinterpret a human “update this app” request permits dependency substitution, unexpected removals/downgrades, scope expansion, and unreviewed hooks.

## Decision

Resolution produces an immutable deployment plan bound to exact installed-state, repository, trust, policy, artifact, scope, authority, native-provider, user-choice, restart/reboot, service/data, and recovery generations. Approval binds the plan digest and expiry. Execution revalidates all material preconditions and either follows the plan exactly or returns stale/rejected; it cannot silently re-resolve or broaden it.

## Consequences

- Planning can usually occur without deployment privilege.
- Material environmental changes require explicit re-resolution and approval.
- Plans contain full additions, upgrades, downgrades, removals, hooks, and impacts.
- Native mechanisms remain usable behind evidence-preserving adapters.

