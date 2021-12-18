# Tic-Tac-Toe
# Project title:
Tic-Tac-Toe A.I.
# Technical requirement:
Prolog -> SWI prolog
Python -> VS code
# Project Description:
A Tic-Tac-Toe Artificial Intelligence program that tells what is the best move to win the game with an explanation of the A.I. generated outcome. This is the program where you can practice how to play Tic-Tac-Toe with the smartest move and to win within the shortest time. This game implements the Prolog programming language and Python.
Tic-tac-toe is a very popular game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a vertical, horizontal or diagonal row wins the game.
# AI concepts applied in the project
The algorithm implemented in this project is akin to a Utility-based agent, in which it tries to accomplish the goal which is predicting the best moves of the game by observing the placement of the symbol. 
Property 1: The game admits the player that uses this optimal strategy will win or draw but it will not lose.
Property 2: The number of possible different matches is relatively small.
From properties 1 and 2 it follows that a practical, and general, algorithm to win/draw the game is to use the Alpha Beta search.
At each turn the algorithm evaluates all the possible consequences of each move (possible due to property 2) and chooses the one that will ensure a victory or a draw (possible due to property 1).
An AI player that chooses each move with the alpha beta search algorithm will never lose. To make the game more realistic it is nice to introduce a stochastic factor so that each time with a predefined probability the AI player moves randomly rather than following the alpha beta algorithm. This will make the game more realistic as it will make the AI player more human and sometimes it will lose.

