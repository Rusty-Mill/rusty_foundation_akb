# URI parsing and scheme safety

**RM-ACTIVATION-URI-0001:** A URI target preserves original bounded bytes/text for evidence plus a validated semantic parse: scheme, authority/host, userinfo, port, path segments, query pairs/raw query, fragment, normalization/version, and parse errors. Display rendering is separate.

**RM-ACTIVATION-URI-0002:** Scheme comparison follows its registered grammar; percent encoding, Unicode/IDNA host form, dot segments, backslashes, control characters, embedded credentials, default ports, empty components, and nested URIs are not normalized with one universal rule.

**RM-ACTIVATION-URI-0003:** A URI is an untrusted locator/intent, not authority to connect, fetch, authenticate, spend, message, install, execute, reveal local data, or mutate state. The receiving application revalidates scheme-specific semantics and authority.

**RM-ACTIVATION-URI-0004:** `file:` and custom schemes MUST NOT bypass file capability, sandbox, path, executable, origin, or consent policy. Translation to native file/object references is a separate authority-checked operation.

**RM-ACTIVATION-URI-0005:** High-impact schemes/actions require explicit foreground user intent, trustworthy purpose/target presentation, replay protection, and confirmation in the receiving domain. Handler UI is not proof that effects are safe.

**RM-ACTIVATION-URI-0006:** Universal/web-to-app links carry verified association evidence distinct from ordinary custom-scheme registration and from TLS/web-origin authentication. Fallback to a browser or app is policy-visible.

**RM-ACTIVATION-URI-0007:** Logging, analytics, errors, and previews redact userinfo, query/fragment secrets, tokens, personal paths, message bodies/recipients, coordinates, and custom-scheme payloads by default.
