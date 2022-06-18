import pyray

# Since it adjust the update speed, can be used for difficulty/speed of the game
FRAME_RATES = {"easy": 12, "medium": 30, "hard": 60}
FRAME_RATE = FRAME_RATES["easy"]

"""
    Requries:
        Does NOT update the position of anything, only displays their current position
        Player, based off of Actor (inherits all methods)
        Array of Food, for the Snake to eat (will default to 1, but can increase number of)
    
        Actor base class
            .get_character --> returns the character to print
            .get_x --> x position (0,0 being the top left)
            .get_y --> y position (0,0 being the top left)
            .get_color --> a pyray color
            .get_font_size --> also can adjust

        Player
            .get_score() --> returns player's current score
                Used to display to User
"""

class Window():
    """
        A Window which updates the visual representation of the Game.
        __init__() will create the window
        .close() will close the window
        .update(player, rocks) will update the graphical positions of the Actors
    """
    def __init__(self, width, height, font_size):
        # Given a width and height, creates a new window
        self._width = width
        self._height = height
        pyray.init_window(self._width, self._height, "Cycle Game - DeMott")
        
        # Has a const set Frame Rate, limits number of updates
        pyray.set_target_fps(FRAME_RATE)
        
        # Font size for messages
        self._text_size = int(font_size * 2)

    def _print_message(self, message):
        """
            Displays a Message on the window.
        """
        pyray.draw_text(message.get_message(), message.get_x(), message.get_y(), message.get_font_size(), message.get_color())

    def _print_actor(self, actor):
        """
            Prints the given actor on the board. All variables used are recieved from the actor itself.
        """
        pyray.draw_text(actor.get_symbol(), actor.get_x(), actor.get_y(), actor.get_font_size(), actor.get_color())

    def update(self, cast):
        """
            Draws a frame of the Game given the actors.
        """
        # Refreshes the board to black
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        
        # Update all the Players on the Screen
        for player in cast.get_players():
            self._print_actor(player)

        # Update all the Messages on the Window
        self._print_message(cast.get_messages()["Score1"])
        self._print_message(cast.get_messages()["Score2"])

        pyray.end_drawing()

    def should_close(self):
        return pyray.window_should_close()

    def close(self):
        """
            Closes the window. Called at the end of the program.
        """
        pyray.close_window()

