# Platform research

| Platform | Candidate mechanisms | Architectural variance |
|---|---|---|
| Windows | `VirtualAlloc`/`VirtualFree`, `VirtualProtect`, file-mapping objects/views, `VirtualLock`, large pages | Reserve and commit are explicit; allocation granularity differs from page size; mapping objects and views have separate lifetimes; executable publication requires cache synchronization. |
| Linux | `mmap`/`munmap`, `mprotect`, `madvise`, `mlock`, `shm_open`, `memfd_create`, huge pages | Overcommit and fault behavior vary; file truncation can fault mappings; advice/locking/huge-page features and quotas are kernel/configuration dependent. |
| macOS | `mmap`, Mach VM allocation/map/protect/wire, purgeable memory, `MAP_JIT`, JIT write-protection APIs | Hardened Runtime and entitlements constrain executable mappings; Apple silicon enforces JIT write/execute policy; Mach and POSIX surfaces differ. |

## Primary references

- [Microsoft: VirtualAlloc](https://learn.microsoft.com/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc)
- [Microsoft: File Mapping](https://learn.microsoft.com/windows/win32/memory/file-mapping)
- [Linux: mmap(2)](https://man7.org/linux/man-pages/man2/mmap.2.html)
- [Linux: mlock(2)](https://man7.org/linux/man-pages/man2/mlock.2.html)
- [Linux: memfd_create(2)](https://man7.org/linux/man-pages/man2/memfd_create.2.html)
- [Apple: Mach VM](https://developer.apple.com/documentation/kernel/mach/mach_vm)
- [Apple: Hardened Runtime](https://developer.apple.com/documentation/security/hardened-runtime)
- [Apple: Porting JIT compilers to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-just-in-time-compilers-to-apple-silicon)

