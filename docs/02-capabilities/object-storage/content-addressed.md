# Content-addressed storage

**RM-OBJECT-CAS-0001:** A content descriptor binds digest algorithm/profile, encoded digest, exact byte length, media/artifact type, representation/encoding, optional annotations/embedded bytes, and descriptor schema/version. Digest input is exact stored/retrieved bytes unless another canonical view is explicitly selected.

**RM-OBJECT-CAS-0002:** Content is accepted under a descriptor only after length and independent cryptographic digest verification before unsafe parsing/use. Provider checksum, ETag, multipart validator, filename, URI, signature, or transport security cannot substitute.

**RM-OBJECT-CAS-0003:** Hash algorithm policy declares accepted algorithms, output length/encoding, collision/preimage horizon, deprecation/transition, multi-digest requirements, unknown algorithm behavior, verification provider, and resource limits.

**RM-OBJECT-CAS-0004:** A content address proves byte equality under the selected algorithm and assumptions; it does not prove author, provenance, authenticity of the descriptor, semantic type, safety, freshness, authorization, confidentiality, uniqueness of meaning, or availability.

**RM-OBJECT-CAS-0005:** Namespace references/tags/manifests to content descriptors are mutable or immutable signed/versioned objects with separate authority, conditional generations, reachability, retention, and lifecycle. Moving a tag never mutates content identity.

**RM-OBJECT-CAS-0006:** Deduplication occurs only within declared tenant/encryption/privacy domains and addresses equality/side-channel leakage, ownership/reference counting, quotas/billing, concurrent publish, garbage collection, legal hold, and cryptographic erasure.

**RM-OBJECT-CAS-0007:** Garbage collection uses an authenticated coherent root/reference snapshot, conservative reachability, generation/fencing, grace periods, in-flight upload/read pins, quarantine, retention/hold, replica lag, dry-run manifests, and recoverable deletion evidence.

**RM-OBJECT-CAS-0008:** Algorithm migration creates new descriptors and reference graphs after verified rehashing; old/new coexistence, manifest/signature updates, cache/mirror propagation, rollback horizon, and final retirement are explicit.

