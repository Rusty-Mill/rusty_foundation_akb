# Device authority, privacy, and class handoff

Discovery authority limits namespaces, classes, properties, topology depth, sensitive identifiers, and observation duration. A `DeviceRef` is a locator for a later authorized resolution; possessing it does not authorize open, control, capture, mount, eject, firmware update, or power change.

**RM-DEVICE-AUTHORITY-0001:** Enumeration MUST be side-effect-minimal and MUST NOT open class protocols, mount media, request user consent, wake hardware solely for optional metadata, or execute device-supplied code.

**RM-DEVICE-AUTHORITY-0002:** Sensitive properties—including serials, stable network addresses, precise location/topology, user labels, account-bound identifiers, and unique peripheral fingerprints—MUST require explicit projection and privacy classification.

**RM-DEVICE-AUTHORITY-0003:** Logs, metrics, crash artifacts, and diagnostics MUST use redacted or session-pseudonymous references by default and MUST bound property cardinality.

**RM-DEVICE-AUTHORITY-0004:** A class-specific capability MUST revalidate reference generation, class, current state, and its own authority at the native open/authorization point.

**RM-DEVICE-AUTHORITY-0005:** Delegation MUST attenuate scope and property visibility; a delegated reference MUST NOT gain ambient access in the receiving process.

Class handoff returns a class-specific candidate plus correlation evidence. Audio endpoints, input devices, displays, cameras, removable volumes, sensors, and network interfaces may expose namespaces that do not map one-to-one to general device nodes. “No proven mapping” is valid and preferable to guessed correlation.

Accessible device selection uses stable semantic labels within the current snapshot, disambiguates identical friendly names with non-sensitive attributes, announces additions/removals without unbounded live-region chatter, and provides nonvisual status/error paths.
