from Actors.player_input import Player_Input
from Actors.actor import Actor, Color
from Actors.point import Point
from Actors.message import Score
import pyray

class Cycle(Actor):
    def __init__(self, max_x, max_y, font_size):
        super().__init__(max_x, max_y, font_size)
        self._spawn_point = Point(max_x, max_y, max_x//3, max_y//2)
        self._position = self._spawn_point
        self._direction = [-1, 0]
        self._player_input = Player_Input([pyray.KEY_W, pyray.KEY_A, pyray.KEY_S, pyray.KEY_D])
        self._step_size = 25
        self._score = Score(max_x, max_y, font_size, "RED")
        self._score.set_position(0 + font_size, 0 + font_size)
        self._color = pyray.BLUE

    def get_direction(self):
        """
            Checks the keyboard for if the user has changed the Snake's direction.
            Will only allow the Snake to travel in the X or Y position, not both.
        """
        # Update the x/y direction.
        # The keyboard will only returns 1 non-zero direction.
        #new_direction
        self._direction = self._player_input.get_direction()

        #if not (new_direction[0] == 0 and new_direction[1] == 0):
        #    self._direction = new_direction

        # For debugging, display this to GUI
        return self._direction

    def move(self):
        """
            Moves the Player based on keyboard input, loops to other side of the screen.
        """
        # Checks if the direction has changed.
        self.get_direction()
        
        self._position.add_velocity(self._direction[0]  * self._step_size, self._direction[1]  * self._step_size)

    def get_score(self):
        return self._score

class Cycle2(Cycle):
    def __init__(self, max_x, max_y, font_size):
        # Call the Actor constructor
        super().__init__(max_x, max_y, font_size)
        self._spawn_point = Point(max_x, max_y, max_x - max_x//3, max_y//2)
        self._position = self._spawn_point
        self._direction = [-1, 0]
        self._step_size = 25
        self._player_input = Player_Input([pyray.KEY_I, pyray.KEY_J, pyray.KEY_K, pyray.KEY_L])
        self._score = Score(max_x, max_y, font_size, "RED")
        self._score.set_position(max_x//2 + font_size, 0 + font_size)
        self._color = pyray.GREEN

class Trail(Actor):
    def __init__(self, x_pos, y_pos, font_size, color, player, ahead):
        super().__init__(x_pos, y_pos, font_size, color)
        self._Player = player
        self._ahead = ahead

    def move(self):
        """
            Will follow the Player
        """
        pass