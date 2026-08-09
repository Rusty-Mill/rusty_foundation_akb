# Recipients, endpoints, and audience resolution

**RM-COMMS-RECIPIENT-0001:** Recipient identity is subject/person/account/role/endpoint scoped. Email address, phone number, push token, device, mailbox alias, or provider contact ID is a mutable endpoint, not person equality.

**RM-COMMS-RECIPIENT-0002:** Endpoint records carry verified/control evidence, tenant/account relationship, channel/provider/application/environment, locale/time zone, capability, lifecycle, sensitivity, source, generation, and last observation.

**RM-COMMS-RECIPIENT-0003:** Recycled phone numbers, reassigned mailboxes, forwarded aliases, shared devices, restored apps, rotated push tokens, account merges/splits, and endpoint reuse create new control evidence and invalidate unsafe correlations.

**RM-COMMS-RECIPIENT-0004:** Audience definitions are immutable versioned queries or exact lists with tenant/purpose, snapshot/frontier, filters, exclusions, authorization, deduplication, estimated size, limits, and approval.

**RM-COMMS-RECIPIENT-0005:** Audience resolution produces per-recipient provenance and eligibility inputs at a named instant. Dynamic groups and segments do not silently change after campaign approval without a new generation.

**RM-COMMS-RECIPIENT-0006:** Deduplication across endpoints, subjects, households, accounts, devices, and tenants uses explicit product rules and never broadens cross-tenant correlation or hides required distinct recipients.
