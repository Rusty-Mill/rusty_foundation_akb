# Package identity and installed state

**RM-PACKAGE-IDENTITY-0001:** Package identity includes ecosystem/format, namespace/name, publisher lineage, version with format-specific comparison rules, architecture/platform/ABI, variant/features, channel, and content digest. Display name, filename, bundle identifier, product code, repository name, and signer are distinct.

**RM-PACKAGE-IDENTITY-0002:** Package relationships are typed as exact/minimum/range dependency, predependency, optional/recommended feature, conflict, replacement, supersedence, provider/virtual capability, resource/language/architecture split, or co-installability constraint.

**RM-PACKAGE-IDENTITY-0003:** A package manifest declares complete owned paths/resources, registrations, services/tasks, activation handlers, requested privileges/capabilities, hooks, configuration/data policy, restart/reboot needs, compatibility, migrations, and uninstall behavior under a versioned bounded schema.

**RM-PACKAGE-IDENTITY-0004:** Installed state is an immutable generation snapshot containing selected package identities/digests, native database identifiers/states, ownership/reference relationships, active/staged/retained generations, configuration divergence, pending operations, reboot/session requirements, and provenance.

**RM-PACKAGE-IDENTITY-0005:** `absent`, `downloaded`, `verified`, `staged`, `unpacked`, `configured`, `registered`, `active`, `superseded`, `removal-pending`, `broken`, `half-installed`, `unknown`, and native-specific states are not collapsed into installed/uninstalled.

**RM-PACKAGE-IDENTITY-0006:** Observations identify snapshot generation, enumeration boundary, native manager/store, scope, principal, target volume/root, time, and completeness. Concurrent changes produce stale/inconsistent evidence or retry, never a fabricated atomic snapshot.

**RM-PACKAGE-IDENTITY-0007:** Machine, user, session, container/image, portable directory, and application-private scopes remain distinct. Scope affects authority, visibility, ownership, activation, update policy, and removal.

**RM-PACKAGE-IDENTITY-0008:** Shared components and dependencies retain reference/ownership evidence. Removing one product cannot infer exclusive ownership from a path or label.

