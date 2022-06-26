from actors.collision_actorDeMott import *

class Trail_Piece(Collision_Actor):
    def __init__(self, max_x, max_y, font_size, position, velocity, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        self._spawn_point = position
        self._position = self._spawn_point
        self._velocity_prev = velocity
        self._velocity = velocity

        # TODO: Logic of Trail Piece following ahead
        # Goes the direction the ahead piece was? going

        # TESTING
        # Velocity adjusted by Player in move_trail Method
        # Velocity is still multiplied, but now stays on the grid.. weird

    def move(self, ahead):
        self._position = Point(self._max_x, self._max_y, ahead.get_x(), ahead.get_y())
        self.get_velocity()

        # Update the Actor's position
        self._position.add_velocity(self._velocity[0] * -1  * self._font_size, self._velocity[1] * -1  * self._font_size)
        
        # Update the hitbox's position.
        self.update_hitbox()

    def set_color(self, color):
        self._color = Color(color)