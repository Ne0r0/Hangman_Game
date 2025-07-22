import logging


DEBUG_MODE = True # for debuging change to True (then you'll see logs in terminal) default must be False

def game_logger():
    if DEBUG_MODE: 
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(
            filename="hangman.log",
            filemode="a", # for DEBUG purpose change form "w" to "a"
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
