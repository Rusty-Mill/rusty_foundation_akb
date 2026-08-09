# Email binding

**RM-COMMS-EMAIL-0001:** Email binding states envelope sender/recipients, header From/To/Cc/Reply-To, message/thread IDs, subject, MIME structure, charset/transfer encoding, text/HTML alternatives, attachments/inline assets, list headers, priority, and size limits.

**RM-COMMS-EMAIL-0002:** Sender identity binds exact domain/mailbox, DKIM key/profile, SPF-authorized path, DMARC alignment/policy, return path, provider/account/IP pool, reputation class, and rotation/revocation evidence.

**RM-COMMS-EMAIL-0003:** SMTP/provider acceptance transfers responsibility at a named hop only. Relayed, queued, delivered-to-mailbox, quarantined/spam, bounced, displayed, opened, clicked, replied, and acted remain distinct.

**RM-COMMS-EMAIL-0004:** Enhanced status/DSN and provider bounce/complaint classifications map loss-consciously with original recipient/attempt correlation, authenticity, duplicate/reorder handling, permanent/transient policy, and suppression effects.

**RM-COMMS-EMAIL-0005:** Mailing-list/promotional profiles include standards-compatible unsubscribe metadata and an accessible visible mechanism. One-click endpoints are integrity-protected, idempotent, token-scoped, CSRF/automation safe, and do not require login where policy requires frictionless withdrawal.

**RM-COMMS-EMAIL-0006:** Open pixels and link rewriting are optional privacy-sensitive observations affected by proxying, scanners, blocking, prefetched content, shared devices, and security gateways; they never prove human reading or intent.

**RM-COMMS-EMAIL-0007:** Inbound replies, auto-replies, loops, DSNs, abuse reports, and out-of-office messages use authenticated bounded parsing, loop headers/state, attachment/link inspection, threading policy, and quarantine.
