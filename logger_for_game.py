import os
import logging
from datetime import datetime
from parameters import DEBUG_MODE

# Creates logs/ directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

def game_logger() -> None:
    '''
    Initializes logging system for the game.
    Logs to terminal if DEBUG_MODE is True, and always logs to the a file
    '''
    log_filename = generate_session_filename() # Unique log file per session
    handlers = []

    if DEBUG_MODE: 
        handlers.append(logging.StreamHandler()) # Log to terminal
    
    handlers.append(logging.FileHandler(log_filename)) # Logs to file

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=handlers
    )

def generate_session_filename() -> str:
    '''
    Generates a timestamped filename for the current game session.
    '''
    now = datetime.now()
    return f"logs/session_{now.strftime('%Y-%m-%d_%H-%M-%S')}.log"
