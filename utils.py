import random

win_faces: list[str]= [r"\(^▽^)/", r"\(^_^)/","*(^o^)*","(◕ ˬ ◕✿)", "(づ｡◕‿‿◕｡)づ"]
lose_faces: list[str] = ["(x_x)", "(>_<)", "(-_-;)", "(=_=)", "(≖ ‸ ≖ ✿)", "(ﹷ _ ﹷ✿)"]


def display_result(win: bool) -> None:
    '''
    Displays a win or lose message with a random face.
    '''
    if win:
        print("🎉 You won! 🎉")
        print(random.choice(win_faces))
    else:
        print("☠️  Game Over ☠️")
        print(random.choice(lose_faces))


def display_status(word_display: list[str], guessed_letters: set[str], lives: int) -> None:
    '''
    Displays current word progress, guessed letters and remaining lives.
    '''
    print("🔤 Word: " + " ".join(word_display))
    print("📜 Guessed letters: " + ", ".join(sorted(guessed_letters)))
    print(f"❤️ Lives left: {lives}")


def play_again() -> bool:
    '''
    Asks the user if they want to play again.
    Returns True if input starts with 'y' or 'Y'.
    '''
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")
