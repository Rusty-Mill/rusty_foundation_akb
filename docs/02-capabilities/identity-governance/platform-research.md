# Platform and standards research

## Standards

- [RFC 7643](https://www.rfc-editor.org/rfc/rfc7643.html) defines SCIM's platform-neutral User and Group schemas, attribute characteristics, identifiers, extensions, and resource metadata.
- [RFC 7644](https://www.rfc-editor.org/rfc/rfc7644.html) defines SCIM discovery, query/filter, create, replace, patch, delete, bulk, versioning, and HTTP protocol behavior.
- [RFC 7642](https://www.rfc-editor.org/rfc/rfc7642.html) supplies SCIM definitions, concepts, and use cases.
- [RFC 4511](https://www.rfc-editor.org/rfc/rfc4511.html) defines LDAP bind, search, compare, add, delete, modify, rename, abandon, and extended operations.

## Native families

| Family | Relevant facilities | Architectural consequence |
|---|---|---|
| Windows | local/domain accounts and groups, Active Directory, Entra and Microsoft Graph | object IDs, tenant IDs, security identifiers, delta tokens, group forms, and cloud/on-premises lifecycle are provider evidence |
| Linux | NSS/PAM views, local account databases, LDAP/SSSD, FreeIPA and system services | lookup results may compose multiple sources and caches; numeric IDs and names are namespace-scoped |
| macOS | Open Directory, local/network nodes, account and group records, managed identity | record types, node scope, generated identifiers, cached/mobile accounts, and authorization services remain distinct |

## Conclusions

- SCIM is the primary portable provisioning mapping, not the Rusty Mill semantic model.
- LDAP is a directory protocol with provider schemas and consistency characteristics, not a universal account-lifecycle contract.
- Provider-native identifiers and delta cursors remain opaque and scope-bound.
- Product profiles must publish supported mappings and semantic loss rather than advertising generic directory compatibility.
