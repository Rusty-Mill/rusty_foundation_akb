# Typed activation intents

`rm.activation.intent` is immutable, purpose-specific data. It never contains shell syntax or an implicitly executable command line.

**RM-ACTIVATION-INTENT-0001:** Intent kinds MUST distinguish open/view, edit, print, reveal/select, share, compose, application launch/reopen, URI navigation, protocol action, settings, and namespaced extensions. Unsupported kinds remain explicit.

**RM-ACTIVATION-INTENT-0002:** Every intent MUST carry identity/generation, purpose/verb, ordered targets, source/application/user-interaction provenance, origin/session, creation/freshness, foreground/presentation context, preferred-handler constraint if policy permits, interaction policy, cancellation/deadline, and privacy class.

**RM-ACTIVATION-INTENT-0003:** Target kinds MUST distinguish file/object capability, directory, URI, application identity, settings page, content-type-only query, and provider extension. A string cannot be inferred as file or URI by punctuation alone.

**RM-ACTIVATION-INTENT-0004:** Open, edit, print, reveal, share, and execute are different authority and handler-role requests. A handler eligible to view MUST NOT be assumed eligible to edit or print.

**RM-ACTIVATION-INTENT-0005:** Multiple targets preserve order, per-target type/authority, all-or-partial policy, and grouping. Providers disclose splitting, truncation, unsupported combinations, and per-target outcomes.

**RM-ACTIVATION-INTENT-0006:** Display name, icon, claimed MIME/UTI/extension, URI scheme/host, originating app, and recommended handler are advisory evidence, not authority or verified identity.

See [ADR-0072](../../adr/0072-activation-is-untrusted-intent-not-authority.md).
