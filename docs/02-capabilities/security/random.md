# `rm.security.random` — Cryptographically secure random bytes

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Security |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server, Embedded/headless |

## Purpose

Fill caller-owned memory with bytes from the operating system's cryptographically secure random source for keys, nonces, salts, tokens, and seeding approved higher-level generators.

This capability does not define random distributions, password generation, deterministic test randomness, hardware RNG access, key storage, or a general cryptographic library.

## Requirements

- **RM-SECURITY-RANDOM-0001:** Successful completion **MUST** initialize the entire requested output region with fresh output from the selected OS cryptographic source.
- **RM-SECURITY-RANDOM-0002:** Failure **MUST NOT** expose partially filled output as usable random material.
- **RM-SECURITY-RANDOM-0003:** The default provider **MUST NOT** fall back to time, process identifiers, application-supplied seeds, or a non-cryptographic generator.
- **RM-SECURITY-RANDOM-0004:** Zero-length requests **MUST** succeed without consulting or changing caller memory.
- **RM-SECURITY-RANDOM-0005:** Request length conversion and provider limits **MUST** be checked before native invocation; chunking **MAY** be used without changing exact-fill semantics.
- **RM-SECURITY-RANDOM-0006:** Provider initialization/readiness **MUST** fail closed; degraded entropy **MUST NOT** be reported as success.
- **RM-SECURITY-RANDOM-0007:** The synchronous path **MUST** be available and **MUST NOT** create or nest an async runtime.
- **RM-SECURITY-RANDOM-0008:** If a supported environment can wait materially for source readiness, the provider **MUST** either establish readiness during explicit initialization or expose a cancellable async readiness path without occupying an executor worker solely to wait where native readiness is available.
- **RM-SECURITY-RANDOM-0009:** Random bytes, intermediate state, and caller buffers **MUST NOT** appear in logs, traces, metrics, errors, panic messages, or conformance reports.
- **RM-SECURITY-RANDOM-0010:** A provider **MUST** document behavior across process fork, VM/container snapshot or clone, suspend/resume, and provider reinitialization where those events apply.
- **RM-SECURITY-RANDOM-0011:** Provider failure **MUST** preserve sanitized native diagnostics and **MUST NOT** return predictable substitute output.
- **RM-SECURITY-RANDOM-0012:** The capability **MUST NOT** claim compliance with a cryptographic certification unless the exact provider, module boundary, configuration, platform, and evidence support that claim.

## Concurrency and lifecycle

Independent fills may execute concurrently. The provider owns synchronization for native shared state. There is no portable global stream position and consumers cannot rely on output ordering between calls. Randomness quality is not tested by comparing outputs for uniqueness alone.

## Platform realization

| Platform | Candidate mechanism | Contract adaptation |
|---|---|---|
| Windows | `BCryptGenRandom` system-preferred RNG | Chunk/check native length; surface status failure |
| Linux | `getrandom` using the urandom source after initialization | Loop on partial progress and specified interruptions; handle readiness explicitly |
| macOS | `SecRandomCopyBytes` with `kSecRandomDefault` | Require successful status before exposing output |

## Error categories

Source unavailable, readiness canceled, invalid request size, provider initialization failure, provider failure with sanitized diagnostic context, and unsupported environment.

