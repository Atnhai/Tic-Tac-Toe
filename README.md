# Tic-Tac-Toe
# Project title:
Tic-Tac-Toe A.I.
# Technical requirement:
Prolog -> SWI prolog 

Python -> VS code
# Project Description:
A Tic-Tac-Toe Artificial Intelligence program that can play Tic Tac Toe with you(computer will be the player). You can select X(first) and O(second). The computer will play their best to win.
Tic-tac-toe is a very popular game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a vertical, horizontal or diagonal row wins the game.

Property 1: The game admits the player that uses this optimal strategy will win or draw but it will not lose.

Property 2: The number of possible different matches is relatively small.

From properties 1 and 2 it follows that a practical, and general, algorithm to win/draw the game is to use the Alpha Beta search.
At each turn the algorithm evaluates all the possible consequences of each move (possible due to property 2) and chooses the one that will ensure a victory or a draw (possible due to property 1).

An AI player that chooses each move with the alpha beta search algorithm will never lose. To make the game more realistic it is nice to introduce a stochastic factor so that each time with a predefined probability the AI player moves randomly rather than following the alpha beta algorithm. This will make the game more realistic as it will make the AI player more human and sometimes it will lose.

