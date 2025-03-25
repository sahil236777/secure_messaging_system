# secure_messaging_system/src/messaging/sender.py

import os
from src.crypto.aes_cipher import generate_aes_key, encrypt_message
from src.crypto.rsa_sign import sign_message
from src.utils.file_io import write_binary_file, write_text_file

def send_secure_message(message_path: str,
                        sender_private_key_path: str,
                        aes_key_path: str = "messages/aes.key"):
    os.makedirs("messages", exist_ok=True)

    # Load plaintext message
    with open(message_path, "rb") as f:
        plaintext = f.read()

    # Generate AES key and encrypt
    aes_key = generate_aes_key()
    encrypted = encrypt_message(plaintext, aes_key)

    # Save AES key (demo only)
    write_binary_file(aes_key_path, aes_key)

    # Serialize encrypted components
    encrypted_blob = encrypted['nonce'] + encrypted['tag'] + encrypted['ciphertext']
    write_binary_file("messages/encrypted_message.bin", encrypted_blob)

    # Sign encrypted blob
    signature = sign_message(encrypted_blob, sender_private_key_path)
    write_binary_file("messages/signature.bin", signature)

    print("[+] Message encrypted and signed successfully.")

# Example usage
if __name__ == "__main__":
    send_secure_message("messages/original_message.txt", "keys/sender_private.pem")
