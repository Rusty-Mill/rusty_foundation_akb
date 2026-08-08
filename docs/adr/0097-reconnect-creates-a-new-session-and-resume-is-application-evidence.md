# ADR-0097: Reconnect creates a new session and resume is application evidence

## Status

Accepted

## Context

Long-lived connections fail across network changes, sleep, server deploys, credential rotation, proxy rebinding, and process restarts. WebSocket defines no resume protocol; SSE carries an opaque last-event identifier; WebTransport streams and datagrams end with their session. Treating reconnect as continuity hides gaps, duplicates, changed authority, expired server state, and ambiguous prior effects.

## Decision

Every reconnect creates a new session generation and repeats current security, origin, authentication, authorization, negotiation, and resource checks. Resume cursors, sequence numbers, acknowledgments, snapshots, and deduplication tokens are typed application evidence with scope and retention, never transport proof. Products explicitly reconcile gaps, overlap, duplicates, lost state, and unknown effects; queued client operations are not replayed automatically.

## Consequences

- Credential and policy changes take effect on every new session.
- Exactly-once and lossless claims require an application protocol and durable state.
- Late data from superseded sessions is rejected deterministically.
- Reconnection APIs must expose more evidence than a simple connected boolean.

