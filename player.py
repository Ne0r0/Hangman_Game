
class Player:
    '''
    Repersents the player, tracking lives and guessed letters.
    '''
    def __init__(self, lives: int) -> None:
        self.lives: int = lives
        self.guessed_letters: set[str] = set()


    def guess_letter(self, letter: str) -> None:
        '''
        Adds a guessed letter to the set of guessed leeters.
        '''
        letter = letter.upper()
        self.guessed_letters.add(letter)


    def guess_word(self, word: str, correct_word: str) -> bool:
        '''
        Checks if the guessed word matches the correct word.
        Updates guessed letters if correct, halves lives if incorrect.
        '''
        word = word.upper()
        correct_word = correct_word.upper()

        if word == correct_word:
            for letter in correct_word:
                self.guessed_letters.add(letter)
            return True
        else:
            self.lives = self.lives // 2
            if self.lives < 0:
                self.lives = 0
            return False


    def take_damage(self) -> None:
        '''
        Reduces player's lives by one.
        '''
        self.lives = self.lives - 1


    def has_lives(self) -> bool:
        '''
        Returns True if the player has remaining lives.
        '''
        if self.lives > 0:
            return True
        return False
    