# ADR-0133: Use without reveal is a provider-mediated operation contract

## Status

Accepted

## Context

Secret references and vault handles are often described as preventing secret exposure even when an SDK, agent, plugin, driver, temporary file, or application process later receives plaintext. Storage location does not determine the runtime exposure boundary, and generic read APIs cannot prove non-reveal.

## Decision

Rusty Mill claims use without reveal only for a named provider-mediated operation whose contract identifies the boundary containing plaintext/private material and demonstrates that reusable material never enters caller-visible memory, files, environment, IPC, logs, dumps, or telemetry. References and encrypted blobs remain location/protection evidence, not non-reveal proof.

## Consequences

- Sign/decrypt/connect/request-sign/token-exchange operations receive separate contracts.
- Providers disclose agent, plugin, driver, and target-client materialization.
- Output oracle and chosen-input risks are included in policy and conformance.
- Products may still choose explicit bounded reveal when no truthful opaque operation exists.
