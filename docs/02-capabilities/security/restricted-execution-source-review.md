# Restricted-execution source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK, isolation mechanism, packaging/signing/entitlement, privilege, container, or supervision change, or 2027-02-08, whichever occurs first |
| Reviewer | Restricted-execution owner |
| Open blocking findings | None for dossier reviewability; exact supported generations, compositions, privileges, and bypass probes remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| Microsoft [CreateProcess security remarks](https://learn.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights), [PROC_THREAD_ATTRIBUTE_HANDLE_LIST](https://learn.microsoft.com/en-us/windows/win32/procthread/attribute-list), [restricted tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/restricted-tokens), [job objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects), and [AppContainer isolation](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation) | Microsoft platform contracts; reviewed 2026-08-08 | controlled process creation, explicit inheritance, token restriction, containment/accounting, and app-container mechanisms | compatible ingredients; exact Windows build, privileges, package identity, mitigations, job nesting/breakaway, suspended-release sequence, and bypass behavior require composed evidence |
| Linux [`clone(2)`](https://man7.org/linux/man-pages/man2/clone.2.html), [`execve(2)`](https://man7.org/linux/man-pages/man2/execve.2.html), [`prctl(2)`](https://man7.org/linux/man-pages/man2/prctl.2.html), [`seccomp(2)`](https://man7.org/linux/man-pages/man2/seccomp.2.html), [namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html), [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html), and [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) | Linux man-pages/kernel contracts; reviewed 2026-08-08 | controlled clone/exec, credential/no-new-privileges, syscall filtering, namespace isolation, capability constraints, and resource/descendant control | compatible ingredients; exact kernel/libc/LSM/container/user-namespace/cgroup configuration, ordering, privilege, inherited descriptors, exec handshake, and bypasses require evidence |
| Apple [App Sandbox](https://developer.apple.com/documentation/security/app-sandbox), [XPC](https://developer.apple.com/documentation/xpc), and [security-scoped resources](https://developer.apple.com/documentation/security/accessing-files-from-the-macos-app-sandbox) | Apple platform contracts; reviewed 2026-08-08 | entitlement/container isolation, helper/service boundary, and scoped resource access | compatible ingredients; entitlements are signing-time constraints and cannot be invented dynamically; exact macOS/SDK, signing, helper/XPC topology, inheritance, supervision, and residual ambient access require evidence |

No source establishes that one mechanism equals the portable service. Rusty Mill's claim is the verified composition and its disclosed gaps.

**RM-SECURITY-RESTRICTED-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, native APIs/mechanisms, artifact/signing/package identity, privileges, sandbox/container/LSM state, configuration/order, manifest, supervision topology, and artifact provenance.

**RM-SECURITY-RESTRICTED-SOURCE-0002:** Living sources MUST be release- or revision-bound where possible; familiar mechanism names or unchanged URLs MUST NOT prove unchanged behavior, privilege requirements, composition, or bypass resistance.

**RM-SECURITY-RESTRICTED-SOURCE-0003:** Documented native contracts, observed composed behavior, adversarial bypass results, platform limitations, Rusty Mill guarantees, and deployment threat assumptions MUST remain separately identified.

**RM-SECURITY-RESTRICTED-SOURCE-0004:** A platform, mechanism, policy, signing/entitlement, privilege, packaging, container, service-manager, supervision, or dependency change invalidates affected evidence until pre-release, inheritance, enforcement, lifecycle, degradation, and cleanup impact is classified.
