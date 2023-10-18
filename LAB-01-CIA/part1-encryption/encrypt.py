from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    """
    Encrypts a file
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(f"{filename}.encrypted", "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    generate_key()
    key = load_key()
    file = "very_sensitive_data.txt"
    encrypt_file(file, key)
