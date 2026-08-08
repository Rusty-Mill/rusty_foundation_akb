# Security, privacy, and accessibility

**RM-BACKGROUND-QUALITY-0001:** Definitions, registration transactions, triggers, attempts, checkpoints, and updates MUST be authenticated and integrity-bound to product/package ownership, scope, principal, generation, and authority.

**RM-BACKGROUND-QUALITY-0002:** Background services MUST minimize privilege, filesystem/network/device reach, inherited handles, environment, plugins, and parser surface. Restricted execution and privilege separation are selected from actual workload needs.

**RM-BACKGROUND-QUALITY-0003:** Arguments, environment, trigger payloads, IPC, logs, metrics, crash reports, checkpoints, and results MUST not expose credentials, secrets, raw personal content, precise history, or stable identifiers by default.

**RM-BACKGROUND-QUALITY-0004:** User-visible registration, enable/disable, schedule, current activity, resource impact, errors, recovery, and removal controls MUST be localized, keyboard/screen-reader operable, high-contrast compatible, and available without relying on transient background UI.

**RM-BACKGROUND-QUALITY-0005:** A background context MUST NOT display arbitrary UI, steal focus, inject input, or prompt for credentials/permissions. Required interaction uses typed notification/activation to a current foreground session and revalidates authority there.

**RM-BACKGROUND-QUALITY-0006:** Applications MUST make ongoing background activity discoverable and stoppable and respect user/admin disablement, logout, battery/data restrictions, reduced background activity, and accessibility preferences where relevant.

**RM-BACKGROUND-QUALITY-0007:** Observability MUST correlate definition, package, registration, trigger, attempt, checkpoint, and result generations while redacting sensitive payloads and exposing sampling/loss.
