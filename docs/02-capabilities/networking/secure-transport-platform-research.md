# Platform and protocol research

This research informs adapters; protocol specifications and current provider behavior remain authoritative.

## Protocols

- TLS 1.3 defines full and PSK/resumed handshakes, optional 0-RTT early data with weaker replay/forward-secrecy properties, post-handshake messages, traffic-key updates, record limits, alerts, and closure.
- QUIC uses TLS 1.3 for authentication/key establishment and authenticated transport parameters while QUIC owns packet protection levels, multiplexed streams, flow/congestion/loss, migration, connection IDs, and connection closure. QUIC requires compatible ALPN.
- `tls-exporter` is the TLS 1.3 channel-binding profile. ALPN is authenticated protocol selection but may expose metadata depending on version/privacy mechanisms.

Primary sources: [RFC 8446 TLS 1.3](https://www.rfc-editor.org/info/rfc8446/), [RFC 9000 QUIC](https://www.rfc-editor.org/rfc/rfc9000.html), [RFC 9001 TLS for QUIC](https://www.rfc-editor.org/rfc/rfc9001.html), [RFC 7301 ALPN](https://www.rfc-editor.org/info/rfc7301/), [RFC 9266 TLS exporter channel binding](https://www.rfc-editor.org/rfc/rfc9266.html), [RFC 9849 TLS Encrypted Client Hello](https://www.rfc-editor.org/rfc/rfc9849.html).

## Windows

Schannel is Windows' TLS/DTLS security provider behind SSPI and inherits OS protocol, cipher, credential, trust, and policy behavior that varies by Windows build and configuration. Connection attributes and shutdown must be queried/mapped; provider success does not replace Rusty Mill's original-identity/application-readiness policy.

Primary sources: [Schannel TLS overview](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-ssl-schannel-ssp-overview), [creating a Schannel connection](https://learn.microsoft.com/en-us/windows/win32/secauthn/creating-a-secure-connection-using-schannel).

## Apple platforms

Network.framework composes TLS over TCP and provides QUIC parameter construction with ALPN. Legacy Secure Transport is deprecated. App Transport Security can impose additional platform policy; custom verification may tighten but must not silently weaken product policy.

Primary sources: [Network TLS options](https://developer.apple.com/documentation/network/nwprotocoltls/options), [Network parameters for TLS/QUIC](https://developer.apple.com/documentation/network/nwparameters/tls), [App Transport Security](https://developer.apple.com/documentation/security/preventing-insecure-network-connections).

## Linux and portable providers

Linux may use OpenSSL, rustls, GnuTLS, NSS, kernel/user-space QUIC, distribution crypto policy, hardware/remote keys, or application-private trust. Provider/library version and build/configuration matter more than the OS label. OpenSSL exposes provider-specific early-data, exporter, key-update, shutdown, and QUIC behavior that adapters must map rather than generalize.

Primary sources: [OpenSSL early data](https://docs.openssl.org/master/man3/SSL_read_early_data/), [OpenSSL key update](https://docs.openssl.org/master/man3/SSL_key_update/), [OpenSSL exporters](https://docs.openssl.org/master/man3/SSL_export_keying_material/).

