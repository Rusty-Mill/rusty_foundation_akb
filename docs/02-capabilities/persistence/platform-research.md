# Persistence provider and platform research

## Primary sources

- PostgreSQL documents exact [transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [locking](https://www.postgresql.org/docs/current/explicit-locking.html), [write-ahead logging](https://www.postgresql.org/docs/current/wal-intro.html), and [continuous archiving/PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) semantics.
- SQLite's [atomic commit](https://www.sqlite.org/atomiccommit.html), [transactions](https://www.sqlite.org/lang_transaction.html), and [WAL](https://www.sqlite.org/wal.html) documentation expose important embedded-filesystem, locking, synchronization, and recovery boundaries.
- Microsoft documents SQL Server [isolation levels](https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql), [transactions](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/begin-transaction-transact-sql), and [point-in-time restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-sql-server-database-to-a-point-in-time-full-recovery-model).

## Portability conclusion

Database semantics arise from a selected engine/service, storage, driver, protocol, topology, and configuration rather than the host OS. Embedded providers inherit filesystem/process constraints; services add networks, pools, authentication, replication, and independent operations. Rusty Mill therefore standardizes typed workloads and evidence while product RFCs select exact providers, dialects, schemas, topology, migration tools, and operational objectives.

