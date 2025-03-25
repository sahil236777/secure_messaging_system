# secure_messaging_system/src/utils/logger.py

from datetime import datetime

LOG_ENABLED = True  # Toggle this for silent mode

def _log(level: str, msg: str):
    if LOG_ENABLED:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level.upper()}] {msg}")

def info(msg: str):
    _log("info", msg)

def error(msg: str):
    _log("error", msg)

# Example usage
if __name__ == "__main__":
    info("Logger initialized.")
    error("This is a test error.")
