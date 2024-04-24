# Hash Function in Python
This repository contains a basic hash function implemented in Python. The hash function takes a key as input and produces an index in an array, suitable for use in hash table implementations. The function aims to distribute keys uniformly across the array to minimize collisions, providing a basic yet effective hashing mechanism.

## Usage
To use the hash function, simply call the hash_function method with the key and the size of the array as arguments. Here's an example:

This will calculate the index for the key "example_key" in an array of size 10.

index = hash_function("example_key", 10)
print(f"The index for key 'example_key' is {index}")
