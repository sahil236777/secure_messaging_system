# secure_messaging_system/src/crypto/hash_utils.py

from Crypto.Hash import SHA256

def hash_bytes(data: bytes) -> str:
    """
    Returns SHA-256 hash digest as a hex string.
    """
    digest = SHA256.new(data)
    return digest.hexdigest()

def hash_file(file_path: str) -> str:
    """
    Reads file as bytes and returns SHA-256 hash digest.
    """
    with open(file_path, 'rb') as f:
        data = f.read()
        return hash_bytes(data)

# Example usage
if __name__ == "__main__":
    message = b"Hash me!"
    print("[+] Hash of message:", hash_bytes(message))

    # To test hash_file(), create a dummy file and test
    with open("messages/temp.txt", "wb") as f:
        f.write(message)

    print("[+] Hash of file:", hash_file("messages/temp.txt"))
