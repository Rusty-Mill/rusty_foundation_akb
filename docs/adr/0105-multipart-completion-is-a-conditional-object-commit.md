# ADR-0105: Multipart completion is a conditional object commit

## Status

Accepted

## Context

Multipart and resumable uploads stage independently retryable pieces. Parts can be replaced, expire, remain orphaned, or have provider-specific validators; completion responses can be lost. Meanwhile another writer can create or replace the intended target. Treating part upload or an upload-session identifier as the final object permits wrong ordering, mixed intent, lost updates, and unsafe retries.

## Decision

An upload session is bounded staging state. Completion supplies an immutable ordered part manifest, whole-object length/integrity expectations, metadata/encryption/retention policy, and create-only or exact-generation target precondition. It atomically commits one new provider object generation or returns failure/unknown. Unknown completion is reconciled against both upload and target-generation evidence before any retry or abort.

## Consequences

- Uploaded parts never become application-visible objects by themselves.
- Concurrent writers cannot silently overwrite each other under the strong profile.
- Orphan staging is separately inventoried and garbage-collected.
- Providers lacking completion preconditions require quarantine/promotion or a weaker declared profile.

