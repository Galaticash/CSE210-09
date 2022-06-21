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
  - Players keep moving and turning but don't run into each other. <-- see professor's Snake example

## Classes
We'll try and reach the goal of 16 classes by making a lot of smaller classes and more base classes

| Class | Job |
| ----- | --- |
Director | Directs the inner workings of the game
Collision Handler | Handles all the Actor collisions for the Director
Hitbox | Makes it easier for the Collision Handler to remember the hitbox range per Actor (all Actors possess a hitbox that Collision Handler can calculate for them?)
Actor | The base class for items moving around the screen
Cast | The collection of Actors that the Director is in charge of, has methods to move/update the position of all Actors
Player/Cycle | Moves around the screen, interacting with the other Player
Trail | The pieces following the Player/Cycle, inherits from Actor. Kept within the Player/Cycle class
Player Input | Moves the Player around the screen, different key_set per Player
Key_set | A set of keys, given the up/down/left/right value
Score | Within the Player class, keeps track of the points gained by the Player
Message | The base class for Score, so the GUI can display any message like the Game Over. Contains the location, font size, color, etc for the GUI to display
Point | point/grid location separated into its own class
Color | colors are separated into its own class
Window | The GUI of the program, displays everything to the user

- Score - remake to inherit from Message (A type of message that updates itself)
- Player_input - remake to fit with key_set pyray.is_key_down(key_set.get_up_key())


| Member | Classes to Program |
| ------ | ------------------ |
Ashley | Director, Actor (base class for Player, Trail, AND Message), other classes as added
Hailey | Graphic Interface/Window, Point (x/y position), Color (can use pyray Colors OR python colors (rgb values))
Matt | key_set, player_input, Player/Cycle, Trail/Trail_piece
John | Score, Message (base class for Score), Cast
Ethan | Collision Handler, Hitbox (can be an Attribute of Player and Trail Piece*)

* OR can have another base class from Actor like Actor_collidable (Since Messages inherit from Actor but shouldn't have hitboxes)

# Week 10 - Cycle Program
## Team Members in attendance 6/23 (Programming): 


## TODO: Implementation
- [ ] Code each class out
  - [ ] Director
  - [ ] Collision Handler
  - [ ] Hitbox
  - [ ] Cast
  - [ ] Window/Grahpical Interface
  - [ ] Actor
  - [ ] Player
  - [ ] Player Input
  - [ ] Key Set
  - [ ] Tail Piece
  - [ ] Message
  - [ ] Score
  - [ ] Point
  - [ ] Color

## Extra
- Enhanced scoring and game reset.
- Enhanced game play and game over messages.
- Enhanced game display, e.g. cycle and trails
