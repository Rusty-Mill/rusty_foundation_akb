# Metadata, privacy, and provenance

**RM-IMAGE-METADATA-0001:** Metadata projection separates structural decode-critical fields, color/orientation, descriptive/accessibility, capture/device/location/people, rights/provenance, editing history, thumbnails/previews, integrity/signature, and unknown/vendor blocks.

**RM-IMAGE-METADATA-0002:** Every value preserves schema/namespace/version, container path/scope, raw type/unit/encoding, normalized interpretation where selected, source byte range, provenance, validation, conflict/duplicate order, and truncation/withholding.

**RM-IMAGE-METADATA-0003:** EXIF, XMP, IPTC, container-native properties, filenames, filesystem timestamps, MIME headers, sidecars, and application databases are independent sources. Conflicts follow explicit precedence and MUST NOT be silently merged.

**RM-IMAGE-METADATA-0004:** Metadata read is size/nesting/count bounded and lazy. Thumbnail, preview, profile, maker-note, XML, or vendor-block parsing never bypasses the image decode threat boundary.

**RM-IMAGE-METADATA-0005:** Default import/display strips or withholds precise location, people/biometric tags, device serials, account IDs, edit history, hidden thumbnails, and other sensitive fields according to purpose. Presence is not consent to log, index, upload, or preserve on export.

**RM-IMAGE-METADATA-0006:** Unknown-block preservation is opt-in, byte-bounded, provenance-bearing, and incompatible with a claim that sensitive metadata was removed. Semantic edit, lossless container rewrite, and full re-encode report which bytes/fields were preserved, rewritten, normalized, or dropped.

**RM-IMAGE-METADATA-0007:** Embedded signatures, content credentials, hashes, or provenance manifests are evidence requiring their own validation/trust policy; ordinary decode does not authenticate them or make other metadata trustworthy.
