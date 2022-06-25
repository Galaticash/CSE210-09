from actors.actor import *

class Message(Actor):
    def __init__(self, max_x, max_y, font_size, message, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        self._message = message
        # Centers the message in the middle of the screen.
        self._position = Point(self._max_x, self._max_y, (self._max_x - (int(len(self._message)/2 * self._font_size)))//2, (self._max_y - self._font_size)//2)
        

    def get_display(self):
        """
            Returns the string that is used to display the Actor.
        """
        return self._message
