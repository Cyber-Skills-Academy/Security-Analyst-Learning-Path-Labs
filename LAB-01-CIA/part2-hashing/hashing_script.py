import hashlib

# Function to generate hash of the file
def hash_file(filename):
    # Open the file in read-only mode
    with open(filename, "rb") as f:
        # Read the contents of the file
        file_data = f.read()
        # Generate hash
        return hashlib.sha256(file_data).hexdigest()

def main():
    filename = "very_sensitive_data.txt"
    
    # Scenario 1: No changes in the file
    print("Scenario 1: Original file, no changes made.")
    original_hash = hash_file(filename)
    print(f"Original SHA-256 hash: {original_hash}\n")

    input("Simulating file send. Press Enter to continue...")
    
    received_hash = hash_file(filename)
    print(f"Received SHA-256 hash: {received_hash}\n")

    if original_hash == received_hash:
        print("Success! The file was not modified during transmission.\n")
    else:
        print("Alert! The file was modified during transmission.\n")

    # Scenario 2: File gets modified
    print("\nScenario 2: File gets modified after the initial hash.")
    original_hash = hash_file(filename)
    print(f"Original SHA-256 hash: {original_hash}\n")

    input("Go ahead and modify 'very_sensitive_data.txt' file (change a character, add something new, or delete something). Then, press Enter to continue...\n")

    modified_hash = hash_file(filename)
    print(f"Modified SHA-256 hash: {modified_hash}\n")

    if original_hash == modified_hash:
        print("The file has not been modified after the changes.\n")
    else:
        print("Alert! The file has been modified after the changes.\n")

if __name__ == "__main__":
    main()
