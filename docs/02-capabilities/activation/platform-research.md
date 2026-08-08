# Platform research

| Concern | Windows | Linux desktop | macOS |
|---|---|---|---|
| Outgoing | `Windows.System.Launcher`, Shell/association mechanisms; file and URI launch have different objects/options/restrictions | Desktop entries/MIME apps and D-Bus activation; XDG OpenURI/OpenFile portal for sandboxed user-controlled handoff | Launch Services / workspace APIs open documents, URLs, or apps using role handlers |
| Incoming | Windows App SDK AppLifecycle/file/protocol activation, packaged/unpackaged and instance-redirection differences | desktop-entry `%` fields, D-Bus activation, portal/document tokens; desktop/compositor variance | AppKit/SwiftUI application delegate open-file/URL events and Launch Services routing |
| Defaults | User-controlled Default Apps; registration declares capabilities and settings flow changes by Windows version | `mimeapps.list` layering plus desktop policy; implementations may choose fallback | Launch Services role/default handler database and user/system policy |
| File authority | `StorageFile`/FutureAccessList/package identity paths or classic locators vary | file descriptors and document portal grants preserve sandbox authority better than `file:` | security-scoped URLs/bookmarks and sandbox entitlements where applicable |

## Portability findings

1. Windows explicitly restricts dangerous automatic file launching and generally preserves user choice of handler; modern activation and classic shell mechanisms expose different evidence.
2. Freedesktop specifications separate desktop-entry eligibility from layered MIME default/added/removed associations. XDG portals distinguish URI strings from open file descriptors and can ask the user.
3. macOS Launch Services models role handlers for document/content types and URL schemes; sandbox/security-scoped references and app delegate delivery affect authority and lifetime.
4. No platform promises that launch acceptance means content was handled. Foreground policy, existing-instance routing, chooser interaction, package updates, and acknowledgment vary.

## Primary references

- [Microsoft: Launch the default app for a URI](https://learn.microsoft.com/en-us/windows/apps/develop/launch/launch-default-app)
- [Microsoft: Launch the default app for a file](https://learn.microsoft.com/en-us/windows/apps/develop/launch/launch-the-default-app-for-a-file)
- [Microsoft: App activation](https://learn.microsoft.com/en-us/windows/apps/develop/launch/activate-an-app)
- [Freedesktop.org: MIME applications associations](https://specifications.freedesktop.org/mime-apps/latest-single/)
- [XDG Desktop Portal: OpenURI/OpenFile](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.OpenURI.html)
- [Apple: Launch Services](https://developer.apple.com/documentation/coreservices/launch_services)
