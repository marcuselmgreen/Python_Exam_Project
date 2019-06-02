# Python Exam Project - BlackJack game
This project makes use of simple_colors to be able to change the color of a text print.

The game starts of explaining the rules, and then you're given the option play as the player or the dealer.
As a player you start of with 1000 chips, and at the end of the game, the amount of chips that you bet will increase or decrease the chips available in the next game.
The player is given options throughout the game:
1. Hit
2. Stand
3. Double down
4. Surrender

If the dealers upcard is an ace, the player is also given the option to receive insurance.

The results of a game include:
1. Bust
2. Normal win
3. Blackjack win (1.5 times value of the bet)
4. Push

If a player hits 0 chips the game will have to be restarted to reset the chips back to 1000.

As a dealer, the game is played out automatically.


## Installation
First you'll want to use a virtual enviroment.
If you're already using one then you'll need to deactivate it.
```
$ deactivate
```
```
$ python -m venv tutorial_2_env
$ source tutorial_2_env/bin/activate

# on windows in git bash
$ source tutorial_2_env/Scripts/activate
```

The next thing you'll need to do is to clone this repository using GIT CLONE:
```
$ git clone https://github.com/marcuselmgreen/Python_Exam_Project.git
```

To run the project you need to install the dependency - simple_colors:
```
$ pip install -r requirements.txt
```

Go to the folder that you've cloned:
```
$ cd Python_Exam_Project
```

Now you can run the game:
```
python BlackJack.py
```
