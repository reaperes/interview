# Datasource
Datasource objects can provide connection pooling and distributed transactions.
Datasource is implemented in three ways.
- A basic DataSource implementation produces standard Connection objects that are not pooled or used in a distributed transaction.
- A DataSource implementation that supports connection pooling produces Connection objects that participate in connection pooling, that is, connections that can be recycled.
- A DataSource implementation that supports distributed transactions produces Connection objects that can be used in a distributed transaction, that is, a transaction that accesses two or more DBMS servers.
