# Platform and standards research

- [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321.html) defines SMTP relay and formal responsibility handoff; [RFC 3461](https://www.rfc-editor.org/rfc/rfc3461.html) defines delivery-status notification requests. Neither proves reading or comprehension.
- [RFC 8058](https://www.rfc-editor.org/rfc/rfc8058.html) defines one-click mailing-list unsubscribe using signed headers and HTTPS POST; [RFC 2369](https://www.rfc-editor.org/rfc/rfc2369.html) defines list command headers.
- [DKIM RFC 6376](https://www.rfc-editor.org/rfc/rfc6376.html), [SPF RFC 7208](https://www.rfc-editor.org/rfc/rfc7208.html), and [DMARC RFC 7489](https://www.rfc-editor.org/rfc/rfc7489.html) provide different email authentication/alignment evidence and do not establish content truth or user consent.
- [RFC 8030](https://www.rfc-editor.org/rfc/rfc8030.html), [RFC 8291](https://www.rfc-editor.org/rfc/rfc8291.html), and [RFC 8292](https://www.rfc-editor.org/rfc/rfc8292.html) define Web Push, payload encryption, and voluntary application-server identification.
- Apple's [remote notification server guidance](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server) separates provider server, APNs, device, OS, and app and notes storage/coalescing behavior.
- Firebase documents [message lifespan](https://firebase.google.com/docs/cloud-messaging/customize-messages/setting-message-lifespan) and [collapsible messages](https://firebase.google.com/docs/cloud-messaging/customize-messages/collapsible-message-types), including that provider acceptance is not device delivery and order is not guaranteed.
- Twilio's [outbound message status guidance](https://www.twilio.com/docs/messaging/guides/track-outbound-message-status) exposes queued/sent/delivered/undelivered/read provider and carrier evidence with channel-specific callbacks.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) informs accessible HTML and interactive communication content; channel/client limitations remain explicit.

**RM-COMMS-RESEARCH-0001:** Rusty Mill maps protocol and provider milestones at their exact boundary and never promotes a weaker status to recipient delivery or human engagement.

**RM-COMMS-RESEARCH-0002:** Windows, Linux, and macOS offer native notification presentation and application activation, but remote push, email, SMS, preference governance, and provider delivery remain application services above native attention capabilities.
