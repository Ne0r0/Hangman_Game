from game import HangmanGame
from words import python_words
from art import hangman_pics
from utils import display_result, play_again, display_status
from logger_for_game import game_logger
import logging

# Initializes the log system – allows you to follow the game progress in the terminal or in a file.
game_logger()

def run_game() -> None:
    '''
    Runs a single session of Hangman game.
    Handles user input, game loop, and result display.
    '''
    # Creates a game object with a random Python word and initial number of lives.
    game = HangmanGame(python_words)
    warned_once = False  # Used to ensure that the warning about incorrect input is displayed only once.
    logging.info(f"New game started. Word length: {len(game.word_manager.word)}")

    print("🎯 Welcome to Python Hangman!")
    print(game.display_word_progress())  # Shows the initial progress of the word (letters vs _).
    print(f"You have {game.player.lives} lives.\n")

    # The main game cycle repeats until the player wins or loses.
    while not game.is_victory() and not game.is_defeat():
        # Determines which ASCII stage of the hangman should be displayed based on the remaining lives.
        stage = len(hangman_pics) - game.player.lives - 1
        print(hangman_pics[stage]) # Shows a visualization of the hangman.

        # User input – can be a letter or a whole word.
        guess = input("Enter a letter or guess the full word: ").strip()
        logging.info(f"Player guessed: {guess}")

        # Checks whether the input consists only of letters.
        if not guess.isalpha():
            logging.warning(f"Invalid input: '{guess}' | Lives before penalty: {game.player.lives}")
            if not warned_once:
                print("🧙 Letters only, brave adventurer! \nNumbers and symbols are forbidden magic. \nOne more misstep and the hangman tightens the rope...")
            else:
                print("❌ Invalid input → -1 life penalty.")
                game.player.take_damage() # Second wrong try – takes a life
                logging.info(f"Penalty applied. Lives now: {game.player.lives}")
            warned_once = True
            continue

        # If a single letter is entered, it is checked to see if it has already been guessed, and then processed.
        if len(guess) == 1:
            if guess.upper() in game.player.guessed_letters:
                print("⚠️ You've already guessed that letter.")
                logging.info(f"Repeat guess: {guess}")
                continue
            game.guess_letter(guess)
            logging.info(f"Letter guessed: {guess.upper()} | Lives left: {game.player.lives}")
        else:
            # If the entire word is entered, it is checked to see if it is correct.
            logging.info(f"Word attempt: {guess.upper()}")
            game.guess_word(guess)
            logging.info(f"Lives after word guess: {game.player.lives}")
            
        # If the game is not over yet, the current progress and number of lives are displayed.
        if not game.is_victory() and not game.is_defeat():
            display_status(
                word_display=game.display_word_progress().split(),
                guessed_letters=game.player.guessed_letters,
                lives=game.player.lives
            )
        logging.info(f"Lives left: {game.player.lives} | Word progress: {game.display_word_progress()}")

    # End of game – shows whether you won or lost, and what the word was.
    result = "WON" if game.is_victory() else "LOST"
    logging.info(f"Game ended. Result: {result} | Word was: {game.word_manager.word}")
    display_result(game.is_victory())
    print(f"The word was: {game.word_manager.word}")

# Allows several sessions to be played in a row until the user chooses to stop playing.
if __name__ == "__main__":
    while True:
        run_game()
        if not play_again():
            print("Thanks for playing Python Hangman!")
            print("See you next time!")
            break
        