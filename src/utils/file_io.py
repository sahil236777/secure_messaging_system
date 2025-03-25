# secure_messaging_system/src/utils/file_io.py

import os

def write_binary_file(path: str, data: bytes):
    with open(path, 'wb') as f:
        f.write(data)

def read_binary_file(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()

def write_text_file(path: str, text: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def read_text_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Example usage
if __name__ == "__main__":
    write_text_file("messages/sample.txt", "Secure test message.")
    print("[+] File written.")

    content = read_text_file("messages/sample.txt")
    print("[+] Read content:", content)
