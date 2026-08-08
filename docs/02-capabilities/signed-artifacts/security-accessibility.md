# Security, privacy, and accessibility

**RM-SIGNED-CROSS-0001:** Signing and verification treat artifacts, envelopes, certificates, claims, provenance, SBOMs, log responses, timestamps, URLs, names, and error text as hostile input with explicit allocation, recursion, decompression, parsing, and network bounds.

**RM-SIGNED-CROSS-0002:** Verification never executes, loads, renders active content, resolves unrestricted external resources, follows unsafe paths, or installs the artifact merely to inspect it.

**RM-SIGNED-CROSS-0003:** Signing keys remain behind least-privilege operation capabilities; ceremony logs exclude secrets and minimize artifact content, identities, repository topology, and unpublished dependency disclosure.

**RM-SIGNED-CROSS-0004:** Error behavior does not expose private key/provider details or form a signing oracle. Security telemetry is structured, access-controlled, redacted, rate-limited, and correlated without artifact contents by default.

**RM-SIGNED-CROSS-0005:** User-facing verification distinguishes cryptographic validity, identified signer, trusted signer role, trusted time, transparency, provenance, platform assessment, and final product policy. Status never relies on color or icon alone.

**RM-SIGNED-CROSS-0006:** Signing approval and exception workflows are keyboard and assistive-technology operable, preserve focus, expose the exact artifact identity/digest/purpose, support review without time pressure where safe, and provide an accessible recovery path.

**RM-SIGNED-CROSS-0007:** Localized signer and artifact labels are untrusted presentation strings. Stable machine identifiers and digests remain available, bidirectional-text controls are contained, and translated status text cannot alter policy meaning.

**RM-SIGNED-CROSS-0008:** Overrides require reason, authority, scope, expiry, affected digest/policy generation, prominent nonvisual indication, and audit evidence; they cannot become silent global trust.

