# `rm.profile.foundation.server`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.1.0 |
| Purpose | Long-running non-interactive service foundation with bounded shutdown and protected credentials |

## Workload assumptions

No interactive desktop session, unattended restart, concurrent I/O, explicit service identity, and observable graceful shutdown. Networking, configuration, process service, and observability capabilities remain explicit gaps.

## Required capabilities and services

**RM-PROFILE-FOUNDATION-SERVER-0001:** Requires the [CLI foundation](foundation-cli.md) capability set, `rm.security.secret-store` `>=0.1.0,<0.2.0`, and the orderly shutdown service `>=0.1.0,<0.2.0`.

**RM-PROFILE-FOUNDATION-SERVER-0002:** `rm.filesystem.atomic-replace` is conditionally required when the deployment persists mutable local state. The deployment predicate and required durability level are part of the request; an in-memory/stateless deployment does not select it.

## Security and interaction constraints

- **RM-PROFILE-FOUNDATION-SERVER-0003:** Secret store interaction is prohibited; it remains available before workload acceptance under the configured service identity.
- **RM-PROFILE-FOUNDATION-SERVER-0004:** Secret persistence, machine/service-account binding, exportability, replication, and recovery behavior are explicit.
- **RM-PROFILE-FOUNDATION-SERVER-0005:** No provider may depend on a desktop session or silently fall back to plaintext files.
- **RM-PROFILE-FOUNDATION-SERVER-0006:** Resolution and secret retrieval use explicit authority; environment variables do not become a secret store.
- **RM-PROFILE-FOUNDATION-SERVER-0007:** Restricted execution is optional for workers/helpers and must meet the manifest without interactive degradation.

## Operational constraints

Deadline timers and cancellation support bounded multi-phase shutdown. Sync paths cannot create a runtime, while async I/O waits use native readiness/completion where available. Conformance includes high concurrency, credential rotation conflict, locked/unavailable provider, clock suspend behavior, cancellation races, and supervisor termination.
