from castDeMott import Cast
from actors.cycleDeMott import *
from actors.messageDeMott import Message
from actors.buttonDeMott import Button
from collisionHandlerDeMott import Collision_Handler
from GraphicInterface import Window
from mouse_input import Mouse_Input

WINDOW_MAX_X = 900
WINDOW_MAX_Y = 600
FONT_SIZE = 25

class Director():
    """
        Directs the inner workings of the Cycle game.
    """
    def __init__(self):
        self._game_over = False
        self._window_close = False
        # Add all the constants
        self._max_x = WINDOW_MAX_X
        self._max_y = WINDOW_MAX_Y
        self._font_size = FONT_SIZE

        # Create a Window to display things on
        self._window = Window(self._max_x, self._max_y)
        # Create a Cast to add Players and Messages to
        self._cast = Cast()
        # Create a Collision Handler to manage collisions between Actors
        self._collision_handler = Collision_Handler(self._cast)

        # Create a Mouse_input
        self._mouse = Mouse_Input()

    def start_game(self):
        """
            Begin the Cycle game. Create the two players
        """
        # Add each of the Players to the Cast.
        self._cast.add_player(Player(self._max_x, self._max_y, self._font_size))
        self._cast.add_player(Player2(self._max_x, self._max_y, self._font_size))

        # Update the collision handler.
        self._collision_handler.update_colliders()

    def update_game(self):
        """
            Updates the game based on Player movement and the falling Rocks. 
        """
        # Move all members of the cast.
        self._cast.move_players()
        
        if not self._game_over:
            # Check for collisions, if the Cycles collide, the game is over.
            self._game_over = self._collision_handler.check()
            if self._game_over:
                self.add_game_over()
        else:
            # Check for "Play Again" or "Exit" click            
            mouse_position = self._mouse.click_position()

            # If the mouse was clicked
            if not (mouse_position == None):
                # Check if the user chose to play again (based on which button is clicked).
                play_again = self._cast.check_replay_buttons(mouse_position)
                if not (play_again == None):
                    if play_again:
                        self.replay()
                    else:
                        self._window_close = True
                        return

        # Updates the visuals of the game.
        self._window.update(self._cast)

        # Checks if the window should close (X button pressed).
        self._window_close = self._window.should_close()

    def add_game_over(self):
        game_over_size = self._font_size * 2
        button_size = int(self._font_size * 1.5)
        center = [(self._max_x - (int(len("Game Over")/2 * game_over_size)))//2, (self._max_y - game_over_size)//2]
        x_offset = game_over_size * 2
        y_offset = int(game_over_size * 1.5)
        
        # Add the Game Over message
        self._cast.add_message(Message(self._max_x, self._max_y, center, game_over_size, "Game Over"))
        
        # Add Play Again and Exit Buttons to the cast
        self._cast.add_button("PLAY_AGAIN", Button(self._max_x, self._max_y, [center[0] - (x_offset//2), center[1] + y_offset], button_size, "Play Again"))
        self._cast.add_button("EXIT", Button(self._max_x, self._max_y, [center[0] + (2 * x_offset), center[1] + y_offset], button_size, "Exit"))

    def replay(self):
        """
            Resets the game, but keeps the current scores.
        """
        self._game_over = False
        self._cast.remove_game_over()
        self._cast.remove_buttons()
        self._cast.reset_players()
    
    def get_window_close(self):
        """
            Returns to main if the game window has been closed.
        """
        return self._window_close

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
    # Slightly different here, window will not close until user presses the "X" button.
    while not cycle_game.get_window_close():
        cycle_game.update_game()
    cycle_game.end_game()