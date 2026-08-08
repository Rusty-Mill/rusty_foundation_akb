# Object-storage provider research

## Primary sources

- Amazon S3 documents its [consistency model](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel), [multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html), [checksums](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html), and [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).
- Azure documents [blob concurrency](https://learn.microsoft.com/en-us/azure/storage/blobs/concurrency-manage), [leases](https://learn.microsoft.com/en-us/rest/api/storageservices/lease-blob), [versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview), and [immutable storage](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview).
- Google Cloud Storage documents [consistency](https://cloud.google.com/storage/docs/consistency), [generation preconditions](https://cloud.google.com/storage/docs/request-preconditions), [resumable uploads](https://cloud.google.com/storage/docs/resumable-uploads), and [retention](https://cloud.google.com/storage/docs/bucket-lock).
- The OCI Image Specification defines [content descriptors and digest verification](https://github.com/opencontainers/image-spec/blob/main/descriptor.md) used by portable content-addressed graphs.

## Portability conclusion

Providers differ in key/version identity, ETags and checksums, conditional requests, list/event consistency, multipart completion, metadata, copies, leases, delegated access, encryption, storage classes, versioning/soft delete, retention/legal hold, replication, inventory, and billing. Rusty Mill standardizes exact typed intent and evidence; product RFCs select provider profiles and reject unsupported or lossy mappings.

