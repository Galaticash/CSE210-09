class Point():
    """
        The Point class (add description here)
    """
    def __init__(self, max_x, max_y, x_pos, y_pos):
        self._max_x = max_x
        self._max_y = max_y
        self._x_pos = x_pos
        self._y_pos = y_pos
        # TODO: Remove this code from add_velocity(), was to try and get rid 
        # of flickering/player not being visible, but didn't really work
        self._border_buffer = 0

    def set_position(self, new_x, new_y):
        """
            Sets a new [x, y] position.
        """
        self._x_pos = new_x
        self._y_pos = new_y

    def get_position(self):
        """
            Returns the position as an array[].
        """
        return [self._x_pos, self._y_pos]

    def add_velocity(self, dx, dy):
        """
            Changes the Point position based on the change in direction.
        """
        # Update the x position
        self._x_pos += dx
        
        # Loop over the horizontal axis
        if self._x_pos > (self._max_x - self._border_buffer):
            self._x_pos = 0
        elif self._x_pos < (0 + self._border_buffer):
            self._x_pos = self._max_x
        
        # Update the y position
        self._y_pos += dy
        
        # Loop over the vertical axis
        if self._y_pos > (self._max_y - self._border_buffer):
            self._y_pos = 0
        elif self._y_pos < (0) + self._border_buffer:
            self._y_pos = self._max_y

    def get_x(self):
        """
            Returns the integer x position.
        """
        return self._x_pos

    def get_y(self):
        """
            Returns the integer y position.
        """
        return self._y_pos