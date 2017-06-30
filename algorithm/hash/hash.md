# What is hash (function)
Hash function can be used to map data of arbitrary size to data of fixed size. The values returned by a hash function are called hash values, digests, or simply hashs.

# How to resolve hash collision?
## Separate chaining
By having each bucket contains a linked list of elements.
Especially, JDK 8 use tree instead of linked list.

## Open addressing
Insert to other bucket using linear probing or quadratic probing.

## Expand hash buckets
Increase the number of buckets and then redistribute all the elements.
