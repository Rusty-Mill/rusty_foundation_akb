# Device identity and generations

A `DeviceRef` contains provider identity, observation scope, opaque native correlation token, and generation. Equality answers “the same observed provider object generation,” not “the same physical unit forever.”

**RM-DEVICE-IDENTITY-0001:** Device references MUST be opaque, provider-scoped, scope-scoped, and generation-scoped.

**RM-DEVICE-IDENTITY-0002:** A provider MUST advance generation when removal/republication, driver-stack replacement, namespace reuse, or material identity uncertainty can invalidate prior properties or class handoffs.

**RM-DEVICE-IDENTITY-0003:** Friendly name, device path, topology location, serial number, vendor/product/revision identifiers, MAC address, filesystem path, and OS registry identifier MUST NOT individually be represented as universal physical identity.

**RM-DEVICE-IDENTITY-0004:** Cross-restart persistence MUST use an explicit match policy over disclosed evidence, return ambiguity, and require product confirmation when a wrong match could affect security, privacy, or data integrity.

**RM-DEVICE-IDENTITY-0005:** Resolving a stale reference MUST return stale/absent/ambiguous distinctly; it MUST NOT silently select a similar or default device.

Identity confidence may be `same-generation`, `provider-continuity`, `evidence-match`, `ambiguous`, or `unknown`. Only the first two can support automatic continuity when the class-specific contract also permits it. See [ADR-0050](../../adr/0050-device-identity-is-generation-scoped-evidence.md).
