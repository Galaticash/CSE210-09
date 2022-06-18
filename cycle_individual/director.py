from collision_handler import Cast, Collision_Handler
from graphical_interface import Window

WINDOW_MAX_X = 900
WINDOW_MAX_Y = 600
FONT_SIZE = 25

class Director():
    """
        The Director class (add comment here)
    """
    def __init__(self):
        self._game_over = False
        # Add all the constants
        self._max_x = WINDOW_MAX_X
        self._max_y = WINDOW_MAX_Y
        self._font_size = FONT_SIZE

        # Create a Window to display things on
        self._window = Window(self._max_x, self._max_y, self._font_size)
        # Create a Cast to add Players and Messages to
        self._cast = Cast()
        # Create a Collision Handler to manage collisions between Actors
        self._collision_handler = Collision_Handler()

    def start_game(self):
        """
            Begin the Cycle game. Create the two players
        """
        # Add Player 1
        self._cast.add_player([self._max_x, self._max_y, self._font_size])

        # Add Player 2 - Cycle class is in charge of differentiating spawn_position, etc
        self._cast.add_player([self._max_x, self._max_y, self._font_size], 2)

    def update_game(self):
        """
            Updates the game based on Player movement and the falling Rocks. 
        """
        # Checks if the window should close (X button pressed).
        if self._window.should_close():
            self._game_over = True
        # Otherwise, gameplay as normal.
        else:
            # Move all members of the cast
            self._cast.move()
            
            # Check for collisions
            self._collision_handler.check()

            # Updates the visuals of the game
            self._window.update(self._cast)

    def get_game_over(self):
        """
            Returns to main if the game has finished.
        """
        return self._game_over

    def end_game(self):
        """
            Ends the game by closing the window. Additional things can be added
              like adding a game over animation/screen.
        """
        self._window.close()

# Game can also just be run from Director
if __name__ == "__main__":
    cycle_game = Director()
    cycle_game.start_game()
    while not cycle_game.get_game_over():
        cycle_game.update_game()    
    cycle_game.end_game()