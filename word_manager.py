import random

class WordManager:
    '''
    Manages the terget word and its progress during the game.
    '''
    def __init__(self, word_list: list[str]) -> None:
        chosen_word = random.choice(word_list)
        self.word: str = chosen_word.upper()


    def contains_letter(self, letter: str) -> bool:
        '''
        Checks if the word contains the given letter.
        '''
        letter = letter.upper()
        return letter in self.word


    def is_complete(self, guess_letters: set[str]) -> bool:
        '''
        Returns True if all letters in word have been guessed.
        '''
        for letter in self.word:
            if letter not in guess_letters:
                return False
        return True
    
    
    def display_word_progress(self, guessed_letters: set[str]) -> str:
        '''
        Returns the current progress of the word, showing guessed letters and underscores.
        '''
        progress: list[str] = []

        for letter in self.word:
            if letter in guessed_letters:
                progress.append(letter)
            else:
                progress.append('_')

        return ' '.join(progress)
