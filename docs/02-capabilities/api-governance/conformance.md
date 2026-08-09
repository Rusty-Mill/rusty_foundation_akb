# Conformance

**RM-API-GOV-CONFORMANCE-0001:** A provider proves contract release identity and exercises success, every declared error, authorization denial, validation boundaries, cancellation/deadline, concurrency, idempotency, pagination, quota, and long-running transitions.

**RM-API-GOV-CONFORMANCE-0002:** Consumer tests use provider-independent vectors including absent/null/default, unknown fields/enums, additive/removal changes, reordered pages, duplicate delivery, partial streams, retry guidance, and deprecated elements.

**RM-API-GOV-CONFORMANCE-0003:** Differential tests compare generated and handwritten adapters plus HTTP/RPC/event bindings against the same logical vectors and report semantic loss.

**RM-API-GOV-CONFORMANCE-0004:** Change-analysis fixtures contain known safe, unsafe, conditional, and consumer-specific changes and fail closed when a relevant axis cannot be evaluated.

**RM-API-GOV-CONFORMANCE-0005:** Lifecycle histories cover notification loss, unknown consumers, stale SDKs, rollback, emergency retirement, withdrawn deprecation, and attempted identifier reuse.

**RM-API-GOV-CONFORMANCE-0006:** Evidence records source/release/tool/provider/consumer generations, environment, policy, seeds, clocks, fault schedule, results, unsupported cases, and artifact digests.
