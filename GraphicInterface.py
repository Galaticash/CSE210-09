import pyray

#Step_size = FrameRate/12
FRAME_RATES = {"easy": 12, "medium": 30, "hard": 60}
FRAME_RATE = FRAME_RATES["easy"]

"""
    Requires:
        Does NOT update the position of anything, only displays their current position
        Player, based off of Actor (all the same base object type)
"""

class Window():
    """
        A Window which updates a visual representation of the state of the Game.
        __init__() will create the window
        .close() will close the window
        .update(self, cast) will update the graphical positions of all of the actors
    """
    def __init__(self, width, height):
        # Given a width and height, creates a new window
        self._width = width
        self._height = height
        pyray.init_window(self._width, self._height, "Greed Game - Team F")
        # Has a const set Frame Rate, limits number of updates
        pyray.set_target_fps(FRAME_RATE)


    def _print_actor(self, actor):
        """
            Prints the given actor on the board. All variables used are recieved from the actor itself.
        """
        pyray.draw_text(actor.get_display(), actor.get_x(), actor.get_y(), actor.get_font_size(), actor.get_color())

    def update(self, cast):
        """
            Draws a frame of the Game given the actors.
        """
        # Refreshes the board to black
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        
        # Updates the Players
        for player in cast.get_players():
            self._print_actor(player)

        # Updates the Messages
        for message in cast.get_message():
            self._print_actor(message)

        pyray.end_drawing()

    def should_close(self):
        return pyray.window_should_close()

    def close(self):
        """
            Closes the window. Called at the end of the program.
        """
        pyray.close_window()