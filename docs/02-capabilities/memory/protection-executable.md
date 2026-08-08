# Protection and executable memory

## Capability and service boundary

Protection transition belongs to the virtual-region/mapping capability. Executable-memory orchestration is a separate platform service with elevated review.

**RM-MEMORY-PROTECT-0001:** Protections model none, read, write, execute, and platform extension combinations. Effective page-aligned ranges and any widened native protection are disclosed.

**RM-MEMORY-PROTECT-0002:** Safe access is impossible while a region lacks the required protection or a conflicting transition is underway. Callers coordinate all threads; changing page tables does not revoke already copied bytes or guarantee race-free execution.

**RM-MEMORY-PROTECT-0003:** Executable memory is unavailable by default and requires explicit capability/profile selection, authority, platform entitlement/policy evidence, code provenance policy, and threat review.

**RM-MEMORY-PROTECT-0004:** Providers prefer write-xor-execute workflows. Simultaneous writable+executable mappings are prohibited unless a narrowly scoped platform mechanism requires them and exact degradation is accepted.

**RM-MEMORY-PROTECT-0005:** Publishing generated code follows write, validation, transition to execute/nonwrite, required instruction-cache synchronization, and generation commit. Execution cannot begin before commit.

**RM-MEMORY-PROTECT-0006:** Executable aliases, dual mappings, JIT write toggles, code signing, control-flow integrity, pointer authentication, and entitlements are platform qualities reported individually rather than normalized away.

