class Hitbox():
    def __init__(self, width, radius):
        self._hitbox = {"Top": 0, "Bottom": 0, "Right": 0, "Left": 0}
        self._radius = radius
        self._width = width
    
    def update(self, position):
        """
            Updates the Actor's hitbox according to the new position Point.
        """
        # self._position is the center Point, at the middle left of the object
        self._hitbox["Top"] = position.get_y() - self._radius
        self._hitbox["Bottom"] = position.get_y() + self._radius
        self._hitbox["Left"] = position.get_x() - self._radius
        # The right side of the hitbox must be adjusted to the length of the symbol
        self._hitbox["Right"] = position.get_x() + (self._radius * self._width)

    def is_hit(self, other_collider_pos):
        """
            Will check if the other Actor's Point position is within this Hitbox, and return if there has been a collison.
        """
        # Okay. so this is getting called ALL the time
        if other_collider_pos.get_y() >= self._hitbox["Top"]:
            if other_collider_pos.get_y() <= self._hitbox["Bottom"]:
                if other_collider_pos.get_x() >= self._hitbox["Left"]:
                    if other_collider_pos.get_x() <= self._hitbox["Right"]:
                        return True
        else:
           return False

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def top(self):
        return self._hitbox["Top"]

    @top.setter
    def top(self, top_limit):
        self._hitbox["Top"] = top_limit
        self._width = 1

    @property
    def bottom(self):
        return self._hitbox["Bottom"]

    @bottom.setter
    def bottom(self, bottom_limit):
        self._hitbox["Bottom"] = bottom_limit
    
    @property
    def right(self):
        return self._hitbox["Right"]

    @right.setter
    def right(self, right_limit):
        self._hitbox["Right"] = right_limit

    @property
    def left(self):
        return self._hitbox["Left"]

    @left.setter
    def set_left(self, left_limit):
        self._hitbox["Left"] = left_limit