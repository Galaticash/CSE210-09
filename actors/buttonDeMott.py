from actors.messageDeMott import Message
from hitboxDeMott import Hitbox

class Button(Message):
    def __init__(self, max_x, max_y, font_size, message, color="WHITE"):
        super().__init__(max_x, max_y, font_size, message, color)
        self._hitbox = Hitbox(len(self._message)//2, self._font_size//2, 15)
        self._hitbox.update(self._position)

    def get_hitbox(self):
        """
            Returns the Button's hitbox (which is where it can be clicked).
        """
        return self._hitbox

    def pressed(self, cursor_position):
        """
            Returns if the button hitbox has been pressed (The cursor clicks inside the hitbox range)
        """
        return self._hitbox.is_hit(cursor_position)