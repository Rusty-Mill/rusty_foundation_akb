# ADR-0127: Deprovisioning is multi-boundary reconciliation, not account disablement

## Status

Accepted

## Context

Account disablement may stop one login path while active sessions, tokens, credentials, group caches, resource-local grants, delegated access, devices, jobs, owned resources, downstream SaaS accounts, and offline replicas remain effective. Treating a successful directory write as completion creates false security and audit claims.

## Decision

Rusty Mill models deprovisioning as a generation-bound workflow across explicitly inventoried access, credential, session, resource, ownership, retention, and provider boundaries. Each effect has its own requested, applied, observed, verified, failed, deferred, exempt, unmanaged, or unknown result. Completion claims name the frontier and residuals; restoration requires a new authorized generation.

## Consequences

- Fast ingress disablement and complete cleanup can have different objectives.
- Partial failure remains visible and retryable.
- Restore, replay, rehire, and identifier reuse cannot silently resurrect access.
- Products must define their resource inventory, deadlines, exemptions, and escalation policy.
