class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

def hash_djb2(key):
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value

def key_index(key, size):
    hash_value = hash_djb2(key)
    index = hash_value % size
    return index

def hash_table_set(ht, key, value):
    if ht is None or key == "":
        return 0

    index = key_index(key, ht.size)
    current_node = ht.array[index]

    # Check if key already exists, update value if it does
    while current_node is not None:
        if current_node.key == key:
            current_node.value = value
            return 1
        current_node = current_node.next

    # Create a new node
    new_node = HashNode(key, value)
    new_node.next = ht.array[index]
    ht.array[index] = new_node

    return 1

def hash_table_get(ht, key):
    if ht is None or key == "":
        return None

    index = key_index(key, ht.size)
    current_node = ht.array[index]

    while current_node is not None:
        if current_node.key == key:
            return current_node.value
        current_node = current_node.next

    return None

def main():
    size = int(input("Enter the size of the hash table: "))
    ht = HashTable(size)

    while True:
        print("\nMenu:")
        print("1. Add element to hash table")
        print("2. Get value by key")
        print("3. View hash table")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            result = hash_table_set(ht, key, value)
            if result == 1:
                print("Element added successfully!")
            else:
                print("Failed to add element.")
        elif choice == "2":
            key = input("Enter the key: ")
            value = hash_table_get(ht, key)
            if value is not None:
                print("Value found:", value)
            else:
                print("Key not found.")
        elif choice == "3":
            print("\nHash Table:")
            for i, head in enumerate(ht.array):
                print(f"Bucket {i}: ", end="")
                while head:
                    print(f"[{head.key}: {head.value}] -> ", end="")
                    head = head.next
                print("None")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
