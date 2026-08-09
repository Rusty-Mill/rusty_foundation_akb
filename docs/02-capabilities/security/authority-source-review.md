# Authority source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK, policy/provider, sandbox/deployment, IPC transfer, or authority-kind change, or 2027-02-08, whichever occurs first |
| Reviewer | Authority semantics owner |
| Open blocking findings | None for dossier reviewability; exact mechanisms, versions, deployment contexts, authority kinds, and provider matrices remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| Microsoft [Access Tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens) and [`CreateRestrictedToken`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken) | Microsoft platform contracts; reviewed 2026-08-08 | process/thread security contexts contain typed SIDs, groups, privileges, restrictions, and token state; restricted tokens can disable/delete selected inputs | a token is not the portable authority model; exact token type, impersonation level, privileges, restricting SIDs, integrity/AppContainer state, handles, object ACLs, and process context require evidence |
| Microsoft [`AuthzAccessCheck`](https://learn.microsoft.com/en-us/windows/win32/api/authz/nf-authz-authzaccesscheck) and [`AuthzCachedAccessCheck`](https://learn.microsoft.com/en-us/windows/win32/api/authz/nf-authz-authzcachedaccesscheck) | Microsoft evaluation contracts; reviewed 2026-08-08 | requested masks are evaluated against client context and security descriptors; selected results may be cached with bound inputs/lifetimes | API success is not access grant or later operation success; conditional unknowns, cached context/descriptor lifetime, central policy, object changes, and native operation races remain explicit |
| Linux kernel [Credentials in Linux](https://docs.kernel.org/security/credentials.html) | Linux kernel contract; reviewed 2026-08-08 | task/object credentials, immutable published credential structures, capabilities/bounding sets, LSM labels, and open-file credentials affect enforcement | UID/GID/capability sets are not a universal authority descriptor; filesystem/socket/task/key/namespace/LSM and exec inheritance semantics vary by operation and kernel/configuration |
| Linux man-pages [`unix(7)`](https://man7.org/linux/man-pages/man7/unix.7.html) and [`pidfd_getfd(2)`](https://man7.org/linux/man-pages/man2/pidfd_getfd.2.html) | Linux userspace/kernel interface documentation; reviewed 2026-08-08 | descriptor passing and cross-process duplication have concrete ownership, credential, permission, namespace, and lifetime behavior | SCM_RIGHTS duplicates an open-file reference rather than portable policy; message authentication, audience, ancillary truncation, close-on-exec, cancellation, and receiver inventory require explicit protocol evidence |
| Apple [App Sandbox](https://developer.apple.com/documentation/security/app-sandbox) and [security-scoped bookmark access](https://developer.apple.com/documentation/professional-video-applications/enabling-security-scoped-bookmark-and-url-access) | Apple platform contracts; reviewed 2026-08-08 | entitlements/container policy constrain access and security-scoped resources extend selected file access | entitlement or bookmark presence is not general identity/authority; exact app identity, entitlement, user selection, scope, staleness, start/stop lifecycle, XPC boundary, distribution, and OS generation require evidence |

**RM-SECURITY-AUTHORITY-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, provider and artifact, authority/resource kind, identity/security context, policy/evaluator, native object/control, sandbox/container/namespace, transport, deployment, clock, lifecycle, toolchain, and provenance.

**RM-SECURITY-AUTHORITY-SOURCE-0002:** Platform documentation, configured policy, provider observation, portable guarantees, domain-operation evidence, and security claims MUST remain separately identified.

**RM-SECURITY-AUTHORITY-SOURCE-0003:** Token/credential/entitlement/bookmark/descriptor possession, access-query success, cached decision, transfer acceptance, and native operation success MUST NOT be treated as mutually equivalent evidence.

**RM-SECURITY-AUTHORITY-SOURCE-0004:** Living sources and mutable platform policy/mechanism catalogs MUST be version- and deployment-bound; changes invalidate affected authority, inheritance, transfer, revocation, and performance evidence.

**RM-SECURITY-AUTHORITY-SOURCE-0005:** Native mechanisms MAY substantiate only the exact dimensions and contexts they enforce; unsupported aliases, ambient inputs, inheritance paths, bypasses, partitions, and already-started effects remain explicit nonclaims.
