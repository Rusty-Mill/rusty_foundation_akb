# Cryptographic operations and key-management benchmark specification

| ID | Benchmark | Measures |
|---|---|---|
| CRYPTO-BENCH-001 | Policy/provider | cold/warm discovery and plan resolution, provider/module activation and self-test cost |
| CRYPTO-BENCH-002 | Key lifecycle | generate/import/open/public-export/wrap/unwrap/rotate/revoke/destroy latency, interaction, storage and concurrency |
| CRYPTO-BENCH-003 | Hash/MAC | latency by size, incremental update/finalize, throughput, crossover, allocations/copies and parallel scaling |
| CRYPTO-BENCH-004 | KDF/password | latency, CPU/memory/parallelism, peak resident bytes, contention, cancellation and policy-upgrade cost |
| CRYPTO-BENCH-005 | AEAD | seal/open latency and throughput by size, in-place/copy/provider path, nonce allocation, invalid-tag cost and batching |
| CRYPTO-BENCH-006 | Signature/agreement | sign/verify/key agreement/KEM operations per second and latency by parameter set/provider; invalid-input cost |
| CRYPTO-BENCH-007 | Hardware/remote | queue, prompt/authentication, transport, device operation, rate limit, reconnect/session unlock and fallback-denial latency |
| CRYPTO-BENCH-008 | Rotation/migration | key cutover, data rewrap/re-encryption, overlap reads, checkpoint/restart, rollback and compromise retirement |
| CRYPTO-BENCH-009 | Sustained quality | p99/max latency, throughput stability, queue/fairness, memory, CPU, energy/thermal, provider errors over long runs |

## Comparison requirements

**RM-CRYPTO-BENCH-0001:** Policy/provider comparisons MUST bind the same workload and policy generation, provider inventory/provenance, exact resolution result, cold/warm state, activation/self-test boundary, unsupported/fallback behavior, and artifact/build context.

**RM-CRYPTO-BENCH-0002:** Key-lifecycle and transition comparisons MUST bind the same key plan, origin, protection/export/interaction policy, provider/store state, generations, rotation/migration inputs, milestones, faults, terminal/unknown outcomes, and cleanup/residual contract.

**RM-CRYPTO-BENCH-0003:** Operation comparisons MUST bind exact algorithm/parameters/encoding/purpose, key generation/origin/protection, semantic inputs and valid/invalid cases, sizes/segmentation, nonce/salt/context/AAD, buffer/aliasing/output rules, batching/concurrency, provider path, and failure oracle.

**RM-CRYPTO-BENCH-0004:** Hardware/remote and sustained comparisons MUST bind identical semantic operations plus hardware/firmware/service, session/authentication/prompt, transport/queue/rate, outage/reconnect, fallback-denial, duration/load, power/thermal, fairness, and resource-pressure conditions.

**RM-CRYPTO-BENCH-0005:** Every run MUST record policy/standards generation, provider/module/library artifact and provenance, OS/kernel/SDK, CPU/microcode/hardware/firmware, configuration/operating mode, algorithms/parameters/encodings, key origin/protection/export, random/nonce strategy, toolchain/build, workload/concurrency, stages, samples/statistics, conformance result, and scoped security/certification nonclaims without secret-derived artifacts.

**RM-CRYPTO-BENCH-0006:** A baseline is equivalent only when it preserves policy, validation, exact input/output/failure semantics, key protection/authority, nonce/counter ownership, provider mode/self-tests, fallback prohibition, and evidence boundaries; numeric budgets and native-performance, constant-time, hardware, energy, or compliance claims require reviewed representative runs.

Results report p50/p95/p99/max and distributions, bytes/second or operations/second, setup/update/finalize stages, allocations/copies, memory/queue occupancy, CPU/vector/instruction and hardware-engine use where observable, energy/thermal state, prompts, failures/rate limits, and clock methodology. Performance never substitutes for conformance or policy acceptance.
