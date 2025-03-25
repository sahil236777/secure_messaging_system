# Secure Messaging System

## Project Overview

This project implements a Python-based **Secure Messaging System** that ensures the core principles of communication security:

- **Confidentiality** (via AES encryption)
- **Integrity** (via SHA-256 hashing)
- **Non-Repudiation** (via RSA digital signatures)
- **Authentication** (via RSA public-private key infrastructure)

The system simulates a secure exchange of messages between a sender and a receiver using industry-standard cryptographic tools.

---

## Architecture Overview

The project is organized modularly into distinct components:

```
secure_messaging_system/
├── src/
│   ├── crypto/         # Core crypto algorithms
│   ├── messaging/      # Sender and receiver logic
│   └── utils/          # File I/O and logging
├── demo/               # CLI scripts to run simulation
├── keys/               # Generated RSA keys
├── messages/           # Message input/output and artifacts
├── README.md           # This documentation
└── requirements.txt    # Python dependencies
```

Each component encapsulates a part of the secure communication pipeline to allow traceable and testable development.

---

## How It Works

1. **Key Generation**:
   - `keygen.py` creates RSA public/private keys for sender and receiver.
   - Output: `.pem` files in `keys/`.

2. **Sending a Secure Message**:
   - `sender_demo.py` prepares a plaintext message.
   - AES key is generated and used to encrypt the message.
   - The encrypted blob is digitally signed with sender's private key.
   - Artifacts are saved to `messages/`.

3. **Receiving and Verifying**:
   - `receiver_demo.py` verifies the digital signature using the sender’s public key.
   - If valid, the message is decrypted using the AES key and saved.

---

## Security Features Implemented

| Feature           | Technique Used                       |
|-------------------|--------------------------------------|
| Confidentiality   | AES (Advanced Encryption Standard)   |
| Integrity         | SHA-256                              |
| Non-Repudiation   | RSA Digital Signature (PKCS#1 v1.5)  |
| Authentication    | Public-Private Key Verification      |

All algorithms are sourced from the `pycryptodome` library.

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate RSA Keys
```bash
python src/crypto/keygen.py
```

### 3. Send a Secure Message
```bash
python demo/sender_demo.py
```

### 4. Receive and Decrypt
```bash
python demo/receiver_demo.py
```

---

## Sample Output Artifacts

![image](https://github.com/user-attachments/assets/901a3969-2488-40e1-a271-353f71d92a6a)


- `messages/original_message.txt` – Plaintext
- `messages/encrypted_message.bin` – AES ciphertext
- `messages/signature.bin` – RSA signature
- `messages/decrypted_message.txt` – Final decrypted message

---

## Dependencies

```txt
pycryptodome
cryptography
```

---

## Future Improvements

- Encrypt AES key using receiver's public RSA key.
- Add support for mutual authentication.
- Replace plaintext AES key with secure key exchange.
- Implement GUI or web interface for real-time use.
- Package modules into installable Python package.

---

© 2025 – Secure Messaging System | CSTP2301 | Vancouver Community College
