from Actors.point import Point
import pyray

class Color():
    """
        The Color class, decides what color objects are displayed in on the Window.
    """
    def __init__(self):
        self._COLORS = {"WHITE": pyray.RAYWHITE, "RED": pyray.RED}
        self._color = pyray.RAYWHITE
        #self._COLORS["WHITE"]

    def set_color(self, color_str):
        self._color = pyray.RAYWHITE
        #self._COLORS[color_str]

    def get_color(self):
        return self._color

class Actor():
    def __init__(self, max_x, max_y, font_size, color = pyray.RAYWHITE):
        self._max_x = max_x
        self._max_y = max_y
        # TODO: some calculations for spawn point
        self._spawn_point = Point(max_x, max_y, 0, 0)
        self._position = self._spawn_point
        self._symbol = "#"
        self._font_size = font_size
        self._color = pyray.RAYWHITE
        #Color()
        #self._color.set_color("WHITE")

    def get_velocity(self):
        """
            TODO: Implement. Doesn't do anything right now
        """
        pass

    def move(self):
        """
            TODO: Implement. Doesn't do anything right now
        """
        #self._position.set_position(self._position.get_x(), self._position.get_y())
        pass
        
    def get_x(self):
        """
            Returns the X position of the Actor.
        """
        return self._position.get_x()

    def get_y(self):
        """
            Returns the Y position of the Actor.
        """
        return self._position.get_y()

    def get_direction(self):
        """
            Returns the direction the Actor is going.
        """
        return self._direction

    def get_symbol(self):
        """
            Returns the symbol that is used to display the Actor.
        """
        return self._symbol

    def get_font_size(self):
        """
            Returns the font size of the Actor.
        """
        return self._font_size

    def get_color(self):
        """
            Returns the pyray color of the Actor.
        """
        return self._color
        #return self._color.get_color()