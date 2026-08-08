# ADR-0058: Notification submission is not presentation

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native notification systems apply user permissions, focus/quiet-hours settings, rate limits, foreground policy, lock-screen privacy, platform heuristics, and retention rules after an application submits content. Platforms expose different and incomplete post-submission callbacks.

## Decision

Portable submission success means only that the selected provider accepted the request. Accepted, presented, announced, retained, remotely delivered, responded, dismissed, expired, suppressed, and unknown are distinct milestones, exposed only when supported with stated evidence quality. Notifications are never correctness or durable-message channels.

## Consequences

- Product state and required work remain independent of notification outcome.
- User/system attention policy remains authoritative.
- Observability avoids false “delivered” claims.
