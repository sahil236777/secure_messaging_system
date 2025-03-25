# secure_messaging_system/src/messaging/receiver.py

import os
from src.crypto.aes_cipher import decrypt_message
from src.crypto.rsa_sign import verify_signature
from src.utils.file_io import read_binary_file, write_text_file

def receive_secure_message(sender_public_key_path: str,
                           aes_key_path: str = "messages/aes.key"):
    # Load files
    encrypted_blob = read_binary_file("messages/encrypted_message.bin")
    signature = read_binary_file("messages/signature.bin")
    aes_key = read_binary_file(aes_key_path)

    # Reconstruct components
    nonce = encrypted_blob[:16]
    tag = encrypted_blob[16:32]
    ciphertext = encrypted_blob[32:]

    encrypted_dict = {
        'nonce': nonce,
        'tag': tag,
        'ciphertext': ciphertext
    }

    # Verify signature
    is_valid = verify_signature(encrypted_blob, signature, sender_public_key_path)
    if not is_valid:
        raise Exception("Signature verification failed. Message may have been tampered.")

    # Decrypt message
    plaintext = decrypt_message(encrypted_dict, aes_key)
    write_text_file("messages/decrypted_message.txt", plaintext.decode())

    print("[+] Signature verified. Message decrypted and saved.")

# Example usage
if __name__ == "__main__":
    receive_secure_message("keys/sender_public.pem")
