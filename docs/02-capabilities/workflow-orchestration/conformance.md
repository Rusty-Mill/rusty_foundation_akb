# Conformance

**RM-WORKFLOW-CONFORMANCE-0001:** Definition suites cover state/DAG/choice/loop/map/parallel/race/child constructs, validation failures, schemas/functions, bounds, visual/executable identifiers, publication, compatibility, and provider-language differential mappings.

**RM-WORKFLOW-CONFORMANCE-0002:** Replay suites execute every retained history across restarts/workers/platforms/toolchains, injected time/random/ID/config/network variance, snapshots/compaction/continue-as-new, nondeterministic changes, and prove no external calls/effects during replay.

**RM-WORKFLOW-CONFORMANCE-0003:** Activity/effect fault injection interrupts dispatch/accept/start/heartbeat/target effect/result/history at every boundary and covers retries/backoff, ambiguous completion, durable idempotency, fencing, worker loss, authority expiry, cancellation, and exactly-once nonclaims.

**RM-WORKFLOW-CONFORMANCE-0004:** Time/parallel suites cover monotonic/civil/calendar/DST/change/missed timers, waits and accept-before-register races, map limits, all/any/quorum/race joins, late branches, recursive children, parent close, fan-out/backpressure, and failover.

**RM-WORKFLOW-CONFORMANCE-0005:** Cancellation/compensation suites cover cooperative refusal, termination residuals, activity/task/child propagation, partial/irreversible effects, dependency ordering, retries/idempotency, failed/impossible compensation, repair, and no rollback claims.

**RM-WORKFLOW-CONFORMANCE-0006:** Version/migration suites replay old histories, mixed worker routing, recorded patches, state/event/activity/task/timer mappings, concurrent stimuli, quiescence, conditional commit, rollback limits, continue-as-new, and recovery from interrupted migration.

**RM-WORKFLOW-CONFORMANCE-0007:** Human-task/approval histories cover offer/claim/release/delegate/reassign/save/submit/decide/withdraw/expire, shared queues, offline conflicts, accessible/localized forms, privacy, authorization filtering, quorum/SoD/aliases, changed evidence, fulfillment, and revocation.

**RM-WORKFLOW-CONFORMANCE-0008:** Reports bind synthetic definitions/histories/payloads, engine/provider/toolchain/worker/policy/schema generations, clocks/calendars, topology, limits, expected effect histories, privacy/accessibility mode, and every skipped/degraded assertion without production workflow data.
