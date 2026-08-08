# Crash capture and analysis

## Capability identity

`rm.diagnostics.crash-capture` records the minimum available fatal-failure evidence under a declared platform crash policy.

**RM-DIAGNOSTICS-CRASH-0001:** Crash capture, post-crash artifact processing, symbol resolution, classification, consent, retention, and upload are separate stages with separate authorities.

**RM-DIAGNOSTICS-CRASH-0002:** In-process fatal-path code uses only operations proven safe for the platform crash context. It does not allocate from the ordinary heap, acquire application locks, start runtimes, perform network I/O, invoke general logging, or assume other threads are consistent.

**RM-DIAGNOSTICS-CRASH-0003:** Recursive failure is bounded by a one-way state transition. At most one primary capture attempt occurs; secondary failures terminate through the platform default or previously chained policy.

**RM-DIAGNOSTICS-CRASH-0004:** Crash artifacts record product/build/debug identity, process execution identity, failure mechanism/code, thread/module snapshot quality, capture mechanism/version, truncation, and missing-data reasons.

**RM-DIAGNOSTICS-CRASH-0005:** Raw memory, register, stack, module, command-line, environment, and breadcrumb data are classified independently. Full-memory capture is never the secure default and requires explicit authority, retention, access, and consent policy.

**RM-DIAGNOSTICS-CRASH-0006:** Symbolication and source mapping occur out of process against exact build/debug-artifact identities. Symbolicated frames report confidence and unresolved/inlined/truncated state.

**RM-DIAGNOSTICS-CRASH-0007:** Platform-owned crash handlers and user policy take precedence where required. Installing a handler cannot silently disable OS reporting, debugger behavior, core policy, or another owner without an explicit composition decision.

**RM-DIAGNOSTICS-CRASH-0008:** Crash capture is best effort. Failure to obtain an artifact is a supported outcome with whatever minimal external evidence can be established; the contract never promises recovery or continued execution after memory corruption.

## Breadcrumbs

A crash breadcrumb buffer is fixed-capacity, preallocated, overwrite-bounded, and contains only preclassified compact records. It exposes loss/wrap count and never stores secrets or arbitrary formatted strings.

