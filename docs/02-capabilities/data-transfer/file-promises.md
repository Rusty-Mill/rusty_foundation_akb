# File and content promises

| Field | Value |
|---|---|
| Status | Draft service contract 0.1.0 |

**RM-TRANSFER-PROMISE-0001:** A promise describes ordered items, safe suggested names, type/size estimates, directory/file kind, overwrite/collision policy, metadata preservation, source provenance, and required destination authority without claiming content already exists.

**RM-TRANSFER-PROMISE-0002:** The target grants an explicit destination directory capability and chooses final names under target filesystem policy. Source-provided paths, separators, traversal, reserved names, links, and device names cannot escape that authority.

**RM-TRANSFER-PROMISE-0003:** Fulfillment creates temporary/incomplete artifacts, streams with byte/time/resource bounds and integrity checks, then publishes each result atomically where supported. Partial artifacts never masquerade as completed files.

**RM-TRANSFER-PROMISE-0004:** Executable bits, ACLs, extended attributes, quarantine/download provenance, alternate streams, links, sparse state, timestamps, and platform metadata are independent preservation choices. Unknown metadata is not silently trusted or executed.

**RM-TRANSFER-PROMISE-0005:** Cancellation/failure reports item-level outcomes and cleans temporary artifacts under explicit retry/quarantine policy. A multi-item promise states whether commit is per-item or transaction-like; universal atomicity is not assumed.

**RM-TRANSFER-PROMISE-0006:** Source deletion for move occurs only after the target proves committed items and the selected move policy allows deletion. Cross-filesystem/cross-application move normally composes copy plus acknowledged deletion rather than claiming atomic rename.

**RM-TRANSFER-PROMISE-0007:** Content scanning, type detection, decompression, thumbnailing, and preview are separate restricted services; declared MIME/UTI/extension does not establish safe content type.

