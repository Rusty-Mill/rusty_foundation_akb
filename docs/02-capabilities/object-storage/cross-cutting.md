# Object-storage cross-cutting requirements

**RM-OBJECT-CROSS-0001:** Public access is denied by default at account/namespace/object/network layers. Identity, policy, ACL, delegated access, service roles, replication/lifecycle principals, and break-glass administration remain distinct, least privilege, generation-bound, and audited.

**RM-OBJECT-CROSS-0002:** Encryption claims name transport and at-rest coverage, provider/customer/application keys and generations, envelope/context, metadata/checksum exposure, multipart/copy/replication/cache/backup handling, rotation/re-encryption, restore, key loss, and plaintext boundaries.

**RM-OBJECT-CROSS-0003:** Security review covers key/path/URI confusion, canonical-signing differentials, SSRF/redirects, unauthorized copy source, generation races, multipart substitution, checksum confusion, malicious metadata/content, public/cache leakage, dedup side channels, retention bypass, lifecycle deletion, and resource exhaustion.

**RM-OBJECT-CROSS-0004:** Privacy classifies keys, metadata/tags, contents, versions, inventories/events, access logs, delegated URLs, digests/equality leakage, replicas/caches/backups, retention/holds, and erasure residuals by tenant/purpose/region.

**RM-OBJECT-CROSS-0005:** Observability correlates logical/attempt identity, provider/account/namespace/key hash or approved identifier, exact generation, upload/part/range, condition, bytes/checksums/digests, encryption/class, latency/throttle/retry, replication/lifecycle/recovery, cost, and telemetry loss without sensitive data by default.

**RM-OBJECT-CROSS-0006:** User-visible uploads/downloads/deletes/restores/shares/retention expose destination/recipient, size/type, progress, verification, version/conflict, cost/network, cancellation/unknown state, retention/data-loss, and recovery accessibly and locally; opaque identifiers have safe bidi/spoofing-resistant display.

**RM-OBJECT-CROSS-0007:** Keys, digests, validators, metadata protocol, sizes, ranges, clocks, and signing are locale-independent. Human names/times/units/messages use explicit locale/Unicode/time-zone contexts without altering canonical wire identities.

