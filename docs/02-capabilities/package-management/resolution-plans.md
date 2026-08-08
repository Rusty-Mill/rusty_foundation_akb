# Resolution and deployment plans

**RM-PACKAGE-PLAN-0001:** Resolution input binds installed-state and repository-snapshot generations, requested goals, holds/pins/channels, target scope/platform/architecture, feature choices, compatibility policy, disk/network/time budgets, restart/reboot constraints, and authority ceiling.

**RM-PACKAGE-PLAN-0002:** The resolver evaluates format-specific version ordering, dependencies, alternatives/providers, conflicts/replacements, architecture/co-installability, platform applicability, already-running generations, and policy. It never interprets a human version string with another ecosystem's rules.

**RM-PACKAGE-PLAN-0003:** Resolution returns zero, one, or multiple candidate plans with deterministic explanation: selected versions/digests/sources, additions/upgrades/downgrades/removals/holds, dependency reasons, alternatives, conflicts, downloads, space, privileges, hooks, restart/reboot, risk, and unresolved facts.

**RM-PACKAGE-PLAN-0004:** A plan is immutable and identifies all package/artifact/metadata digests, operation ordering/graph, expected installed precondition generation, native manager/provider, scope, authorities, user choices, hooks, service/data actions, recovery policy, and expiry.

**RM-PACKAGE-PLAN-0005:** Execution revalidates every precondition. Installed state, repository/trust/policy generation, artifact, authority, free space, target volume, session, or native manager change makes the plan stale or requires explicit re-resolution.

**RM-PACKAGE-PLAN-0006:** The executor cannot add packages, select a new version/source, convert an upgrade to downgrade, remove conflicts, enable a feature, broaden scope, run undeclared hooks, or accept new licenses outside the authorized plan.

**RM-PACKAGE-PLAN-0007:** User/admin approval presents the complete material diff and separates license acceptance, privilege elevation, service interruption, data migration, restart, reboot, removal, downgrade, and telemetry choices. Approval is plan-digest and expiry bound.

**RM-PACKAGE-PLAN-0008:** Resolver nondeterminism, provider-specific choices, and policy tie-breaking are recorded. Re-running against identical inputs must reproduce the plan or explain provider/environment variance.

