# Notification platform research

| Platform | Native mechanisms | Architectural consequence |
|---|---|---|
| Windows | Windows App SDK app notifications, tags/groups, expiration, scheduling, progress, buttons/input, app lifecycle activation, optional WNS push | Packaging/registration and app model affect features; acceptance/history/activation differ; foreground activation behavior and push prerequisites are provider qualities |
| Linux | Freedesktop.org Notifications D-Bus service with capabilities/actions/replacement/close signals; XDG Desktop Portal notification API and activation tokens | Server capabilities and hints are negotiated and desktop-specific; IDs are server/application scoped; portal is preferred under sandbox policy; presentation is compositor/server controlled |
| macOS | UserNotifications authorization/settings, categories/actions, local scheduling, delivered/pending management, responses, optional APNs transport | Authorization/settings are explicit and mutable; categories/actions require registration; system decides presentation; local notification and remote APNs transport are separate |

## Primary sources

- Microsoft, [Windows notifications overview](https://learn.microsoft.com/windows/apps/develop/notifications/), [app notification content](https://learn.microsoft.com/windows/apps/develop/notifications/app-notifications/app-notifications-content), [management](https://learn.microsoft.com/windows/apps/develop/notifications/app-notifications/manage-app-notifications), and [activation](https://learn.microsoft.com/windows/apps/develop/launch/activate-an-app)
- freedesktop.org, [Desktop Notifications Specification](https://specifications.freedesktop.org/notification/latest-single/)
- XDG Desktop Portal, [Notification interface](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Notification.html)
- Apple, [UserNotifications](https://developer.apple.com/documentation/usernotifications), [asking permission](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications), [notification categories and actions](https://developer.apple.com/documentation/usernotifications/declaring-your-actionable-notification-types), and [handling responses](https://developer.apple.com/documentation/usernotifications/handling-notifications-and-notification-related-actions)

## Synthesis

All targets let applications request system-managed notification presentation, but feature sets, permissions, settings, replacement, history, action activation, and scheduling differ materially. The common value is a typed request and evidence model that preserves user policy and unknown outcomes. Cloud push is not part of local notification presentation.
