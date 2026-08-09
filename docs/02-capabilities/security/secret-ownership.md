# Secret-protection ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Secret-protection owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation secret-management/security review for protection claims, exposure, provider state, replicas, recovery, deletion, and diagnostics |
| Evidence reviewer | Foundation secret-store conformance, platform-lifecycle, accessibility, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains claim-vector matching, item identity, create/replace/delete, generations/conflicts, metadata/enumeration, secret-value exposure, interaction, sync/async/cancellation, provider lifecycle, replication/backup/recovery, deletion residuals, errors/observability, compliance claims, dependencies/profiles, source/quality review, conformance, benchmarks, and dossier boundaries. Provider owners maintain separate Windows, Linux, and macOS store/item/configuration/account/session frontiers. Consumer owners retain purpose, target/audience, secret class/format, operation-specific opaque use, rotation, delivery, and downstream-copy policy.

## Bounded trial plan

A later disposable trial may exercise generated canary secrets and sensitive metadata across exact provider/item classes. It may mutate every required protection dimension, test create collisions and conditional replace, enumerate under distinct authority, exercise opaque/scoped/owned exposure, trigger declared prompt/no-prompt/locked/headless cases, race cancellation and provider completion, inject every supported native failure, and traverse logout/lock/account/password/reboot/migration/backup/restore/sync/sandbox/provider-update/delete/recovery states.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), disposable accounts/keychains/collections/keyrings/stores and isolated machines/VMs where lifecycle changes are destructive, generated non-production values, bounded items/concurrency/time, isolated native code, and no production credentials, endpoints, backups, or data. It does not select public Rust APIs, crates/workspaces, default providers, item schemas, remote vault protocols, cryptographic algorithms, product prompts, retention, performance budgets, assurance/certification, or release support.

Stop conditions include plaintext before successful selection, silent plaintext/file/environment fallback, unexpected prompt or network/replication, unauthorized enumeration/export/replace/delete, overwrite on create, stale-generation acceptance, secret/derived/sensitive-metadata leakage, fabricated cancellation/deletion/erasure state, unreconciled item or provider operation, unsafe destructive lifecycle testing, unbounded resource use, provenance loss, or material drift.

**RM-SECURITY-SECRET-OWNER-0001:** Promotion and trial records MUST name accountable people for the unit and every claimed provider/store/item/platform/account/session/configuration context, exact generations, reviewer independence, and unresolved limitations.

**RM-SECURITY-SECRET-OWNER-0002:** Trial hypotheses MUST distinguish discovery, selection, plaintext submission, provider acceptance, visibility, exposure/use, update/delete acceptance, cancellation, replication/backup, garbage collection, recovery, and evidenced erasure.

**RM-SECURITY-SECRET-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, native/unsafe code, production secret access, persistent host changes, accounts/identities, prompting, networking/synchronization, backup/restore, destructive deletion, cryptographic choice, packaging, or release.

**RM-SECURITY-SECRET-OWNER-0004:** Closeout MUST account for every generated value, item generation, metadata record, provider session, account/store/collection/keyring, replica/backup/restore copy, temporary exposure buffer, log/trace/report, and host policy change; retain only sanitized negative evidence and documented residuals.
