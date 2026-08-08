# Platform research

This mapping records native mechanisms as research, not guaranteed equivalence.

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Principal/context | SIDs, access-token user/groups/privileges, integrity/app-container data | real/effective/saved/fs UID/GID, supplementary groups, capabilities, LSM labels, keyrings | BSD IDs/groups, audit/session context, entitlements/sandbox and Authorization Services rights |
| Login/session | LSA logon sessions, sessions/desktops, lock/disconnect notifications | PAM session lifecycle plus logind/seat/session facilities where present | loginwindow/audit sessions and workspace/session notifications |
| Authentication | LSA/authentication packages and trusted credential UI/brokers | PAM stacks and provider-specific agents; desktop brokers vary | LocalAuthentication/AuthenticationServices and Security/Authorization brokers by purpose |
| Impersonation | Thread impersonation token overrides process primary token | Credential changes and fs credentials are task/thread-sensitive; service-specific delegation is common | No universal peer equivalent; privileged helpers/XPC and Authorization rights are operation-oriented |
| Credential storage | Credential Manager/DPAPI and provider-specific brokers | kernel keyrings, Secret Service/wallets, agents, provider-specific caches | Keychain and provider-specific Authentication Services |

## Portability findings

1. Windows explicitly has process primary and thread impersonation tokens; async thread migration makes ambient impersonation unsafe.
2. Linux credentials are a vector, include subjective/objective distinctions, and may interact with per-thread/process/session keyrings. PAM authentication and PAM session establishment are separate phases.
3. macOS Authorization Services obtains rights through a trusted security agent and may avoid exposing credentials to the app, but it is not a universal login-session or sandbox-compatible impersonation abstraction.
4. All platforms have provider-, policy-, desktop-, sandbox-, and deployment-dependent gaps. A truthful base contract reports them instead of promising a universal “current user,” “admin,” or “authenticate” call.

## Primary references

- [Microsoft: Parts of the Access Control Model](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-components)
- [Microsoft: Impersonation Tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/impersonation-tokens)
- [Linux kernel: Credentials in Linux](https://docs.kernel.org/security/credentials.html)
- [Linux-PAM: `pam_open_session`](https://www.man7.org/linux/man-pages/man3/pam_open_session.3.html)
- [Apple: Authorization Services](https://developer.apple.com/documentation/security/authorization-services)
- [Apple: Security framework](https://developer.apple.com/documentation/security/)
