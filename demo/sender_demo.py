# secure_messaging_system/demo/sender_demo.py

import os
import sys

# Add the project root (where src/ is located) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.messaging.sender import send_secure_message
from src.utils.logger import info

def setup_demo_message():
    os.makedirs("messages", exist_ok=True)
    message = (
        "This is a confidential message.\n"
        "Please decrypt and verify before reading.\n"
        "- Sender"
    )
    with open("messages/original_message.txt", "w", encoding="utf-8") as f:
        f.write(message)
    info("Sample message prepared at messages/original_message.txt")

if __name__ == "__main__":
    setup_demo_message()
    send_secure_message("messages/original_message.txt", "keys/sender_private.pem")
