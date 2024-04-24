def hash_djb2(key):
    """
    Hashes a string using the djb2 algorithm.

    Args:
    - key: The string to be hashed.

    Returns:
    - The hash value of the input string.
    """
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value

def key_index(key, size):
    """
    Calculates the index for a given key using the djb2 hash function.

    Args:
    - key: The key to be hashed.
    - size: The size of the array of the hash table.

    Returns:
    - The index at which the key/value pair should be stored in the array
      of the hash table.
    """
    hash_value = hash_djb2(key)
    index = hash_value % size
    return index

# Call the key_index function with sample input
key = "example_key"
size = 10
index = key_index(key, size)
print(f"The index for key '{key}' is {index}")
