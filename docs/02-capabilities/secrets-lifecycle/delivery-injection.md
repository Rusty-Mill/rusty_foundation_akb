# Delivery, injection, and dependent adoption

**RM-SECRETS-DELIVERY-0001:** Delivery plans bind secret generation, dependent workload/process/container, target library/protocol, destination form, lifetime, file descriptor/handle/path/env/argument/stdin/memory scope, permissions, ownership, cleanup, reload, and exposure claim.

**RM-SECRETS-DELIVERY-0002:** Environment variables and command-line arguments are high-exposure legacy channels because they may propagate to children, diagnostics, process inspection, dumps, telemetry, or orchestrator state; use requires explicit product exception and evidence.

**RM-SECRETS-DELIVERY-0003:** File delivery uses private directories, non-following/handle-relative creation, restrictive native ACL/mode, atomic replacement, controlled ownership, no backup/index/sync, bounded lifetime, and deletion nonclaims. Mount projection reports update and inode/open-handle semantics.

**RM-SECRETS-DELIVERY-0004:** Handle/descriptor/IPC delivery allowlists inheritance and recipient identity, prevents unrelated child or sibling access, binds transfer acknowledgment, and defines cancellation/close/duplication semantics.

**RM-SECRETS-DELIVERY-0005:** Dependent adoption is verified by configuration generation, reload/restart transaction, readiness/health plus target authentication using the successor, not inferred from file write, event delivery, or process signal.

**RM-SECRETS-DELIVERY-0006:** Multi-secret configurations use an immutable bundle generation or staged compatibility plan so dependents never silently combine incompatible versions.
