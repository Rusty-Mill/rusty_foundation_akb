# Conformance

**RM-SECRETS-CONFORMANCE-0001:** Model suites cover every secret/credential class, provider/path/version identity, conditional create/replace, metadata partitions, generation/lease/handle distinctions, cancellation milestones, provider recreation, clock changes, rollback, and no secret-derived artifacts.

**RM-SECRETS-CONFORMANCE-0002:** Bootstrap/workload suites cover process/node/container attestation, endpoint impersonation, cross-tenant/sibling callers, cloned images/snapshots, replay/expiry, selector changes, rescheduling, streamed rotations, trust-bundle change, broker outage, and secret-zero nonclaims.

**RM-SECRETS-CONFORMANCE-0003:** Dynamic-credential suites cover database/cloud/API/SSH/certificate/token profiles, issuance partial effects, target activation, renewal ceilings, lease expiry, manual/cascade/force revocation, target outage, orphan cleanup, delegation/impersonation, and provider differentials.

**RM-SECRETS-CONFORMANCE-0004:** Non-reveal/delivery suites use secret canaries across caller/provider/agent/plugin/driver/target memory, logs, IPC, files, environment, arguments, child inheritance, dumps, telemetry, backups, output oracles, cancellation, and every claimed opaque operation.

**RM-SECRETS-CONFORMANCE-0005:** Rotation fault injection interrupts issuance, storage, distribution, reload/restart, target authentication, health, cutover, predecessor revocation/denial, rollback, fleet scheduling, expiry, mixed bundles, offline dependents, and verifies no compromised rollback.

**RM-SECRETS-CONFORMANCE-0006:** Privileged-access histories cover JIT checkout, approvals/quorum/self-conflict, brokered sessions, protocol feature restriction, recording privacy, expiry, revocation, offline break-glass, post-use rotation, native denial, emergency scope, and review.

**RM-SECRETS-CONFORMANCE-0007:** Leak/recovery suites cover repository/package/log/dump/backup/scanner findings, false positives, cloud disclosure, immediate containment, history/caches/forks, restore anti-rollback, provider migration/loss, rewrap versus rotate, deletion boundaries, and residuals.

**RM-SECRETS-CONFORMANCE-0008:** Reports bind synthetic canary corpus, provider/broker/agent/target/dependent/policy generations, platforms, clocks, network, protection claims, delivery forms, limits, expected histories, privacy/accessibility mode, and every skipped/degraded assertion without reusable secret or derived fingerprint.
