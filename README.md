# Week 9 - Cycle Design
## Team Members: Ashley, Hailey, John, Matt, Ethan

## Cycle Game
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

# TODO: Design
## Team Members in attendance 6/16 (Designing): Ashley, Hailey
Requirements:
- Players can move up, down, left and right...
  - Player one moves using the W, S, A and D keys.
  - Player two moves using the I, K, J and L keys.
- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail...
  - A "game over" message is displayed in the middle of the screen.
  - The cycles turn white.
  - Players keep moving and turning but don't run into each other. (???)

## Classes
I do not think we can make 16 classes, so we'll only plan for as many as we need

| Class | Job |
| ----- | --- |
Director | Directs the inner workings of the game
Collision Handler | Handles all the Actor collisions for the Director
Actor | The base class for items moving around the screen
Player/Cycle | Moves around the screen, interacting with the other Player
Trail | The pieces following the Player/Cycle, inherits from Actor. Kept within the Player/Cycle class
Player Input | Moves the Player around the screen, different key_set per Player
Key_set | 
Score | Within the Player class, keeps track of the points gained by the Player
Message | The base class for Score, so the GUI can display any message like the Game Over. Contains the location, font size, color, etc for the GUI to display
Grid | A grid to keep the cycles on, but needs to be translated back into pixel/points by the GUI
Point | point/grid location separated into its own class
Color | colors are separated
Window | The GUI of the program, displays everything to the user
Trail? Trail piece? | 

Score - remake to inherit from Message (A type of message that updates itself)

TODO: Assign jobs

| Member | Classes to Program |
| ------ | ------------------ |
Ashley | Director
Hailey | -
Matt | -
John | -
Ethan | -

# Week 10 - Cycle Program
## Team Members in attendance 6/23 (Programming): 

## TODO: Implementation
- [ ] Code each class out


## Extra
- Enhanced scoring and game reset.
- Enhanced game play and game over messages.
- Enhanced game display, e.g. cycle and trails
