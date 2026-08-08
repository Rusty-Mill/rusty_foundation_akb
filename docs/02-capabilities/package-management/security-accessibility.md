# Security, privacy, and accessibility

**RM-PACKAGE-CROSS-0001:** Repository metadata, packages, archives, paths, links, manifests, dependency graphs, hooks, licenses, logs, native-manager output, and health signals are hostile inputs with strict parse, graph, archive, disk, process, network, time, and output bounds.

**RM-PACKAGE-CROSS-0002:** Planning is unprivileged where feasible; privileged execution receives only an authenticated, approved, expiry-bound plan and content-addressed artifacts. Elevation cannot become a general package-manager shell.

**RM-PACKAGE-CROSS-0003:** Installation prevents path traversal, link/reparse races, mount/volume substitution, case/Unicode collisions, device files, special streams, ownership/ACL/capability escalation, ambient search paths, and TOCTOU between verification and commit.

**RM-PACKAGE-CROSS-0004:** Hooks/custom actions run with the minimum declared authority and isolation available. Secrets, signing credentials, repository credentials, other users' data, and unrestricted network are unavailable by default.

**RM-PACKAGE-CROSS-0005:** Inventory, cohort, update availability, vulnerability, failure, license, device, account, and health telemetry are privacy-classified, minimized, purpose-bound, retained by policy, and export/delete capable where required.

**RM-PACKAGE-CROSS-0006:** Interactive flows expose exact publisher/package/version/channel, material plan changes, download/space, privileges, services, data/configuration effects, restart/reboot, progress, cancellation boundary, failure, recovery, and residual state to assistive technology.

**RM-PACKAGE-CROSS-0007:** Prompts are keyboard operable, focus-stable, non-color-dependent, localized, safe under bidi/untrusted labels, and do not use inaccessible countdown pressure except an explicitly justified emergency policy with deferral/recovery.

**RM-PACKAGE-CROSS-0008:** Noninteractive policy has an accessible audit/explanation surface. Administrators can distinguish not offered, not eligible, deferred, held, stale, failed, rolled back, reboot pending, unhealthy, offline, and unknown.

**RM-PACKAGE-CROSS-0009:** Observability correlates repository snapshot, plan, transaction, native manager, package generations, rollout, and recovery without logging secrets, license/private content, user paths, command output, or full inventory by default.

