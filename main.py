from game import HangmanGame
from words import python_words
from art import hangman_pics
from utils import display_result, play_again
from logger_for_game import game_logger
import logging

# Paleidžia log'ų sistemą – pasirenkama, ar rašyti į terminalą ar į failą.
game_logger()

# Pagirndinė žaidimo paleidimo funkcija.
def run_game():
    game = HangmanGame(python_words)  # Sukuria žaidimo objektą su atsitiktiniu Python žodžiu ir pradiniu gyvybių skaičiumi.
    warned_once = False  # Redflag, kuris leidžia parodyti įspėjimą dėl neteisingos įvesties tik vieną kartą.
    logging.info(f"🎮 New game started. Word length: {game.word}")

    print("🎯 Welcome to Python Hangman!")
    print(game.display_word_progress())  # Pradinio žodžio progresas (raidės vs _)
    print(f"You have {game.lives} lives.\n")

# Žaidimo ciklas – kol dar ne laimėta ir dar yra gyvybių, leidžia spėlioti.
    while not game.is_game_won and not game.is_game_over:
        stage = len(hangman_pics) - game.lives - 1 # Kuo mažiau HP tuo arčiau pakarimo
        print(hangman_pics[stage])

 # Rodomas pakaruoklio etapas pagal gyvybių kiekį
        guess = input("Enter a letter or guess the full word: ").strip()  # User spėja raides arba visą žodį.
        logging.info(f"Player guessed: {guess}")

# Tikrina, ar įvestis sudaryta iš raidžių – kitaip parodo įspėjimą arba atima gyvybę.
        if not guess.isalpha():
            logging.warning(f"⚠️ Invalid input: '{guess}' | Lives before penalty: {game.lives}")
            print("⚠️ Only letters allowed!" if not warned_once else "❌ Invalid input → -1 life penalty.")
            if warned_once:
                game.lives -= 1  # Antras bandymas spėti ne raidę -1 hp
                logging.info(f"Penalty applied. Lives now: {game.lives}")
            warned_once = True
            continue

# Vienos raidės spėjimas
        if len(guess) == 1:
            if guess.upper() in game.guessed_letters:
                print("⚠️ You've already guessed that letter.")
                logging.info(f"Repeat guess: {guess}")
                continue
            game.guess_letter(guess)
            logging.info(f"Letter guessed: {guess.upper()} | Lives left: {game.lives}")
        else:
            logging.info(f"Word attempt: {guess.upper()}")
            game.guess_word(guess)
            logging.info(f"Lives after word guess: {game.lives}")
            
# Rodomas dabartinis žodžio progresas ir gyvybės
        print("\n" + game.display_word_progress())
        print(f"Guessed letters: {', '.join(sorted(game.guessed_letters))}")
        print(f"Lives left: {game.lives}\n")
        logging.info(f"Lives left: {game.lives} | Word progress: {game.display_word_progress()}")

    result = "WON" if game.is_game_won else "LOST"
    logging.info(f"🏁 Game ended. Result: {result} | Word was: {game.word}")
    display_result(game.is_game_won)
    print(f"The word was: {game.word}")

if __name__ == "__main__":
    while True:
        run_game()
        if not play_again():
            print("Thanks for playing Python Hangman!")
            print("See you next time!")
            break
        