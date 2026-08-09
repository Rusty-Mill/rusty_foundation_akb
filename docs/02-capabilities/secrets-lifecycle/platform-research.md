# Platform and standards research

## Primary references

- [SPIFFE Workload API](https://spiffe.io/docs/latest/spiffe-specs/spiffe_workload_api/) defines local workload identification, X.509/JWT SVID and bundle streams, rotation updates, and trust-domain federation without requiring a preprovisioned application secret.
- [Vault secrets engines](https://developer.hashicorp.com/vault/docs/secrets) document stored, generated, and operation-oriented secret providers; [leases](https://developer.hashicorp.com/vault/docs/concepts/lease) bind dynamic credentials to renewal and revocation lifecycle.
- [RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html) defines OAuth token exchange with explicit resource/audience/scope and distinct delegation versus impersonation semantics.
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) document volume and environment delivery, update behavior, node distribution, immutable objects, and security limitations.

## Platform families

| Family | Relevant facilities | Architectural consequence |
|---|---|---|
| Windows | Credential Manager/Vault, DPAPI/DPAPI-NG, CNG/TPM, service accounts and managed identities, named pipes/handles | user/machine binding, opaque key operations, workload/service identity, and generic secret delivery differ |
| Linux | kernel keyrings, secret-service implementations, TPM/PKCS#11, credentials files/descriptors, systemd credentials, workload agents | namespaces, process credentials, file descriptors, tmpfs, agents, and target protocols define the actual exposure boundary |
| macOS | Keychain, Secure Enclave/CryptoTokenKit, launch services and app sandbox/keychain groups | application identity/access groups, interactive unlock, opaque keys, synchronizing vaults, and generic values have different claims |

## Conclusion

The portable model standardizes lifecycle evidence, exposure, leases, delivery, rotation, and reconciliation. Exact providers, targets, protocols, and platform protection remain explicit selections.
