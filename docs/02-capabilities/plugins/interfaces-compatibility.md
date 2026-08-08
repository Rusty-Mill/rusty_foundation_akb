# Interfaces and compatibility

**RM-PLUGIN-INTERFACE-0001:** Interfaces have stable identity and semantic version independent of package version. Imports and exports declare exact compatible ranges and optional features.

**RM-PLUGIN-INTERFACE-0002:** Cross-boundary values use an explicitly specified ABI/protocol representation with ownership, allocation/deallocation, error, string/byte encoding, alignment, calling convention, panic/exception, async, cancellation, and thread-affinity rules.

**RM-PLUGIN-INTERFACE-0003:** Rust types, trait objects, layouts, unwinding, and standard-library allocations do not form a stable independent-plugin ABI unless an exact shared toolchain/build contract is selected and evidenced.

**RM-PLUGIN-INTERFACE-0004:** Native interfaces use narrow C-compatible or generated ABI surfaces where selected; process plugins use versioned IPC protocols; portable components use a pinned component/runtime/interface specification. These are separate compatibility classes.

**RM-PLUGIN-INTERFACE-0005:** Additive optional operations require explicit feature discovery. Changing semantics, ownership, threading, error meaning, required operation, representation, or authority is breaking even if symbols still link.

**RM-PLUGIN-INTERFACE-0006:** Panics, exceptions, signals, process exits, traps, and protocol disconnects are contained according to isolation class and mapped to typed plugin failure; undefined behavior in a native in-process plugin cannot be contained by the contract.

