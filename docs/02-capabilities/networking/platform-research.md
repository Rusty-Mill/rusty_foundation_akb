# Platform and standards research

| Platform | Candidate mechanisms | Important variance |
|---|---|---|
| Windows | Winsock `GetAddrInfoEx`, sockets, overlapped I/O/IOCP, `ConnectEx`/`AcceptEx`, Network List/Connectivity APIs, Schannel | Extension functions and cancellation/lifetime rules vary by provider; connectivity is policy observation; handle inheritance and reuse need explicit setup. |
| Linux | `getaddrinfo`, sockets, nonblocking readiness/epoll, resolver/system services, netlink or network-manager integrations, kernel TLS/user TLS providers | libc/resolver and network-manager stacks vary; readiness is not completion; socket option semantics differ; namespaces change observations. |
| macOS | Network framework connections/listeners/path monitors, BSD sockets, system resolver, Network.framework TLS/Secure Transport | Path evaluation is per process/parameters; framework may race/migrate internally; callbacks and ownership use framework-specific queues. |

## Standards references

- [RFC 8305: Happy Eyeballs v2](https://www.rfc-editor.org/rfc/rfc8305)
- [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [RFC 1123: Internet host requirements](https://www.rfc-editor.org/rfc/rfc1123)
- [Microsoft: Winsock functions](https://learn.microsoft.com/windows/win32/winsock/winsock-functions)
- [Linux: getaddrinfo(3)](https://man7.org/linux/man-pages/man3/getaddrinfo.3.html)
- [Linux: socket(7)](https://man7.org/linux/man-pages/man7/socket.7.html)
- [Apple: Network framework](https://developer.apple.com/documentation/network)
- [Apple: NWPathMonitor](https://developer.apple.com/documentation/network/nwpathmonitor)

## Conclusions

Adapters must publish native async quality, cancellation precision, path/cost quality, option mappings, resolver provenance, and secure-provider behavior. No OS name alone proves IPv6 behavior, DNS security, Internet reachability, proxy policy, certificate validation, or transport performance.

