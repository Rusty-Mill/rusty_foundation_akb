# Background services and durable scheduling conformance specification

| Area | Required evidence |
|---|---|
| Definition/registration | workload kinds, immutable package binding, namespace collision, transactional register/enable/disable/remove, policy/admin edits, partial commit |
| Scope/authority | system/user/session/container contexts, principal/credential provenance, least privilege, no interactive assumptions, delegation boundary |
| Service activation | endpoint reservation, duplicate/concurrent activation, instance policy, explicit readiness, request cancellation/orphaning, crash/backoff/circuit behavior |
| Scheduling | instant/interval/civil/event/maintenance schedules, DST gap/overlap, clock/time-zone/rule change, sleep/downtime, missed/coalesced/deferred/expired policy |
| Triggers | duplicate/loss/coalesce/reorder/overflow, registration races, hostile payload, broker restart, state reconciliation, wake authorization |
| Attempts/results | attempt generations, work claims/idempotency, checkpoints, overlap, ambiguous effects, bounded retry/poison handling, result access/retention |
| Budgets | CPU/memory/I/O/network/wakeup/energy limits, expiration, dependency loss, foreground fairness, abrupt termination and checkpoint recovery |
| Update/security/UX | generation promotion/coexist/drain/rollback/removal, signing/ownership, secret/log redaction, accessible localized controls/status/recovery |

Fixtures cover demand/persistent/user-session services, one-shot/recurring/maintenance jobs, boot/login/network/device/socket triggers, multiple users/sessions, restricted principals, missing profiles/mounts/network, clock/DST/tzdb changes, sleep/reboot/downtime, duplicate/missed triggers, overlaps, crash loops, quota expiration, package updates/rollback, partial registration, administrative edits, and abrupt power loss.

Reports bind OS/build/service manager/scheduler, product/package/definition/registration/trigger/attempt/checkpoint generations, scope/principal/security context, native configuration normalization, authority/policy, schedule time data, resource constraints, restart/retry/overlap/update policy, dependencies, milestones, and every durability/timing/exactly-once nonclaim. Fault injection covers forged definitions, identifier collision, stale generation, trigger storm/loss, clock step, work-claim race, corrupt checkpoint, service-manager restart, update crash, rollback incompatibility, and teardown races.
