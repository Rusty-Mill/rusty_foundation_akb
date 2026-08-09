# In-application inbox and conversations

**RM-COMMS-INAPP-0001:** In-app message identity binds tenant/account/recipient, conversation/thread, sender, content generation, created/effective/expiry time, visibility, read/ack state, actions, retention, and authorization.

**RM-COMMS-INAPP-0002:** Stored in service, synchronized locally, listed, rendered, presented, marked read, acknowledged, archived, deleted, and acted are distinct milestones; native push is only an optional invalidation/attention hint.

**RM-COMMS-INAPP-0003:** Pagination and unread counters bind stable snapshots/frontiers or disclose drift. Read/ack updates are idempotent, multi-device reconciled, and do not claim comprehension.

**RM-COMMS-INAPP-0004:** Conversation membership, sender authority, audience changes, tenant boundaries, participant blocking, moderation, retention, and export are enforced on every read/write and attachment fetch.

**RM-COMMS-INAPP-0005:** Inbound email/SMS/provider replies bind original delivery/conversation where proven, sender endpoint/control evidence, channel metadata, signature/webhook authenticity, parser limits, content inspection, deduplication, and ambiguity handling.

**RM-COMMS-INAPP-0006:** Reply, action, and preference links are untrusted requests. Domain effects require fresh authentication/authorization, CSRF/replay protection, explicit context, idempotency, and result evidence.
