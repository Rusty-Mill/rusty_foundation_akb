# Platform and format research

| Target | Candidate mechanisms | Architectural variance |
|---|---|---|
| Windows native | `LoadLibraryEx` with safe explicit search directories, Authenticode/package identity, restricted helper processes/AppContainer-style policy | DLL dependency search and loader callbacks are process-global hazards; native code shares host authority; signatures do not sandbox. |
| Linux native | `dlopen`/`dlsym`, optional link-map namespaces, ELF/package signatures external to loader, namespaces/seccomp/cgroups/process brokers | `dlclose` does not prove safe unload; symbol/dependency scope varies; distro packaging/trust and sandbox mechanisms are not universal. |
| macOS native | bundles/dyld, code signing, Hardened Runtime library validation, sandbox/XPC helpers | Third-party native plugins may require weakening library validation; entitlements belong to host; helper services provide stronger isolation. |
| Portable component | WebAssembly Component Model/WIT with pinned runtime and host imports | Runtime maturity/version/async/ABI varies; component isolation does not constrain authority exposed by host imports. |

## Primary references

- [Microsoft: Dynamic-Link Library Security](https://learn.microsoft.com/windows/win32/dlls/dynamic-link-library-security)
- [Microsoft: LoadLibraryEx](https://learn.microsoft.com/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexa)
- [Linux: dlopen/dlmopen/dlclose](https://man7.org/linux/man-pages/man3/dlmopen.3.html)
- [Apple: Hardened Runtime](https://developer.apple.com/documentation/security/hardened-runtime)
- [Apple: Library Validation entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.disable-library-validation)
- [WebAssembly Component Model](https://component-model.bytecodealliance.org/)

