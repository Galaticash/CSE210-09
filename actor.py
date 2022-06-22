# from [COLOR] import Color, pyray <-- import only once?
# from [POINT] import Point
import pyray

class Actor():
    """
        An object that can be displayed on the GUI.
        Given the maximum bounds of the screen, the font size, and color of itself. 
        Has a Point position on the screen
        Has a symbol to represent itself with, can be a single character or a string of them (Message).
        Has Getters for each Attribute so the GUI can properly display the Actor.
    """
    def __init__(self, max_x, max_y, font_size, color = pyray.RAYWHITE):
        self._max_x = max_x
        self._max_y = max_y
        # TODO: some calculations for spawn point
        # self._spawn_point = [import Point] Point(max_x, max_y, 0, 0) <-- give max_x/max_y for loop over, then x/y position to set OR use a method test_point.set_position(x, y)
        self._position = self._spawn_point # Could replay the game and set the actor back to the start
        self._velocity = [0, 0] # The X and Y velocity
        self._symbol = "#"
        self._font_size = font_size
        self._color = pyray.RAYWHITE
        #Color()
        #self._color.set_color("WHITE")

    def move(self):
        """
            Moves the Actor. Doesn't do anything right now
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

    def get_velocity(self):
        """
            Gets the current dx/dy of the Actor. Doesn't do anything right now
        """
        # return self._velocity --> could also split into get_velocity_x/y if that works better?
        return self._velocity
 
    def get_display(self):
        """
            Returns the character or string that is used to display the Actor.
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
        #return self._color.get_color() <-- get pyray Color/rbg color directly from Color class