# Day 28: Pomodoro Timer

- A simple Pomodoro timer application built with Python and Tkinter.
- This application helps you manage your work and break intervals using the Pomodoro Technique.
- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu on Udemy.

## Features

- **Work Interval:** 25 minutes of focused work.
- **Short Break:** 5 minutes break after each work interval.
- **Long Break:** 20 minutes break after every 4 work intervals.
- **Visual Countdown:** Displays the remaining time for the current interval.
- **Session Tracking:** Displays check marks for completed work sessions.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Tkinter library (usually included with Python installations).
- An image file for the tomato timer (`tomato.png`). 

## Usage

- **Start Button:** Begins the Pomodoro timer.
- **Reset Button:** Resets the timer and session tracking.

## Code Overview

### Constants

- `PINK`, `RED`, `GREEN`, `YELLOW`: Color codes for UI elements.
- `FONT_NAME`: Font used in the application.
- `WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`: Duration settings for work, short break, and long break intervals.
- `reps`: Tracks the number of intervals completed.
- `check_mark`: Symbol used to indicate completed work sessions.
- `timer`: Holds the reference to the timer.

### Functions

- `reset_timer()`: Resets the timer and UI elements.
- `start_timer()`: Initiates the timer based on the current interval.
- `count_down(count)`: Handles the countdown mechanism and updates the UI.

### UI Setup

- Configures the main application window, canvas, buttons, and labels.



*This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu on Udemy.*
