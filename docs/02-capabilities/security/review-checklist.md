# Cross-domain security review checklist

**Status:** Draft governance input

Every capability and service review answers these questions with requirement or evidence links. “Not applicable” requires a reason.

## Authority and identity

- What authority is required, where does it originate, and can a narrower authority suffice?
- Are identities typed by issuer/namespace and kept distinct from authority?
- Which ambient inputs exist, and can each be removed or explicitly admitted by policy?
- Can authority be duplicated, transferred, inherited, serialized, expired, or revoked?
- Does every derivation provably attenuate all relevant dimensions?

## Enforcement and races

- What exact operation is the native enforcement point?
- Can policy, namespace, identity, labels, or object state change between check and use?
- Are redirects, links, aliases, inheritance, and confused-deputy paths addressed?
- Does missing evidence or unsupported enforcement fail closed?
- Are degradation and fallback visible before authority is exercised?

## Data and diagnostics

- Which inputs, outputs, metadata, and errors are sensitive?
- Are buffers initialized on every outcome and retained only as long as necessary?
- Can logs, traces, metrics, crash reports, or benchmarks reveal sensitive values?
- Are zeroization, memory locking, encryption, or certification claims precisely scoped and evidenced?

## Lifecycle and concurrency

- What happens during close, cancellation, revocation, process creation, fork/clone, snapshot, suspend, and crash?
- Can an in-flight operation outlive or broaden its authority?
- Are ownership and terminal outcomes unambiguous under races?
- Are resource exhaustion and denial-of-service limits specified?

## Supply chain and verification

- Which unsafe/native boundary and third-party dependencies are trusted?
- Are provider identity, build provenance, configuration, and evidence bound to the claim?
- Do tests include adversarial state changes and fault injection, not only happy paths?
- Are platform/version/filesystem/sandbox qualifiers preserved in conformance reports?

