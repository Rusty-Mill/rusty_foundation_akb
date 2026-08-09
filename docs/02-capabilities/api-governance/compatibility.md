# Compatibility and change analysis

**RM-API-GOV-COMPAT-0001:** Every comparison declares producer and consumer generations, direction, protocol/encoding profile, deployment overlap, and intended audience.

**RM-API-GOV-COMPAT-0002:** Analysis reports schema/wire, source, behavioral, operational, security, privacy, and economic compatibility independently; no aggregate `non-breaking` result may hide a failing axis.

**RM-API-GOV-COMPAT-0003:** Consumer compatibility is evaluated against known use: accepted values, exhaustive enums, required presence, validation, ordering, timing, retries, error handling, pagination, quota, and authorization assumptions.

**RM-API-GOV-COMPAT-0004:** Unknown fields and enum values have explicit preserve/ignore/reject behavior. Removed field tags/names remain reserved wherever their encoding can recur.

**RM-API-GOV-COMPAT-0005:** Tightened validation, broadened side effects, weakened ordering, changed defaults, newly required authority, lower limits, or increased disclosure are behavioral changes even when wire-compatible.

**RM-API-GOV-COMPAT-0006:** Compatibility rules are versioned policy inputs. Waivers identify affected consumers, risk owner, expiry, rollout controls, and rollback or migration evidence.

## Change analysis result

A result contains changed symbols/operations, classified deltas, affected directions and consumers, confidence and blind spots, required mitigations, approval, and reproducible analyzer inputs/tool versions.
