# Platform and standards research

Research informs adapters; it does not define the portable contract.

| Platform | Candidate mechanisms | Architectural variance |
|---|---|---|
| Windows | Registry values and `RegNotifyChangeKeyValue`; application-owned files/directories | Notifications signal key/subtree categories, require notify rights, must be rearmed, and can be affected by handle/thread lifetime. Registry transactions are not a portable baseline. |
| Linux | XDG base directories; application-owned files; inotify-family observation | XDG defines preference-ordered locations but leaves application merge behavior explicit. File observers may coalesce, overflow, and expose rename/replacement races. |
| macOS | `UserDefaults` domains/notifications/KVO; application-owned files | Defaults are cached and persisted asynchronously; notifications and cross-process observation differ. Applications should not edit backing files directly. |

## Primary references

- [Microsoft: RegNotifyChangeKeyValue](https://learn.microsoft.com/windows/win32/api/winreg/nf-winreg-regnotifychangekeyvalue)
- [freedesktop.org: XDG Base Directory Specification 0.8](https://specifications.freedesktop.org/basedir-spec/0.8/)
- [Apple: UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults)
- [Apple: UserDefaults.didChangeNotification](https://developer.apple.com/documentation/foundation/userdefaults/didchangenotification)

## Research conclusions

1. Portable source identity and precedence must be product policy rather than inferred from platform.
2. Native observation cannot support a universal exact-write event stream; re-read plus snapshot comparison is the truthful common contract.
3. Configuration persistence, visibility, durability, and notification continuity are separate quality claims.
4. Adapter conformance must exercise external writers, replacement, deletion/recreation, permission changes, burst/overflow, process restart, and network/shared-filesystem nonclaims.

