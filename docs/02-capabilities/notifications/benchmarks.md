# Notification benchmark specification

| Benchmark | Measures |
|---|---|
| Submission | construct/validate/serialize/native-accept latency and allocation by content/features |
| Update/withdraw | replacement, progress, badge, and removal acceptance latency, coalescing and rate-limit behavior |
| Activation | user response receipt to lifecycle activation parse, instance routing, domain validation, and acknowledged outcome |
| Scheduling | requested versus observable trigger eligibility under wake/sleep/reboot/clock/timezone scenarios, without claiming presentation |
| Burst/load | bounded memory/queues, acceptance/rejection, coalescing, CPU, and recovery across producers/categories |
| Startup/shutdown | registration/reconciliation cost, pending/history enumeration where supported, bounded final submission |
| Accessibility | announcement latency/repetition and interaction completion under representative assistive technology |

Results report p50/p95/p99/max, allocations, payload bytes, CPU, queue occupancy, accepted/rejected/unknown counts, update coalescing, and activation latency boundaries. Runs disclose OS/desktop/provider, app packaging/identity, permission/settings/focus/lock/session, locale/accessibility, content/action/image sizes, scheduling mode, rate policy, and process lifecycle. Human/system presentation latency is reported only when observable and never treated as guaranteed provider delivery.
