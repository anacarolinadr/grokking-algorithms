## Hash Table

#### Chapter Five - H.T. Notes

* It is an better way to store and access information than arrays or linked lists

* Every string saved points to an index, and each index holds an numerical value, check out this example

```python

notebook = {}

#     key - string | value - number value
notebook["apple"] = 1.25
notebook["grapes"] = 2.50
notebook["peach"] = 0.75

```

* A Hash Table maps keys to values, it is great for searching items and creating mappings

* It is possible to check if a value already exists, so you can validate and avoid duplicates

* It is also usefull for caching, the data stored in cache often use hash tables

* You must be careful with collisions, for an example, if you have an array and want to organize it alphabetically, the hash function tells you exactly where each word shoud go. But here is the problem, what if you want to store more words that start with "A"?

* That's why a good hash function must handle colisions carefully

* About performance, all operations generally take O(1) time, but in the worst case (with collisions), they can take O(N)
