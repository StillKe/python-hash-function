def hash_function(key, size):
    """
    A simple hash function that maps keys to indices in the array.

    Args:
    - key: The key to be hashed.
    - size: The size of the array.

    Returns:
    - An index in the array where the corresponding value will be stored.
    """
    # Convert the key to a string (assuming the key is not already a string)
    key_str = str(key)
    
    # Initialize a variable to store the hash value
    hash_value = 0
    
    # Compute the hash value using a simple algorithm
    for char in key_str:
        hash_value += ord(char)
    
    # Take the modulo of the hash value to get the index within the array size
    index = hash_value % size
    
    return index

def main():
    # Prompt the user for the key and size of the array
    key = input("Enter the key: ")
    size = int(input("Enter the size of the array: "))
    
    # Calculate the index using the hash function
    index = hash_function(key, size)
    
    # Print the result
    print(f"The index for key '{key}' is {index}")

if __name__ == "__main__":
    main()
