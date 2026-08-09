# Offline reads, writes, and optimistic effects

**RM-APP-SYNC-OFFLINE-0001:** Every operation declares offline read/write eligibility, maximum staleness, required local evidence, authority lease or prohibition, validation subset, conflict likelihood, and user-visible status.

**RM-APP-SYNC-OFFLINE-0002:** Local-first reads expose source replica, observation frontier/time, pending local changes, conflict state, completeness/selection, and freshness without presenting cached data as current authoritative truth.

**RM-APP-SYNC-OFFLINE-0003:** A durable local write records original intent, normalized mutation, actor/subject, authority evidence, causal base, stable idempotency/effect identity, dependencies, expiry, and reconciliation policy.

**RM-APP-SYNC-OFFLINE-0004:** Optimistic UI state is a reversible projection milestone, not proof of remote acceptance or domain completion. Confirmed, pending, blocked, conflicted, rejected, compensated, and locally discarded states remain distinguishable and accessible.

**RM-APP-SYNC-OFFLINE-0005:** Operations requiring fresh authorization, global uniqueness, scarce inventory, money movement, secret use, irreversible external effects, or current safety state default to online/fenced execution unless a product RFC proves bounded delegated authority.

**RM-APP-SYNC-OFFLINE-0006:** Rejection or changed authority preserves audit and user intent as policy permits, offers repair/rebase/appeal choices, and never silently forges success or deletes unsynchronized work.
