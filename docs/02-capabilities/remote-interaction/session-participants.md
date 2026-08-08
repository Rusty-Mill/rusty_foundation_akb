# Session, participants, and roles

A `RemoteInteractionSession` is a local, generation-scoped coordination service. Its authority manifest binds local login/security-context generation, selected capture-source grant, transport/channel identity, authenticated participant evidence, purpose, roles, device/action allowlists, visibility/interaction policy, expiration, and revocation channel.

**RM-REMOTE-INTERACTION-SESSION-0001:** View, point, keyboard, touch, pen, text, clipboard, file transfer, audio, camera, elevation, session management, and unattended operation MUST be independently selectable authorities.

**RM-REMOTE-INTERACTION-SESSION-0002:** Participant authentication is scoped evidence, not control authority. Role assignment MUST bind participant, channel, local session, purpose, grant revision, freshness, and approving local actor or policy.

**RM-REMOTE-INTERACTION-SESSION-0003:** Adding, replacing, reconnecting, or changing a participant or channel MUST NOT inherit a prior participant's authority without explicit continuity evidence and current policy resolution.

**RM-REMOTE-INTERACTION-SESSION-0004:** Capture-source retargeting, local user switch, privilege/context change, transport rekey/reconnect, or control-policy expansion MUST produce a new session or authority revision and visible reconfirmation where policy requires.

**RM-REMOTE-INTERACTION-SESSION-0005:** Unattended access is a separate privileged profile with installation, device identity, durable policy, recovery, update, audit, secret protection, and local-disclosure requirements; it is never inferred from an interactive grant.

**RM-REMOTE-INTERACTION-SESSION-0006:** Multi-participant control MUST declare arbitration, attribution, simultaneous-device policy, handoff, local ownership, and revocation semantics rather than merging participants into one input source.

The session reports `proposed`, `local_consent_pending`, `connected`, `view_active`, `control_active`, `suspended`, `revoked`, `disconnecting`, and terminal milestones separately.
