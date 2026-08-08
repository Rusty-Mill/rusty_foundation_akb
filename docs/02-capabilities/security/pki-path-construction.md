# Path construction

Path construction consumes a leaf, an untrusted bag of supplied candidates, a trust snapshot, optional bounded provider/intermediate sources, and a construction policy. It emits bounded candidate paths plus provenance and rejection evidence; it does not decide application trust by itself.

**RM-PKI-PATH-0001:** The presented certificate list MUST be treated as an unordered, duplicate-prone, attacker-controlled candidate bag. Its order and terminal element MUST NOT establish issuer relationship or trust.

**RM-PKI-PATH-0002:** Candidate issuer selection MUST validate names/identifiers and cryptographic signatures under exact algorithm policy. Subject/issuer text or key identifier match alone is insufficient.

**RM-PKI-PATH-0003:** Construction MUST bound depth, breadth, candidates per node, signature work, policy/name state, memory, elapsed time, network requests/bytes, and total candidate paths, reporting which bound terminated search.

**RM-PKI-PATH-0004:** Loops, duplicate certificates, cross-signing, multiple anchors, alternate issuers, same-subject keys, expired/not-yet-valid candidates, and algorithm-policy differences MUST be handled deterministically without assuming a unique chain.

**RM-PKI-PATH-0005:** Candidate provenance MUST identify peer-supplied, application-supplied, store, cache, bundled, or network-fetched origin and trust status independently. An intermediate source never becomes an anchor implicitly.

**RM-PKI-PATH-0006:** Path preference/tie-breaking MUST be explicit and evidence-bearing. Provider-selected “best” path records selection policy/version and rejected alternatives where observable.

**RM-PKI-PATH-0007:** No-path, resource-bound, network-disabled/unavailable, ambiguous candidates, unsupported algorithm/extension, and policy-rejected paths MUST remain distinct outcomes.
