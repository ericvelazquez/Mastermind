# Mastermind
Mastremind API

To start the game please run: python game.py

Th input for the codemaker/codebreaker should be the initial of the color. For the code [Red, Blue, Green, Red], the input should be rbgr. If the input is not valid, the game will ask again for the input and will not count it as an attempt.

## Classes

The classes of this project are:

* [Board] - Rest API of the game.
* [Player] - Asks the players (Codemaker/Codebreaker) for an input. If the input is valid, calls Board fucntions.
* [Game] - Makes the workflow of the game. Keeps asking for a guess (using Player fucntions) until the codebreaker is out of attempts or has guessed the solution.

