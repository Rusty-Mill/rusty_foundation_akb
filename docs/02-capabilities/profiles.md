# Capability profiles

Profiles are named, versioned, resolvable workload contracts. They select exact capability contracts, services, quality and security constraints; they never require an undifferentiated domain such as “filesystem” or “security.”

The current profiles are deliberately **foundation profiles**. They exercise only specified capabilities and expose missing workload domains as explicit gaps. They are not yet promises that Rusty Mill can support a complete CLI, desktop, server, or embedded application.

## Profile system

- [Profile contract and resolution rules](profiles/profile-contract.md)
- [Resolution report](profiles/resolution-report.md)
- [Foundation profile comparison](profiles/README.md)

## Seed manifests

- [`rm.profile.foundation.cli`](profiles/foundation-cli.md)
- [`rm.profile.foundation.desktop`](profiles/foundation-desktop.md)
- [`rm.profile.foundation.server`](profiles/foundation-server.md)
- [`rm.profile.foundation.headless`](profiles/foundation-headless.md)

## Authority

Profile requirements are consumer-side constraints. Capability specifications remain authoritative for behavior, and the [architecture model](../01-architecture/architecture-model.md) governs resolution. Profiles cannot strengthen a provider claim without evidence, weaken a capability contract, or turn an optional dependency into an undeclared guarantee.
