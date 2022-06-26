import pyray

FRAME_RATES = {"easy": 12, "medium": 30, "hard": 60}
FRAME_RATE = FRAME_RATES["medium"]

"""
    Note: The GUI does NOT update the position of anything, only displays their current position.
    Requires:
        A Cast with:
            Player, inherits from Actor
            Messages, inherits from Actor
"""
class Window():
    """
        A Window which updates a visual representation of the state of the Game.
        __init__() will create the window
        .close() will close the window
        .update(self, cast) will update the graphical positions of all of the cast members
    """
    def __init__(self, width, height):
        # Given a width and height, creates a new window
        self._width = width
        self._height = height
        pyray.init_window(self._width, self._height, "Cycle Game - Team F")
        # Has a const set Frame Rate, limits number of updates
        pyray.set_target_fps(FRAME_RATE)

    def _print_actor(self, actor):
        """
            Prints the given actor on the board. All variables used are recieved from the actor itself.
        """
        pyray.draw_text(actor.get_display(), actor.get_x(), actor.get_y(), actor.get_font_size(), actor.get_color())

    def _print_button(self, button):
        """
            Prints the given button on the board. Has a box surrounding it to differentiate itself as a button.
        """
        pyray.draw_rectangle(button.get_hitbox().left, button.get_hitbox().top, button.get_hitbox().right - button.get_hitbox().left, button.get_hitbox().bottom - button.get_hitbox().top, pyray.RED)
        pyray.draw_text(button.get_display(), button.get_x(), button.get_y(), button.get_font_size(), button.get_color())
        self._print_hitbox(button.get_hitbox())

    def _print_hitbox(self, hitbox):
        """
            Draws a given hitbox with red lines.
        """
        # Draw the top line
        pyray.draw_line(hitbox.left, hitbox.top, hitbox.right, hitbox.top, pyray.RED)
        # Bottom
        pyray.draw_line(hitbox.left, hitbox.bottom, hitbox.right, hitbox.bottom, pyray.RED)
        # Left
        pyray.draw_line(hitbox.left, hitbox.top, hitbox.left, hitbox.bottom, pyray.RED)
        # Right
        pyray.draw_line(hitbox.right, hitbox.top, hitbox.right, hitbox.bottom, pyray.RED)

    def update(self, cast):
        """
            Draws a frame of the Game given the actors.
        """
        # Refreshes the board to black
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        
        # Shows the center of the screen.
        # pyray.draw_line(self._width//2, 0, self._width//2, self._height, pyray.RED)
        # pyray.draw_line(0, self._height//2, self._width, self._height//2, pyray.YELLOW)

        # Updates the Players
        for player in cast.get_players():
            self._print_actor(player)
            for trail_piece in player.get_trail():
                self._print_actor(trail_piece)

        # Updates the Messages
        for message in cast.get_messages():
            self._print_actor(message)

        for button in cast.get_buttons():
            self._print_button(button)

        pyray.end_drawing()

    def should_close(self):
        return pyray.window_should_close()

    def close(self):
        """
            Closes the window. Called at the end of the program.
        """
        pyray.close_window()