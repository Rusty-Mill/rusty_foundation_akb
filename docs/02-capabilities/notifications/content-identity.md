# Notification content and identity

A notification request binds producer principal, product-defined semantic event identity, replacement/thread key, content revision, locale/resource context, creation and relevance interval, category, attention intent, privacy class, presentation alternatives, actions, and correlation context.

**RM-NOTIFY-CONTENT-0001:** User-visible title, body, action labels, attribution, and accessible descriptions MUST be complete localized message units produced under an explicit immutable locale/resource context.

**RM-NOTIFY-CONTENT-0002:** Content MUST define relevance start/expiry and stale-action behavior. Wall-clock scheduling and expiry MUST state timezone/calendar ambiguity policy where civil time is accepted.

**RM-NOTIFY-CONTENT-0003:** Notification identity, replacement identity, conversation/thread grouping, application activation payload, and observability correlation MUST remain distinct.

**RM-NOTIFY-CONTENT-0004:** Images, icons, sounds, URLs, markup, and attachments MUST use typed bounded representations with origin, integrity, lifetime, accessibility alternative, and platform-support evidence.

**RM-NOTIFY-CONTENT-0005:** Platform payloads are adapter output and MUST NOT be accepted as the portable source of truth or persisted as canonical product state.

Content size, action count, image dimensions, and text length are negotiated against provider limits. Truncation or omission is explicit degradation; security- or action-critical meaning cannot depend on truncated content.
