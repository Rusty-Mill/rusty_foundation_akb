# Clipboard service

| Field | Value |
|---|---|
| Status | Draft platform service 0.1.0 |

**RM-TRANSFER-CLIPBOARD-0001:** A clipboard channel is explicitly selected (`general`, `primary-selection`, or a platform extension) with availability, ownership, persistence, history, synchronization, and privacy properties. Channels are not assumed equivalent across platforms.

**RM-TRANSFER-CLIPBOARD-0002:** Publishing atomically replaces one channel with an immutable offer generation and returns an ownership lease. Success states whether content is source-owned/lazy, materialized by the system, or persisted beyond source lifetime.

**RM-TRANSFER-CLIPBOARD-0003:** Ownership loss, replacement, source exit, session lock/logout, remote-session change, and system persistence are observable where supported. A lease never promises the OS will preserve data after ownership loss.

**RM-TRANSFER-CLIPBOARD-0004:** Reading returns current offer metadata and generation; materialization revalidates that generation or reports replacement/stale rather than reading a different clipboard implicitly.

**RM-TRANSFER-CLIPBOARD-0005:** Read/write operations are user-action scoped by default. Background polling, history enumeration, change monitoring, and content-pattern detection require explicit product purpose, authority, privacy review, and platform evidence.

**RM-TRANSFER-CLIPBOARD-0006:** Sync APIs do not block a UI thread on another process's lazy rendering, conversion, network access, or unbounded payload. Async materialization supports progress, deadlines, cancellation, and source failure.

**RM-TRANSFER-CLIPBOARD-0007:** Clipboard persistence/synchronization across devices or sessions is an OS/provider property disclosed per offer. Sensitive content defaults to nonpersistent/non-synchronized where the platform supports policy; inability is visible.

**RM-TRANSFER-CLIPBOARD-0008:** Clear is a conditional generation operation where supported and never claims erasure from clipboard history, remote peers, past readers, or source applications.

**RM-TRANSFER-CLIPBOARD-0009:** Copy and paste preserve accessibility action equivalence, selection/focus semantics, success/failure feedback, and keyboard-only operation. Silent paste into a privileged/destructive context is prohibited by product policy.

