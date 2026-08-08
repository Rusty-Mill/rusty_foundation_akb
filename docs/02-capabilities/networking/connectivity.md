# Connectivity and path observation

## Capability identity

`rm.network.connectivity-observer` publishes immutable policy-scoped path snapshots.

**RM-NETWORK-PATH-0001:** A snapshot records revision/epoch, evaluated requirements, viability state, interface categories, constrained/expensive/metered/roaming claims where available, local-address/DNS/proxy changes, and provider evidence.

**RM-NETWORK-PATH-0002:** Viability means the platform currently predicts a usable path under supplied constraints. It is not proof of DNS success, Internet access, destination reachability, captive-portal completion, peer availability, or authentication.

**RM-NETWORK-PATH-0003:** Unknown and unavailable observations remain explicit. Providers do not infer cost, roaming, security, or interface type from heuristics without declaring quality.

**RM-NETWORK-PATH-0004:** Events may coalesce but carry final snapshots and skipped revisions. Overflow/loss forces re-observation before continuity claims resume.

**RM-NETWORK-PATH-0005:** Applications use observations to trigger reconciliation or policy, not to suppress all connection attempts. The protected native operation remains the final authority/reachability check.

