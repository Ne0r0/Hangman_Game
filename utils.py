import random

win_faces = [r"\(^▽^)/", r"\(^_^)/","*(^o^)*","(◕ ˬ ◕✿)", "(づ｡◕‿‿◕｡)づ"]

lose_faces = ["(x_x)", "(>_<)", "(-_-;)", "(=_=)", "(≖ ‸ ≖ ✿)", "(ﹷ _ ﹷ✿)"]

def display_result(win: bool) -> None:
    if win:
        print("🎉 You won! 🎉")
        print(random.choice(win_faces))
    else:
        print("☠️ Game Over ☠️")
        print(random.choice(lose_faces))

def play_again() -> bool:
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")
