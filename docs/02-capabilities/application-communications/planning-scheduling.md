# Delivery planning, scheduling, and orchestration

**RM-COMMS-PLAN-0001:** A delivery plan freezes intent, resolved audience or resolution rule, eligibility policy, rendered content, sender/reply identity, channel order, per-channel provider/profile, timing, expiry, retry/fallback, rate/budget, tracking, and approval.

**RM-COMMS-PLAN-0002:** Transactional single-recipient, fan-out campaign, digest/batch, triggered journey, security alert, and conversation reply are distinct orchestration types with different consistency and cancellation semantics.

**RM-COMMS-PLAN-0003:** Scheduling declares time zone, civil-time ambiguity, quiet-hours adjustment, not-before, deadline/expiry, recurrence, deduplication window, missed-window behavior, and policy changes between plan and send.

**RM-COMMS-PLAN-0004:** Before every attempt, the service revalidates endpoint generation, suppression/eligibility, sender/provider authority, content expiry, tenant state, quota/rate/budget, and plan generation as required by policy.

**RM-COMMS-PLAN-0005:** Stable per-recipient/channel attempt identity prevents duplicate submission under retry. Ambiguous provider responses reconcile before retry or use provider idempotency where proven.

**RM-COMMS-PLAN-0006:** Channel fallback names triggering outcome, delay, deduplication relation, content transformation, recipient preference, cost/risk, maximum attempts, and whether later primary delivery is withdrawn or tolerated.

**RM-COMMS-PLAN-0007:** Pause/cancel/withdraw stops future locally controlled attempts but cannot retract accepted downstream delivery; outcomes report residual provider queues and delivered artifacts.
