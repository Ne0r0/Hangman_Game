import random
from parameters import DEFAULT_LIVES

# Paleidžia žaidimą: pasirenka žodį, nustato gyvybes, išvalo spėjimus.
class HangmanGame:
    def __init__(self, word_list, lives=DEFAULT_LIVES):
        self.word = random.choice(word_list).upper()
        self.guessed_letters = set()  # Spėjimų istorija pradedama nuo nulio (unikalio reikšmės)
        self.lives = lives

# Tikrina, ar žaidėjas atspėjo visas raides — tuomet žaidimas laimėtas.
    @property
    def is_game_won(self) -> bool:
        for letter in self.word:
            if letter.upper() not in self.guessed_letters:
                return False
        return True

# Tikrina, ar gyvybės pasibaigusios — žaidimas pralaimėtas.
    @property
    def is_game_over(self):
        return self.lives <= 0

# Apdoroja raidės spėjimą: įtraukia į spėtas ir sumažina gyvybę, jei raidė neteisinga.
    def guess_letter(self, letter: str):
        letter = letter.upper()
        self.guessed_letters.add(letter)
        if letter not in self.word:
            print("❌ Wrong letter!")
            self.lives -= 1

# Leidžia spėti visą žodį. Jei atspėtas — laimima, jei ne — gyvybės bauda.
    def guess_word(self, guess: str):
        guess = guess.upper()
        if guess == self.word:
            self.guessed_letters.update(self.word)
        else:
            print("❌ Wrong word! You lose half your lives.")
            self.lives = max(0, self.lives // 2)

# Grąžina žodį su atskleistomis raidėmis ir _, pvz. _ A _ _ E _.
    def display_word_progress(self) -> str:
        progress = []

        for letter in self.word:
            if letter.upper() in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append('_')

        return ' '.join(progress)
