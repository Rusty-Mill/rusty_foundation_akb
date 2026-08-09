# Application synchronization ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Application synchronization capability owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation security/privacy review for identity, authorization, offline residuals, metadata, and multi-tenant boundaries |
| Evidence reviewer | Foundation distributed-systems conformance and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains dataset/replica/change identity, topology and dependency declarations, schema/merge policy generations, authority, selection, deletion/retirement, platform/source frontier, profile impact, history generators, benchmark scenarios, findings, and promotion evidence. An actual promotion or trial record replaces role placeholders with accountable people.

## Bounded trial plan

A later Experimental trial may compare two materially different repository shapes and provider families using the same deterministic history corpus. At minimum it exercises local durable intent, snapshot plus incremental catch-up, partition/heal, duplicate/reordered delivery, typed conflicts, selection changes, deletion/tombstone retirement, queued old-schema changes, attachment interruption, authority revocation, backup/restore, and provider migration across Windows, Linux, and macOS clients with a declared authoritative boundary.

The trial must use the [foundation trial template](../../05-governance/implementation-trials/trial-template.md). It does not select a database, protocol, service, CRDT/OT library, merge algorithm, topology, crate boundary, or metadata serialization. Interfaces are unstable, data is synthetic/non-production, publication is disabled, and all code is disposable.

Stop conditions include cross-tenant exposure, forged or replayed authority acceptance, silent intent/history loss, false convergence, resurrection past a retirement frontier, unsafe unbounded amplification, unrecoverable migration, provenance loss, or material input drift.

**RM-APP-SYNC-OWNER-0001:** A promotion or trial record MUST name accountable people, disclose reviewer independence, and bind exact contract/profile/provider/tool generations.

**RM-APP-SYNC-OWNER-0002:** Trial hypotheses MUST distinguish local durability, upload/receipt, authoritative effect, remote observation, and qualified convergence.

**RM-APP-SYNC-OWNER-0003:** A bounded plan is promotion evidence only; it MUST NOT authorize a repository, provider, data set, credential, external service, or implementation.

**RM-APP-SYNC-OWNER-0004:** Disposal MUST revoke provider credentials and datasets, account for every replica/artifact, retain positive and negative evidence, and prohibit experimental artifacts from release channels.

