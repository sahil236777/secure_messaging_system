# secure_messaging_system/demo/receiver_demo.py

import sys
import os

# Add the project root (where src/ is located) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.messaging.receiver import receive_secure_message
from src.utils.logger import info

from src.utils.logger import error

if __name__ == "__main__":
    try:
        receive_secure_message("keys/sender_public.pem")
        info("Decrypted message saved at messages/decrypted_message.txt")
    except Exception as e:
        error(str(e))
