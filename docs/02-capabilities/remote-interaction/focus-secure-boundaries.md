# Focus, secure input, and privileged boundaries

**RM-REMOTE-INTERACTION-BOUNDARY-0001:** Focus observation, focus request, activation, foreground placement, input delivery, and domain action completion MUST remain distinct. Remote input does not grant focus-control authority.

**RM-REMOTE-INTERACTION-BOUNDARY-0002:** Local focus and routing policy remains authoritative. The service MUST NOT silently redirect an event to a newly focused window, different desktop/session, or source outside the consented boundary.

**RM-REMOTE-INTERACTION-BOUNDARY-0003:** Secure desktop/input, lock/login, permission/consent, elevation, credential, protected-content, and system-policy surfaces MUST suspend or deny ordinary remote control and invalidate queued commands.

**RM-REMOTE-INTERACTION-BOUNDARY-0004:** Integrity, sandbox, accessibility, privacy, session, compositor, and application restrictions MUST be surfaced as effective-scope evidence; bypassing them with a more privileged backend is not degradation.

**RM-REMOTE-INTERACTION-BOUNDARY-0005:** Local physical input MUST have defined precedence and may suspend remote control. Local escape/stop input MUST never be intercepted, remapped, delayed, or injected by the remote path.

**RM-REMOTE-INTERACTION-BOUNDARY-0006:** Clipboard, file drop, drag-and-drop, shell activation, process launch, accessibility actions, and domain commands MUST use their own typed authority paths rather than being smuggled through injected key or pointer sequences.

**RM-REMOTE-INTERACTION-BOUNDARY-0007:** The system MUST expose when the native destination cannot receive reliable injection provenance; products must not use injected-event origin as their sole authorization or fraud signal.
