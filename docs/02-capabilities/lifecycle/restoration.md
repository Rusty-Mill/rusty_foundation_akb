# State preservation and restoration

## Platform service

The restoration service manages disposable, versioned continuity metadata. It does not replace durable domain persistence.

**RM-LIFECYCLE-RESTORE-0001:** Restoration archives identify product/build, schema version, application/session epoch, creation reason/time, constituent state partitions, integrity evidence, sensitivity, and expiry.

**RM-LIFECYCLE-RESTORE-0002:** Domain data is persisted by its owning service during ordinary operation. Restoration stores identifiers, view/navigation state, window relationships, and explicitly approved ephemeral editing continuity—not an authoritative duplicate database.

**RM-LIFECYCLE-RESTORE-0003:** Save is incremental or bounded, cancellable where execution continues, and atomically publishes a complete archive. A lifecycle callback may request a final checkpoint but is not the only save trigger.

**RM-LIFECYCLE-RESTORE-0004:** Restore validates integrity, schema/build compatibility, authority, referenced-resource existence, display/window constraints, and product policy before applying state.

**RM-LIFECYCLE-RESTORE-0005:** Restoration is transactional by partition: each partition reports restored, migrated, skipped, unavailable, invalid, expired, or failed. Invalid optional UI state falls back safely without corrupting durable data.

**RM-LIFECYCLE-RESTORE-0006:** Sensitive state uses the selected protection and secret-store capabilities. Secure text, credentials, transient authorization, and native handles are prohibited.

**RM-LIFECYCLE-RESTORE-0007:** Restored focus, windows, and activities obey current accessibility, display, locale, security, and activation policy rather than replaying stale native coordinates or authority.

