# Secure-random source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK, provider/module/configuration, or clone-lifecycle change, or 2027-02-08, whichever occurs first |
| Reviewer | Secure-random capability owner |
| Open blocking findings | None for capability planning eligibility; exact supported generations and module boundaries remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [`BCryptGenRandom`](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) | Microsoft platform contract; reviewed 2026-08-08 | system-preferred cryptographic RNG selection, buffer/length/status contract, provider-handle behavior | compatible; exact Windows build, flags, module boundary/configuration, validation mode, virtualization, and failure injection require evidence |
| [`getrandom`](https://man7.org/linux/man-pages/man2/getrandom.2.html) and [Linux random subsystem](https://docs.kernel.org/admin-guide/kernel-parameters.html) | Linux man-pages plus kernel documentation; reviewed 2026-08-08 | kernel random source, initialization/readiness behavior, partial/interrupted/size semantics, and flag-dependent behavior | compatible; exact kernel/libc, flags, boot/namespace/VM state, request sizes, FIPS/provider configuration, and clone lifecycle must be bound |
| [`SecRandomCopyBytes`](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)) | Apple Security framework contract; reviewed 2026-08-08 | default generator selection, output buffer/count, and status-based success/failure | compatible; exact macOS/SDK, framework/module boundary, sandbox, validation mode, virtualization, lifecycle, and fault behavior require evidence |

**RM-SECURITY-RANDOM-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, native API, provider/module/configuration, flags, request/chunk policy, boot/readiness, virtualization/clone, sandbox, validation mode, and artifact provenance.

**RM-SECURITY-RANDOM-SOURCE-0002:** Living sources MUST be release- or revision-bound where possible; an unchanged URL or familiar API name MUST NOT prove unchanged implementation, module boundary, validation, or lifecycle behavior.

**RM-SECURITY-RANDOM-SOURCE-0003:** Documented API contracts, observed platform/lifecycle behavior, statistical diagnostics, cryptographic validation evidence, and Rusty Mill guarantees MUST remain separately identified.

**RM-SECURITY-RANDOM-SOURCE-0004:** A source, OS, kernel, SDK, provider/module, configuration, virtualization, or clone-lifecycle change invalidates affected current claims until readiness, exact-fill, failure, secrecy, lifecycle, and certification impact is classified.
