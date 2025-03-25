# secure_messaging_system/src/crypto/aes_cipher.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_message(plaintext: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return {
        'ciphertext': ciphertext,
        'nonce': cipher.nonce,
        'tag': tag
    }

def decrypt_message(encrypted: dict, key: bytes):
    cipher = AES.new(key, AES.MODE_EAX, nonce=encrypted['nonce'])
    try:
        plaintext = cipher.decrypt_and_verify(encrypted['ciphertext'], encrypted['tag'])
        return plaintext
    except ValueError:
        raise Exception("Message authentication failed or message was tampered.")

def generate_aes_key(length: int = 16):
    return get_random_bytes(length)  # 16 bytes = 128-bit key

# Example usage
if __name__ == "__main__":
    key = generate_aes_key()
    message = b"Confidential: Launch at 0600 hrs."

    encrypted = encrypt_message(message, key)
    print("[+] Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted, key)
    print("[+] Decrypted:", decrypted.decode())
