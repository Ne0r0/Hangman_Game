# 🎮 Python Hangman
```
A terminal-based version of the classic Hangman game, written in Python. 
The player guesses letters or the entire word, while incorrect guesses reduce the number of lives. 
The game visually displays progress using ASCII art and offers a playful experience with Python-themed words.
```
---

## 📖 Game Rules

- You have **10 lives** to guess a hidden Python-related word.
- You can guess either a **single letter** or try the **entire word**.
- Each incorrect **letter** guess subtracts 1 life.
- Each incorrect **word** guess halves your lives.
- Repeated invalid inputs also cost 1 life.
- The word progress is displayed with revealed letters and `_` for hidden ones.
- ASCII visuals show your remaining lives.
- Win by revealing all letters before your lives run out!

---

## 📦 Project Structure

| File / Folder           | Description                                      |
|-------------------------|--------------------------------------------------|
| `main.py`               | Handles user interaction and game loop          |
| `game.py`               | Core game logic: word selection, guess checks   |
| `player.py`             | Manages lives and guessed letters               |
| `word_manager.py`       | Tracks word progress and updates                |
| `art.py`                | ASCII art visuals for hangman stages            |
| `utils.py`              | End-of-game reactions and replay prompt         |
| `logger_for_game.py`    | Configurable logging for sessions               |
| `parameters.py`         | Game settings and constants                     |
| `words.py`              | Word list focused on Python-related terms       |
| `logs/`                 | Stores logs for game sessions

---
```
## ▶️ How to Run

In your terminal, enter:
python main.py
```
---

## 🧠 Features

- Object-oriented game logic with the `HangmanGame` class  
- Modular file structure for maintainability  
- ASCII visual stages that reflect lives remaining  
- Friendly win/lose animations using character faces  
- Input validation and optional logging to file  
- Replay prompt at the end of each session
- Python-themed vocabulary for extra geeky fun 🐍

---

## 👀 Example Output
```
🎯 Welcome to Python Hangman!
_ _ _ _ _ _
You have 5 lives.

Enter a letter or guess the full word: e
_ _ _ _ E _
Guessed letters: E
Lives left: 5
```