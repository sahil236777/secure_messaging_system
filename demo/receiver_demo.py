# secure_messaging_system/demo/receiver_demo.py

from src.messaging.receiver import receive_secure_message
from src.utils.logger import info, error

if __name__ == "__main__":
    try:
        receive_secure_message("keys/sender_public.pem")
        info("Decrypted message saved at messages/decrypted_message.txt")
    except Exception as e:
        error(str(e))
