#from [To be implemented - CAST] import Cast
# frmo [To be implemented - COLLISION HANDLER] import Collision_Handler
#from [To be implemented - WINDOW/GUI] import Graphical Interface

WINDOW_MAX_X = 900
WINDOW_MAX_Y = 600
FONT_SIZE = 25

class Director():
    """
        Directs the inner workings of the Cycle game.
    """
    def __init__(self):
        self._game_over = False
        # Add all the constants
        self._max_x = WINDOW_MAX_X
        self._max_y = WINDOW_MAX_Y
        self._font_size = FONT_SIZE

        # Create a Window to display things on
        # self._window = [WINDOW/GUI] Window(self._max_x, self._max_y, self._font_size)
        # Create a Cast to add Players and Messages to
        # self._cast = [CAST] Cast()
        # Create a Collision Handler to manage collisions between Actors
        # self._collision_handler = [COLLISION HANDLER] Collision_Handler()
    
    def start_game(self):
        """
            Begin the Cycle game. Create the two players
        """
        # TODO: 
        # [CAST Method - Adds a player to the Cast object. 
        #   Cast will have each of the Actors to be displayed on the board stored as an Attribute.
        #   Can add the Scores/Messages inside the add_player method with an inner Method add_message/add_score]
        # Add Player 1
        #self._cast.add_player([self._max_x, self._max_y, self._font_size])

        # Add Player 2 - Cycle class is in charge of differentiating spawn_position, etc
        # TODO: Should Player 2 be another Cycle object or a different class (Cycle2, inherits from Cycle)?
        #self._cast.add_player([self._max_x, self._max_y, self._font_size], 2)
        pass

    def update_game(self):
        """
            Updates the game based on Player movement and the falling Rocks. 
        """
        # Checks if the window should close (X button pressed).
        # [WINDOW Method - makes sure if the user pressed the "x" button, the game will end]
        if self._window.should_close():
            self._game_over = True
        # Otherwise, gameplay as normal.
        else:
            # Move all members of the cast
            # [CAST] self._cast.move()
            
            # Check for collisions
            # [COLLISION] self._collision_handler.check()

            # Updates the visuals of the game
            # [WINDOW/GUI] self._window.update(self._cast)
            pass

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