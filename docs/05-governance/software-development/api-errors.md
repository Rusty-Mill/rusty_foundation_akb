# Public APIs, types, compatibility, and errors

The [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) are review input rather than external mandate; Rusty Mill adopts compatible principles through these normative rules.

**RM-DEV-API-0001:** Public APIs MUST trace to accepted capability requirements and semantic types before stabilization. Native constants, handles, error codes, callbacks, thread rules, or OS names cannot leak into portable contracts accidentally.

**RM-DEV-API-0002:** Constructors and builders MUST reject invalid combinations before effects begin. Typestate, enums, validated newtypes, and private fields SHOULD make illegal states unrepresentable when complexity remains proportionate.

**RM-DEV-API-0003:** Ownership, borrowing, lifetime, thread-safety, blocking, cancellation, partial progress, authority, and resource-release behavior MUST be evident from types and documentation.

**RM-DEV-API-0004:** Extension points MUST be justified by at least two concrete use cases or a required provider boundary. Sealed traits, non-exhaustive enums, reserved fields, and versioned negotiation are used deliberately rather than reflexively.

**RM-DEV-API-0005:** Public compatibility review covers signatures, trait implementation possibilities, inference, auto traits, layout/ABI promises, feature combinations, errors, side effects, timing/order, resource bounds, and behavioral contracts.

**RM-DEV-ERR-0001:** Recoverable library failures use typed `Result`; errors distinguish invalid input, unsupported/degraded capability, denied authority, unavailable provider, timeout, cancellation, partial/ambiguous effect, exhaustion, conflict, corruption, and internal defect where semantically applicable.

**RM-DEV-ERR-0002:** Errors preserve stable programmatic classification and causal source without exposing secrets, native implementation details, localized presentation text, or unstable diagnostic strings as API contracts.

**RM-DEV-ERR-0003:** Context is added at boundary transitions. Errors MUST be handled, propagated with context, or recorded under explicit policy; silent swallowing and catch-all success are prohibited.

**RM-DEV-ERR-0004:** Cancellation, timeout, provider acceptance, and domain-effect completion remain distinct outcomes. Retrying an ambiguous effect requires explicit replay/idempotency authority.

**RM-DEV-ERR-0005:** Panics indicate violated internal invariants or unrecoverable process policy, never ordinary external input/provider failure. FFI unwind boundaries and task/thread panic policy are explicit.
