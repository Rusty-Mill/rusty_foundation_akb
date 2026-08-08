# ADR-0081: Cryptographic policy precedes provider selection

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Provider defaults and available algorithm names change with OS, library, hardware, enterprise policy, certification mode, and time. Choosing “best available” at the operation call site creates downgrade ambiguity, unreproducible data formats, accidental legacy use, and migrations that cannot distinguish new writes from old reads.

## Decision

Every cryptographic key and operation is created from a versioned workload policy resolved to an immutable plan before provider selection and use. The plan fixes purpose, exact suite/parameters/encodings, strength and protection horizon, generation versus legacy-read allowances, provider/protection/certification constraints, transition policy, and failure/degradation rules. Providers prove that plan or resolution fails; they do not silently choose or substitute security policy.

## Consequences

- New encryption/signing and legacy decryption/verification can follow different explicit policies.
- Data/protocol formats carry suite and policy-relevant version evidence.
- Algorithm transitions use multi-generation read/write and rollback plans.
- “FIPS,” “hardware-backed,” or OS identity cannot stand in for exact module and operation evidence.
