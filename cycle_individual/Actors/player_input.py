import pyray

class Key_Set():
    def __init__(self, keys):
        self._up_key = keys[0] # W
        self._left_key = keys[1] # A
        self._down_key = keys[2]  # S
        self._right_key = keys[3] # D

    def get_up(self):
        return self._up_key

    def get_down(self):
        return self._down_key

    def get_left(self):
        return self._left_key

    def get_right(self):
        return self._right_key

class Player_Input():
    def __init__(self, keys):
        self._keys = Key_Set(keys)
        # Player 1: 
        # Player 2: [pyray.KEY_I, pyray.KEY_J, pyray.KEY_K, pyray.KEY_L]
        self._dx = 0
        self._dy = 0

    def set_keys(self, new_keys):
        """
            Given an array of 4 pyray keys, changes the up/down and left/right buttons
        """
        self._keys = Key_Set(new_keys)

    def get_direction(self):
        """
            Changes the values of dx and dy and returns them.
            If X is changed, Y is reset, and vice versa.
        """
        # The Left/Right directions
        if pyray.is_key_down(self._keys.get_left()):
            self._dx = -1
            self._dy = 0
        elif pyray.is_key_down(self._keys.get_right()):
            self._dx = 1
            self._dy = 0

        # The Up/Down directions
        if pyray.is_key_down(self._keys.get_up()):
            self._dy = -1
            self._dx = 0
        elif pyray.is_key_down(self._keys.get_down()):
            self._dy = 1
            self._dx = 0
        
        return [self._dx, self._dy]