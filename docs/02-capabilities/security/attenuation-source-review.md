# Authority-attenuation source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK, authority-kind, sandbox/LSM, or deployment-context change, or 2027-02-08, whichever occurs first |
| Reviewer | Authority-attenuation capability owner |
| Open blocking findings | None for capability planning eligibility; exact mechanisms, authority kinds, and deployment assumptions remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [Access tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens), [CreateRestrictedToken](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken), and [AppContainer isolation](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation) | Microsoft platform contracts; reviewed 2026-08-08 | token identity/group/privilege/restriction structure, restricted-token derivation, and separately configured application isolation | compatible ingredients; exact Windows build, token type, privileges/groups/SIDs, integrity/AppContainer, object ACLs, handles, aliases, impersonation/session, and launch timing require evidence |
| [Linux task credentials](https://docs.kernel.org/security/credentials.html), [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html), and [LSM](https://docs.kernel.org/admin-guide/LSM/index.html) | Linux kernel and man-pages contracts; reviewed 2026-08-08 | immutable published credentials, capability decomposition/transitions, and independent mandatory-security hooks | compatible ingredients; exact kernel, user/mount/PID namespaces, capability sets, UID/GID, seccomp/LSM policy, descriptors, ambient/inheritable state, privilege, and exec boundary require evidence |
| [App Sandbox](https://developer.apple.com/documentation/security/app-sandbox) and [accessing sandboxed files](https://developer.apple.com/documentation/security/accessing-files-from-the-macos-app-sandbox) | Apple platform contracts; reviewed 2026-08-08 | entitlement/container-based constraints and explicitly scoped resource access | compatible ingredients; exact macOS/SDK, entitlement, container, security-scoped resource/bookmark, helper/XPC, codesign/team identity, user consent, alias/lifecycle, and deployment context require evidence |

**RM-SECURITY-ATTENUATE-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, authority kind, native mechanisms/configuration, identity/privilege/sandbox/namespace context, object/resource, launch/exec boundary, aliases, transfer/revocation, deployment assumptions, and artifact provenance.

**RM-SECURITY-ATTENUATE-SOURCE-0002:** Living sources MUST be release- or revision-bound where possible; an unchanged URL or mechanism name MUST NOT prove equivalent constraints, enforcement, aliases, bypass resistance, or lifecycle.

**RM-SECURITY-ATTENUATE-SOURCE-0003:** Documented native contracts, observed enforcement/bypasses, portable subset proof, policy advice, and Rusty Mill claims MUST remain separately identified.

**RM-SECURITY-ATTENUATE-SOURCE-0004:** A source, OS, kernel, SDK, sandbox/LSM, native policy, authority kind, privilege, namespace, or deployment change invalidates affected current claims until subset/enforcement/lifecycle/transfer/revocation impact is classified.
