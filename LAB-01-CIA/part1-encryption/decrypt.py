from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_file(filename, key):
    """
    Decrypts an encrypted file
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(f"{filename}.decrypted", "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    key = load_key()
    file = "very_sensitive_data.txt.encrypted"
    decrypt_file(file, key)
