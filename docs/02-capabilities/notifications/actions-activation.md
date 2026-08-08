# Notification actions and activation

An action descriptor has a stable semantic ID, localized label, role/purpose, foreground/background intent, authentication/confirmation requirements, optional bounded input schema, and expiry. Platform button identifiers are adapter mappings.

**RM-NOTIFY-ACTION-0001:** Action responses MUST enter through the [application activation](../lifecycle/activation.md) path as untrusted typed input with notification/content revision, action ID, user input, provider evidence, and receipt time.

**RM-NOTIFY-ACTION-0002:** Notification response MUST NOT convey authority, identity proof, focus, foregrounding, freshness, or successful domain completion.

**RM-NOTIFY-ACTION-0003:** The application MUST revalidate action existence, content revision, expiry, current domain state, authority, replay/idempotency, and confirmation before executing the ordinary domain command.

**RM-NOTIFY-ACTION-0004:** Destructive, financial, security-sensitive, privacy-sensitive, or irreversible actions require product-defined confirmation/authentication and MUST NOT be weakened because the response originated in trusted system UI.

**RM-NOTIFY-ACTION-0005:** Text input MUST be length/schema validated, treated as sensitive according to context, excluded from ordinary telemetry, and never interpreted as markup or command syntax implicitly.

**RM-NOTIFY-ACTION-0006:** Duplicate, late, reordered, redirected-to-existing-instance, and cold-start responses MUST converge idempotently or report a safe stale outcome.

See [ADR-0059](../../adr/0059-notification-actions-are-untrusted-activation.md).
