from actors.collision_actorDeMott import *

class Trail_Piece(Collision_Actor):
    """
        A single piece of the Player's Trail that can be collided with.
    """
    def __init__(self, max_x, max_y, font_size, position, velocity, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        self._spawn_point = position
        self._position = self._spawn_point
        self._velocity_prev = velocity
        self._velocity = velocity

        # TODO: Logic of Trail Piece following ahead
        # Might just have to update previous velocity only after every step?

    def move(self, ahead):
        """
            Moves the Trail Piece based on the position of the item ahead of it.
        """
        self._position = Point(self._max_x, self._max_y, ahead.get_x(), ahead.get_y())
        self.get_velocity()

        # Update the Actor's position
        self._position.add_velocity(self._velocity[0] * -1  * self._font_size, self._velocity[1] * -1  * self._font_size)
        
        # Update the hitbox's position.
        self.update_hitbox()