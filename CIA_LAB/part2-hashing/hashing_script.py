import hashlib

# Function to calculate a SHA-256 hash of a file
def hash_file(file_name):
    h = hashlib.sha256()

    with open(file_name, "rb") as file:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: file.read(4096), b""):
            h.update(byte_block)

    return h.hexdigest()

# Test the function
file = "sample_file.txt"
file_hash = hash_file(file)
print(f"The SHA-256 hash of {file} is: {file_hash}")
