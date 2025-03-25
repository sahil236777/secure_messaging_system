# secure_messaging_system/src/crypto/keygen.py

from Crypto.PublicKey import RSA
import os

def generate_keys(user_type: str, key_size: int = 2048):
    assert user_type in ["sender", "receiver"], "Invalid user_type. Use 'sender' or 'receiver'."

    # Generate RSA key pair
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Ensure keys directory exists
    os.makedirs("keys", exist_ok=True)

    # Define output paths
    private_key_path = f"keys/{user_type}_private.pem"
    public_key_path = f"keys/{user_type}_public.pem"

    # Write keys to files
    with open(private_key_path, "wb") as priv_file:
        priv_file.write(private_key)

    with open(public_key_path, "wb") as pub_file:
        pub_file.write(public_key)

    print(f"[+] {user_type.capitalize()} RSA key pair generated.")
    print(f"    ├─ Private Key: {private_key_path}")
    print(f"    └─ Public Key : {public_key_path}")

# Example usage (for testing):
if __name__ == "__main__":
    generate_keys("sender")
    generate_keys("receiver")
