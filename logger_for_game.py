import logging
from datetime import datetime

DEBUG_MODE = False  # for debuging change to True (then you'll see logs in terminal) default must be False

def game_logger():
    log_filename = generate_session_filename() # kiekvienai sesijai atskirai
    handlers = []

    if DEBUG_MODE: 
        handlers.append(logging.StreamHandler()) # terminalui
    
    handlers.append(logging.FileHandler(log_filename)) # sesijos logui

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=handlers
    )

def generate_session_filename():
    now = datetime.now()
    return f"logs/session_{now.strftime('%Y-%m-%d_%H-%M-%S')}.log"
