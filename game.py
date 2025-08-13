from word_manager import WordManager
from player import Player
from parameters import DEFAULT_LIVES

class HangmanGame:
    '''
    Coordinates the Hangman game logic, including word management and player actions.
    '''
    def __init__(self, word_list: list[str], lives: int=DEFAULT_LIVES):
        self.word_manager = WordManager(word_list)
        self.player = Player(lives)


    def guess_letter(self, letter: str) -> None:
        '''
        Processes a single letter guess and applies damage if incorect.
        '''
        self.player.guess_letter(letter)
        if not self.word_manager.contains_letter(letter):
            print("❌ Wrong letter!")
            self.player.take_damage()


    def guess_word(self, word: str) -> None:
        '''
        Processes a full word guess. If incorrect, halves the player's lives.
        '''
        success = self.player.guess_word(word, self.word_manager.word)
        if not success:
            print("❌ Wrong word! You lose half your lives.")


    def is_victory(self) -> bool:
        '''
        Checks if the player has guessed all letters correctly.
        '''
        return self.word_manager.is_complete(self.player.guessed_letters)


    def is_defeat(self) -> bool:
        '''
        Checks if the player has run out of lives.
        '''
        return not self.player.has_lives()


    def display_word_progress(self) -> str:
        '''
        Returns the current word progress with guessed letters and underscores.
        '''
        return self.word_manager.display_word_progress(self.player.guessed_letters)
