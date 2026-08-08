# Benchmarks

**RM-POLICY-BENCH-0001:** Benchmarks publish hardware/OS/provider/version, policy/schema/data/function/evaluator generations, entry points, input/entity distributions, policy size/dependency/complexity, tenant/security mix, cache/compile state, concurrency, warmup, repetitions, and uncertainty.

**RM-POLICY-BENCH-0002:** Compile/validation trials measure parse/type/schema/static analysis, artifact size, memory/CPU, cold/warm, incremental updates, errors, dependency graphs, and generated/residual policy across policy scales.

**RM-POLICY-BENCH-0003:** Evaluation trials measure end-to-end and pure evaluator latency distributions, throughput, allocations/memory/CPU, function/data work, cache, batch, result/explanation size, permit/deny/error mix, and tail/adversarial inputs.

**RM-POLICY-BENCH-0004:** Complexity trials vary rules, conflicts, entity graph depth/fanout, collection cardinality, regex/text, quantifiers/comprehensions, unknowns, obligations, and output while proving configured resource bounds.

**RM-POLICY-BENCH-0005:** Distribution/change trials measure bundle validation/compile/activation, fleet propagation, mixed generations, cache invalidation, shadow old/new comparison, emergency revocation, rollback, outage/restart, and decision/enforcement convergence.

**RM-POLICY-BENCH-0006:** Enforcement trials measure decision-to-action and obligation latency, contention/races, transactions/idempotency, failures/retries/reconciliation, audit cost, and effect correctness without charging domain work to pure evaluation ambiguously.

**RM-POLICY-BENCH-0007:** Faster results that weaken fail-closed mapping, schema validation, generation binding, isolation, obligations, audit/privacy, accessibility, or correctness are failures.
