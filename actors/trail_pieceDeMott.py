from actors.collision_actorDeMott import *

class Trail_Piece(Collision_Actor):
    def __init__(self, max_x, max_y, font_size, position, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        self._spawn_point = position
        self._position = self._spawn_point

        # TODO: Fix the spacing of Trail Pieces


        # TODO: Logic of Trail Piece following ahead
        # Goes the direction the ahead piece was? going

        # TESTING
        # Velocity adjusted by Player in move_trail Method
        # Velocity is still multiplied, but now stays on the grid.. weird