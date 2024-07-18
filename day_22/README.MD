# Day 22: Pong Game

This is a simple Pong game implemented in Python using the Turtle library. The game involves two players, each controlling a paddle, trying to bounce the ball so that the opponent cannot return it.

## Features

- Two players can control the paddles using the keyboard.
- The ball moves automatically and bounces off the screen edges and paddles.
- The game keeps track of each player's score and displays it on the screen.

## How to Run the Project

1 - Make sure you are in the project directory.
2 - Run the main game file: python main.py
3 - Use the following keys to control the paddles:
    . Right player: Up and Down keys to move the paddle up and down.
    . Left player: W and S keys to move the paddle up and down.

## Project Structure

main.py: Contains the main code that initializes the screen, paddles, ball, and scoreboard, and manages the game logic.
paddle.py: Defines the Paddle class, which controls the paddle movement.
ball.py: Defines the Ball class, which controls the ball's movement and collisions.
scoreboard.py: Defines the Scoreboard class, which manages the players' scores.

## How to Play

Each player controls a paddle to bounce the ball.
The ball will bounce off the top and bottom edges of the screen and the paddles.
If the ball passes by one of the paddles, the opposing player scores a point.
The game will continue until you close the game window.