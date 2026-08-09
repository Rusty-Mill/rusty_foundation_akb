# Use without reveal and cryptographic operations

**RM-SECRETS-OPAQUE-0001:** Opaque use names an exact operation such as sign, decrypt, derive, MAC, database connect, SSH authenticate, cloud request sign, token exchange, or provider plugin call plus its inputs, output, target, algorithm/protocol, purpose, and authority.

**RM-SECRETS-OPAQUE-0002:** A non-reveal claim identifies the provider/process/hardware boundary containing plaintext or private material and proves that caller-visible memory, logs, IPC, files, environment, and crash artifacts receive no reusable secret.

**RM-SECRETS-OPAQUE-0003:** A reference, URI, handle, encrypted blob, wrapped key, or vault path is not itself proof of non-reveal; providers publish whether they materialize plaintext internally, in agents, plugins, drivers, or target clients.

**RM-SECRETS-OPAQUE-0004:** Outputs are classified for oracle, chosen-input, replay, correlation, and secret-derivation risks. Policy limits operations, inputs, rate, audience, context, and exportability.

**RM-SECRETS-OPAQUE-0005:** Interactive consent, dual control, quorum, hardware presence, or target approval are operation-specific obligations with exact terminal outcomes and cannot be cached as general secret-use authority.

**RM-SECRETS-OPAQUE-0006:** Cancellation and timeout report whether the provider or target may have consumed a nonce, advanced a counter, signed, decrypted, authenticated, or committed an effect.
