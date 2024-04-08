AI Autoplay for the game 2048
Found on Andy's github. https://github.com/MrSquiggles34/2048AI
===========
Based on the popular game [2048](https://github.com/gabrielecirulli/2048) by Gabriele Cirulli. The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048. 

To start the game, run:
    $ python3 puzzle.py

This is a Python implementation of the  2048 game, featuring an AI autoplay mode using a custom algorithm.

Features ------------
Play the 2048 game with arrow keys or alternative keys (WASD or IKJL).
Activate AI autoplay mode to let the computer play the game for you (press "Q" key).
AI autoplay uses a custom algorithm which implements a Monte-carlo tree to make intelligent moves based on game state analysis.
Utilizes multi-threading to prevent GUI crashes. 


Evaluation: -----------------

The core of the scoring system lies in the ai_move function, which evaluates potential moves and assigns a grade to each move.
The function iterates through possible first moves and simulates future game states to evaluate their quality.

For each potential first move, the AI simulates multiple sequences of random moves to explore future game states.
Within each sequence, the AI makes random moves to simulate possible game outcomes.
After each sequence, the AI evaluates the resulting game state and assigns a score based on certain criteria.

How to Play -----------------------
Run the game_2048.py script to start the game.
Activate AI autoplay mode by pressing the "Q" key.

Dependencies -----------------------------
Python 3.x
numpy library
matplotlib library
tkinter library

Install dependencies using pip: ---------
pip install numpy matplotlib
python game_2048.py

Customization
Adjust game parameters and AI algorithm settings in the constants.py and ai_2048.py files.

The 2048 game in Python was built by:
- [Yanghun Tay]
- [Emmanuel Goh]
