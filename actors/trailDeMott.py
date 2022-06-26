from actors.trail_pieceDeMott import *

INITIAL_TRAIL_SIZE = 5

class Trail():
    def __init__(self) -> None:
        self._trail = []
        self._trail_size = INITIAL_TRAIL_SIZE

    def get_trail(self):
        """
            Returns the list of Trail Pieces.
        """
        return self._trail

    def create_tail(self):
        """
            Create the initial trail, of size self._trail_size
        """
        for trail_piece in range(self._trail_size):
            self.add_trail()

    def add_trail(self):
        """
            Adds a new Trail Piece to the Player/Cycle.
        """
        # Finds the Trail_Piece that is ahead of it
        # The Trail_Piece_Index will be the length of the list before it is added.
        ahead = self.get_trail_ahead(len(self._trail))

        # Create a new Point based on the ahead's position Point.
        new_position = Point(self._max_x, self._max_y, ahead._position.get_x(), ahead._position.get_y())
        
        # Adjust the position to be one font_size space behind (opposite of velocity)
        new_position.add_velocity(((ahead._velocity[0]) * -1) * (self._font_size), ((ahead._velocity[1]) * -1) * (self._font_size))

        # Create the new Trail Piece and add it to the end of the Trail.
        self._trail.append(Trail_Piece(self._max_x, self._max_y, self._font_size, new_position, ahead.get_velocity(), self._base_color.to_text()))

    def get_trail_ahead(self, piece_index):
        """
            Returns the Collision Actor that is ahead of the Trail_Piece 
             given the piece_index position in the self._trail list.
        """
         # The piece ahead of the new Trail Piece
        ahead = None
        if piece_index == 0:
            # The first Trail Piece follows the Player.
            ahead = None
        else:             
            # Follow the Trail Piece at the end of the Trail.
            # If _trail[1], ahead is trail[0]
            # If _trail[n], ahead is trail[n - 1]
            ahead = self._trail[piece_index - 1]
        return ahead
