def djb2_hash(key):
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

# Example usage
key = "example_key"
hash_value = djb2_hash(key)
print(f"The hash value for key '{key}' is {hash_value}")
def djb2_hash(key):
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

def main():
    # Prompt the user for input
    key = input("Enter the string to be hashed: ")
    
    # Calculate the hash value using the djb2 hash function
    hash_value = djb2_hash(key)
    
    # Print the hash value
    print(f"The hash value for '{key}' is {hash_value}")

if __name__ == "__main__":
    main()
