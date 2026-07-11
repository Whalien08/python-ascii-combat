# Terminal Stickman Combat 🗡️

A lightweight, turn-based terminal RPG where you battle a randomized roster of enemies using various weapons, featuring frame-by-frame ASCII art animations. 

This project is a heavily refactored, modularized, and English-translated version of an original Dutch terminal game. The core game loop has been rewritten to use clean Python dictionaries, modular drawing functions, and structured animation sequences.

## 🚀 Features
*   **Frame-by-Frame ASCII Animations:** Custom animations for every weapon, including Machine Guns, Grenades, Fireballs, and Enemy Motorcycles.
*   **Dynamic Combat System:** Randomized weapon damage, heal ranges, and dynamic enemy encounters.
*   **Clean Architecture:** Weapon stats and hitpoints are stored in easily expandable dictionaries rather than disjointed variables.
*   **Modular Rendering:** Uses abstracted `draw_frame()` and `play_animation()` functions to keep the main game loop clean and maintainable.

## 🛠️ Prerequisites
*   Python 3.x
*   A terminal/command prompt that supports basic clearing functions (`cls` for Windows, `clear` for macOS/Linux).

## 🎮 How to Play
1. Clone or download this repository.
2. Open your terminal and navigate to the project folder.
3. Run the script:
   ```bash
   python main.py

    Enter your character's name and press Enter to start the encounter spin.

    On your turn, select a weapon (1-5) to attack or heal. Survive until the enemy's HP hits 0!

📂 Code Structure

    WEAPONS Dictionary: Add, balance, or modify weapons easily without hunting through the game loop.

    NAMES List: Expand the randomized pool of enemy combatants.

    play_animation(): Handles the timing and screen-clearing required to render the ASCII string arrays seamlessly.

🤝 Credits & Attribution

This project is an educational refactor. The original concept, base ASCII art, and initial Dutch logic were created by Jurre.

You can find the original, un-refactored source code here:
[](https://github.com/RVKE/Python-StickmanGame.git)

Modifications in this version include:

    Full translation from Dutch to English.

    Removal of repetitive while True spaghetti code.

    Implementation of helper functions for drawing and timing.

    Data structure improvements (grouping discrete variables into unified dictionaries).

📝 License

This adapted version respects the #Copyright reserved tag of the original creator. It is shared for educational and portfolio purposes to demonstrate Python refactoring and modularization.
