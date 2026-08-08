# Hooks, services, configuration, and data

**RM-PACKAGE-HOOK-0001:** Install/upgrade/remove scripts, custom actions, triggers, and declarative registrations are untrusted privileged package behavior. Each is declared with phase, interpreter/runtime, principal, authority, filesystem/network/device access, inputs, outputs, timeout, restartability, idempotency, and rollback/recovery contract.

**RM-PACKAGE-HOOK-0002:** Declarative native registration is preferred to arbitrary hooks. Hooks cannot silently download executable content, alter unrelated packages, escape target roots, obtain ambient credentials, or bypass the deployment plan.

**RM-PACKAGE-HOOK-0003:** Hook output and exit status are bounded evidence. Timeout, signal/crash, reboot request, partial side effect, dependency absence, and unknown completion remain distinct; retry requires declared idempotency or reconciliation.

**RM-PACKAGE-SERVICE-0001:** Service/task/handler activation changes coordinate with background-service and activation generations. Updates define stop/drain/coexist/restart/readiness behavior and preserve old admission until the new generation's commit boundary.

**RM-PACKAGE-DATA-0001:** Executable/package content, administrator configuration, user preferences, secrets, mutable application data, caches, logs, schemas, and migration checkpoints have separate ownership and retention policy.

**RM-PACKAGE-DATA-0002:** Configuration-file merge or replacement exposes base/local/new versions, conflicts, chosen result, provenance, permissions, secret handling, and recovery copy. Silent overwrite of administrator/user changes is prohibited.

**RM-PACKAGE-DATA-0003:** Data migrations are versioned, separately authorized, restartable or transactional, backed up where policy requires, forward/backward compatibility classified, and health-gated. Package rollback does not imply data downgrade.

**RM-PACKAGE-DATA-0004:** Removal distinguishes uninstall, purge, disable, retain-user-data, retain-shared-data, and secure-erasure request. It deletes only proven owned resources under the plan and reports residual state.

