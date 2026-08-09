# ADR-0136: Compatibility is directional and consumer-qualified

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Schema tools often label changes breaking or non-breaking, but old producers with new consumers, new producers with old consumers, generated source, runtime behavior, security, and known consumer assumptions differ.

## Decision

Compatibility decisions declare direction, dimensions, protocol/encoding profile, deployment overlap, and consumer context. Wire compatibility is evidence for one dimension, not a universal conclusion.

## Consequences

Change analysis and approvals are more explicit and can return conditional or unknown. Consumer inventories and conformance vectors become governance inputs. A single undifferentiated compatibility badge is prohibited.
