# Filesystem resolution quality levels

| Field | Value |
|---|---|
| Status | Draft quality model |
| Applies to | `rm.filesystem.resolve` providers |

## Purpose

Express what a provider can prove about directory-relative containment without reducing security to a binary supported/unsupported flag.

## Levels

| Level | Name | Guarantee |
|---|---|---|
| R0 | Anchored | Lookup begins from an opened directory resource, but some ancestor/link/mount races may not be atomically constrained. |
| R1 | Link-confined | Every traversed component is resolved without following disallowed link/reparse objects; ancestor handles prevent path-prefix substitution. |
| R2 | Mount-confined | R1 plus traversal cannot cross a filesystem/volume/mount boundary contrary to policy. |
| R3 | Kernel-constrained | Requested link, parent, root, and mount constraints are enforced atomically by one native resolution mechanism or equivalent provider proof. |

R0 is not sufficient for untrusted-path confinement. Security-sensitive profiles select the required level explicitly. Providers may prove R1/R2 using a component-by-component handle walk when native single-call constraints are unavailable, but conformance must cover mutation races and resource cleanup.

## Rules

1. A provider claims the highest level passed for a particular policy, OS version, and filesystem class.
2. Falling back to a lower level requires explicit negotiation and disclosure.
3. A post-open check alone cannot elevate an escaped operation to a confined level if side effects may already have occurred.
4. Link and mount policies are separate; rejecting symbolic links does not automatically reject mount/reparse crossings.
5. Unknown or provider-specific namespace objects are rejected at R1+ unless their traversal semantics are modeled.
6. Conformance includes adversarial concurrent namespace mutation, not static fixture tests alone.

## Expected platform investigation

- Linux `openat2` is a candidate R3 mechanism for supported policies and kernels; handle-walk fallbacks may prove R1/R2.
- Windows requires evaluation of handle-relative native object operations and reparse controls; ordinary path-based `CreateFileW` should not be assumed R3.
- macOS handle-walk composition may prove R1 and possibly R2 for selected policies; exact mount and alias behavior requires evidence.
