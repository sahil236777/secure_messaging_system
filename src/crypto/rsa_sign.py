# secure_messaging_system/src/crypto/rsa_sign.py

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def load_rsa_key(filepath: str) -> RSA.RsaKey:
    with open(filepath, 'rb') as f:
        key_data = f.read()
        return RSA.import_key(key_data)

def sign_message(message: bytes, private_key_path: str) -> bytes:
    key = load_rsa_key(private_key_path)
    hashed = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hashed)
    return signature

def verify_signature(message: bytes, signature: bytes, public_key_path: str) -> bool:
    key = load_rsa_key(public_key_path)
    hashed = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(hashed, signature)
        return True
    except (ValueError, TypeError):
        return False

# Example usage
if __name__ == "__main__":
    msg = b"This is a signed message."
    private_path = "keys/sender_private.pem"
    public_path = "keys/sender_public.pem"

    sig = sign_message(msg, private_path)
    valid = verify_signature(msg, sig, public_path)

    print("[+] Signature valid:", valid)
