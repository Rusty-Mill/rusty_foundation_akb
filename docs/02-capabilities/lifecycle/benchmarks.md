# Lifecycle and session benchmark specification

| Workload | Metrics |
|---|---|
| Cold/warm launch | process-start to initialized/ready/first-window/first-present/interactive milestones |
| Activation | native receipt to validation, routing, presentation, completion |
| Running-instance forwarding | latency, contention, duplicate rate, failure recovery |
| Lifecycle event | native observation to portable delivery, allocation, queue depth |
| Suspend preparation | handler latency, checkpoint bytes/time, deadline headroom |
| Resume | observation-to-reconciled readiness by affected resource class |
| Termination | query response, quiesce, drain, flush, archive publication, deadline outcome |
| Restoration | archive read/validate/migrate/apply, memory, restored partitions/windows |

Benchmarks record OS/build, session type, power source/mode, storage, product/build, profile, window count, archive schema/size, active services, telemetry configuration, cold/warm cache, and native deadlines. Results separate platform launch cost, Rusty Mill abstraction cost, application work, and first-presentation latency.

