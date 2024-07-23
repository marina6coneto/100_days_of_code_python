# Day 23: Turtle Crossing

This repository contains the project for Day 23 of the "100 Days of Code: Python" course by Angela Yu.

## Features

- One player can control the turtle using the 'up' key on the keyboard.
- The turtle must cross the screen while avoiding obstacles.
- Each time the turtle successfully crosses the screen, the speed of the obstacles increases.

## How to Run the Project

1. Make sure you are in the project directory.
2. Run the main game file:
    ```bash
    python main.py
    ```

## Project Structure

- `main.py`: Contains the main code that initializes the game.
- `car_manager.py`: Manages the cars that move across the screen.
- `player.py`: Defines the `Player` class, which controls the turtle.
- `scoreboard.py`: Defines the `Scoreboard` class, which manages the player score.

## How to Play

1. Use the 'up' key to move the turtle forward.
2. Avoid the cars to reach the other side of the screen.
3. Each successful crossing increases the player's score and the speed of the obstacles.
