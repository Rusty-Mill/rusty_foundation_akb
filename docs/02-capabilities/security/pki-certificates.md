# Certificate parsing and evidence

A `CertificateEvidence` binds immutable original bytes and digest to a bounded parse result: format/encoding, signed object and signature bytes, version, serial, issuer/subject names as structured attributes, validity interval, subject public-key information, extensions with criticality/raw value/recognized projection, parse warnings, provider, and generation.

**RM-PKI-CERT-0001:** DER certificate, PEM envelope, certificate bag, PKCS container, trust record, key, request, CRL, OCSP response, and provider reference MUST be distinct typed inputs with independent bounds and parser contracts.

**RM-PKI-CERT-0002:** Parsing MUST bound total bytes, nesting, lengths, integers, strings, names, attributes, extensions, alternative names, policy data, and object count with checked arithmetic before allocation.

**RM-PKI-CERT-0003:** Original signed bytes MUST remain immutable and authoritative for signature verification. Parsed/re-encoded structures MUST NOT silently replace them or claim byte-for-byte canonicalization.

**RM-PKI-CERT-0004:** Unknown critical extensions MUST cause validation failure unless an exact selected policy/provider contract processes them. Unknown noncritical extensions remain preserved evidence, not discarded proof of irrelevance.

**RM-PKI-CERT-0005:** Duplicate, malformed, nonminimal/noncanonical, conflicting, unsupported, ambiguous-string, invalid-time, and trailing-data cases MUST be explicit. Lenient display parsing MUST NOT feed security validation silently.

**RM-PKI-CERT-0006:** Distinguished-name display is localized presentation over structured values. String equality, display equality, certificate identity, reference-identity matching, and trust are separate.

**RM-PKI-CERT-0007:** Inspection and signature verification are side-effect-free and do not consult trust stores, fetch network data, import certificates, open private keys, prompt, or claim trust.
