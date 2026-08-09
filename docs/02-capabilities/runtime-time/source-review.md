# Runtime and time source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On support-baseline/provider change or 2027-02-08, whichever occurs first |
| Reviewer | Runtime/time capability owner |
| Open blocking findings | None for Draft-to-Experimental eligibility; exact trial platforms remain undecided |

The review binds current architectural propositions, not future supported-version claims.

| Source set | Class and reviewed status | Affected propositions | Impact/finding |
|---|---|---|---|
| [Microsoft platform sources](platform-research.md#microsoft) | Microsoft platform contracts; reviewed 2026-08-08 | high-resolution active measurement; sleep-sensitive domains; tolerable delay; cancellation races | Compatible. `SetWaitableTimerEx` documents Windows 8+ relative-timer low-power exclusion and APC caveats; exact supported Windows builds remain trial-bound. |
| [Linux platform sources](platform-research.md#linux-man-pages-project) | Linux userspace platform contracts; current man-pages reviewed 2026-08-08 | MONOTONIC excludes suspend; BOOTTIME includes it; absolute sleeps; descriptor timers; wake requires separate authority | Compatible. Kernel/libc/container availability and time namespaces require exact environment evidence. |
| [Apple platform sources](platform-research.md#apple) | Apple platform contracts; reviewed 2026-08-08 | uptime excludes sleep; continuous time includes sleep; nanosecond API preference; timer leeway; cooperative cancellation | Compatible with qualification. Public documentation can be JavaScript-rendered and availability must be captured from tested SDKs. |

**RM-RUNTIME-SOURCE-0001:** Adoption evidence MUST snapshot or otherwise bind the exact platform/SDK documentation and availability declarations used for each provider choice.

**RM-RUNTIME-SOURCE-0002:** A mutable documentation URL MUST NOT prove that an older or newer OS/provider generation has identical behavior.

**RM-RUNTIME-SOURCE-0003:** Source review MUST reopen when OS support policy, SDK headers, kernel/libc baseline, native mechanism, suspend model, or documented cancellation behavior changes.

**RM-RUNTIME-SOURCE-0004:** Trial evidence MUST distinguish documented contract, observed behavior, and Rusty Mill portable guarantee.
