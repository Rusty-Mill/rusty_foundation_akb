# Security platform research

**Status:** Research input; native names are not portable contracts

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Execution identity/context | Process or thread access tokens containing SIDs, groups, privileges, owner/default DACL, restrictions, and impersonation state | Task credentials containing identity and capability state; published credential sets are treated as immutable | Process identity, code-signing identity, entitlements, discretionary permissions, privacy controls, and sandbox state |
| Attenuation/isolation | Restricted tokens; AppContainer or LPAC package and capability SIDs | UID/GID transitions, Linux capabilities, namespaces, seccomp, and Linux Security Modules | App Sandbox entitlements, containers, security-scoped access, and separately entitled helpers/XPC services |
| Access evaluation | Object manager access checks and Authz APIs | Operation-time discretionary checks plus capability and LSM hooks | Operation-time discretionary and mandatory controls plus App Sandbox enforcement |
| Secure random | `BCryptGenRandom` with the system-preferred RNG | `getrandom`; initialization and partial/interrupted behavior depend on request and flags | `SecRandomCopyBytes` with the default generator |

## Findings

1. No single cross-platform scalar faithfully represents an execution context. The portable model must preserve typed, provider-scoped facts and explicit uncertainty.
2. Native restriction mechanisms can intersect multiple identities and constraints. Rusty Mill therefore models grants and constraints separately and composes them by intersection.
3. Sandboxing is a deployment and process-creation concern, not merely a boolean property of an already running process.
4. Native access-query APIs do not eliminate check/use races. Actual operations remain authoritative.
5. Secure-random APIs differ in size, initialization, interruption, and failure behavior. The portable contract must provide exact-fill or explicit failure rather than expose partially initialized output.

## Primary sources

- Microsoft: [Access Tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens), [Restricted Tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/restricted-tokens), [Checking Access with Authz API](https://learn.microsoft.com/en-us/windows/win32/secauthz/checking-access-with-authz-api), [AppContainer isolation](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation), and [`BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom)
- Linux kernel: [Task credentials](https://docs.kernel.org/security/credentials.html) and [Linux Security Modules](https://docs.kernel.org/admin-guide/LSM/index.html)
- Linux man-pages: [capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html) and [getrandom(2)](https://man7.org/linux/man-pages/man2/getrandom.2.html)
- Apple: [App Sandbox](https://developer.apple.com/documentation/security/app-sandbox), [accessing sandboxed files](https://developer.apple.com/documentation/security/accessing-files-from-the-macos-app-sandbox), and [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:))

