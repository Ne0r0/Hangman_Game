import random

# Paleidžia žaidimą: pasirenka žodį, nustato gyvybes, išvalo spėjimus.
class HangmanGame:
    def __init__(self, word_list, lives=5):  # DEBUG lives=5. Default for game lives=10
        self.word = random.choice(word_list).upper()
        self.guessed_letters = set()  # Spėjimų istorija pradedama nuo nulio
        self.lives = lives

# Tikrina, ar žaidėjas atspėjo visas raides — tuomet žaidimas laimėtas.
    @property
    def is_game_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

# Tikrina, ar gyvybės pasibaigusios — žaidimas pralaimėtas.
    @property
    def is_game_over(self):
        return self.lives <= 0

# Atlieka spėjimą viena raide. Patikrina, ar raidė teisinga, jei ne — atima gyvybę.
    def guess_letter(self, letter: str):
        letter = letter.upper()
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.lives -= 1

# Leidžia spėti visą žodį. Jei atspėtas — laimima, jei ne — gyvybės bauda.
    def guess_word(self, guess: str):
        guess = guess.upper()
        if guess == self.word:
            self.guessed_letters.update(self.word)
        else:
            self.lives -= 1

# Grąžina žodį su atskleistomis raidėmis ir _, pvz. _ A _ _ E _.
    def display_word_progress(self) -> str:
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
