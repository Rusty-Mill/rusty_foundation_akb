# Cryptographic operations and key-management benchmark specification

| Benchmark | Measures |
|---|---|
| Policy/provider | cold/warm discovery and plan resolution, provider/module activation and self-test cost |
| Key lifecycle | generate/import/open/public-export/wrap/unwrap/rotate/revoke/destroy latency, interaction, storage and concurrency |
| Hash/MAC | latency by size, incremental update/finalize, throughput, crossover, allocations/copies and parallel scaling |
| KDF/password | latency, CPU/memory/parallelism, peak resident bytes, contention, cancellation and policy-upgrade cost |
| AEAD | seal/open latency and throughput by size, in-place/copy/provider path, nonce allocation, invalid-tag cost and batching |
| Signature/agreement | sign/verify/key agreement/KEM operations per second and latency by parameter set/provider; invalid-input cost |
| Hardware/remote | queue, prompt/authentication, transport, device operation, rate limit, reconnect/session unlock and fallback-denial latency |
| Rotation/migration | key cutover, data rewrap/re-encryption, overlap reads, checkpoint/restart, rollback and compromise retirement |
| Sustained quality | p99/max latency, throughput stability, queue/fairness, memory, CPU, energy/thermal, provider errors over long runs |

Results report p50/p95/p99/max and distributions, bytes/second or operations/second, setup/update/finalize stages, allocations/copies, memory/queue occupancy, CPU/vector/instruction and hardware-engine use where observable, energy/thermal state, prompts, failures/rate limits, and clock methodology. Runs disclose machine/CPU/microcode, OS/build, provider/module/version/configuration, algorithm/parameters/encoding, key origin/protection/export policy, input distributions, concurrency/batching, random/nonce strategy, warmup/cache state, power mode, and certification/side-channel nonclaims. Performance never substitutes for conformance or policy acceptance.
