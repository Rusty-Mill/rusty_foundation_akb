# Bootstrap and workload identity

**RM-SECRETS-BOOTSTRAP-0001:** Bootstrap plans bind workload/application identity, runtime/node/container/process evidence, expected binary/package, tenant/environment, broker endpoint, trust material, policy generation, freshness, replay protection, and requested secret class.

**RM-SECRETS-BOOTSTRAP-0002:** Platform or workload attestation establishes issuer-qualified evidence only; broker authorization independently maps it to secret or credential issuance.

**RM-SECRETS-BOOTSTRAP-0003:** Local workload APIs authenticate callers through protected endpoint access plus out-of-band process/runtime evidence, isolate workloads, bind returned identities to exact trust domains/audiences, and stream full generation updates.

**RM-SECRETS-BOOTSTRAP-0004:** Unavoidable bootstrap tokens are single-purpose, audience-bound, short-lived, one-time or tightly replay-limited, minimally distributed, protected at rest/in transit, and immediately exchanged for narrower renewable identity.

**RM-SECRETS-BOOTSTRAP-0005:** Machine images, snapshots, cloned disks, container layers, environment variables, source repositories, user-data scripts, command lines, and global configuration are prohibited as unqualified long-lived secret-zero channels.

**RM-SECRETS-BOOTSTRAP-0006:** Node/workload re-registration, migration, rescheduling, restore, clock rollback, attestor update, and compromised bootstrap authority create new generations and reconcile all issued credentials.
