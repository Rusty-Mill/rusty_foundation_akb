# `rm.transfer.data-offer`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-TRANSFER-OFFER-0001:** An offer has immutable offer identity/generation, ordered item identities, source/provenance class, sensitivity, allowed purposes/operations, lifetime policy, and an ordered representation set for each item.

**RM-TRANSFER-OFFER-0002:** Each representation declares canonical type identifier and version/parameters, content/character encoding, estimated/known size, streaming/random-access capability, fidelity/lossiness, source-native versus converted status, trust classification, and required authority/interaction.

**RM-TRANSFER-OFFER-0003:** Enumeration exposes metadata only and does not trigger content rendering, conversion, network access, file creation, or source mutation.

**RM-TRANSFER-OFFER-0004:** Materialization requests one exact item/representation, maximum bytes/time/resources, cancellation/deadline, destination kind, purpose, and conversion policy. The source returns a bounded byte/message stream or typed unavailable/stale/denied/failure outcome.

**RM-TRANSFER-OFFER-0005:** Stream success means exact declared representation bytes completed and integrity/length checks passed. Partial output is never reported as complete and is discarded or retained only under explicit target policy.

**RM-TRANSFER-OFFER-0006:** A source may become unavailable after enumeration. Offers never imply persistence; stale ownership, source exit, cancellation, conversion failure, and size-budget rejection are distinct outcomes.

**RM-TRANSFER-OFFER-0007:** Provider conversion is a separately identified transformation with input/output types, converter/version, loss and sanitization claims, resource/network behavior, and provenance. Targets may require source-native only.

**RM-TRANSFER-OFFER-0008:** Text representations declare Unicode encoding, newline convention, normalization preservation, embedded NUL/control policy, language/direction where known, and rich-text fallback. Plain text never silently executes markup.

**RM-TRANSFER-OFFER-0009:** File/URL/object references are capabilities or untrusted locators under explicit authority; a path string is not ambient filesystem authority and a URL is not permission to fetch.

**RM-TRANSFER-OFFER-0010:** Offer diagnostics and previews are size-bounded, content-safe, and do not materialize secrets by default.

