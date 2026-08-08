# ADR-0054: A mount is a namespace relationship, not volume identity

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows volumes may have drive letters and multiple directory mount points, Linux supports mount namespaces, bind and overlay mounts, and macOS distinguishes disks/partitions/volumes from mount points. Treating a root path as “the drive” breaks identity, authority, containers, and change handling.

## Decision

A mount is a generation-scoped relationship between a filesystem view and a location in one namespace. Devices, media, regions, filesystem instances, mounts, and paths retain separate identities and lifecycles. Cross-restart matching uses explicit evidence and ambiguity rather than a universal volume ID.

## Consequences

- Observation and APIs are graph- and namespace-aware.
- Paths convey neither volume identity nor authority.
- Mount changes do not automatically mean filesystem or device replacement.
