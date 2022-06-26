from actors.collision_actorDeMott import *
from actors.trail_pieceDeMott import Trail_Piece
from player_inputDeMott import Player_Input, pyray
from actors.scoreDeMott import Score

# Best speed I've found is Frame_Rate/Step_Size = 12
TRAIL_SIZE = 5

class Player(Collision_Actor):
    def __init__(self, max_x, max_y, font_size, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        # Reset Base Color, Color, and Symbol
        self._base_color = Color("BLUE")
        self._color = self._base_color
        self._symbol = "@"

        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input([pyray.KEY_W, pyray.KEY_A, pyray.KEY_S, pyray.KEY_D])

        # Player starts with an initial velocity of up.
        self._velocity = [0, -1]
        self._velocity_prev = self._velocity[:]

        # Overrite Spawn Point, Position
        self._spawn_point = Point(max_x, max_y, int(self._max_x * 1/3), self._max_y//2)
        self._position = self._spawn_point
        
        # Create a Score object
        self._score = Score(max_x, max_y, self._font_size, "Player One:")        
        self._score.move(int(self._max_x * 1/12), 0)
        
        # Initialize the Trail Piece list
        self._trail = []
        self._trail_size = TRAIL_SIZE

    def get_trail(self):
        """
            Returns the Player's list of Trail Pieces.
        """
        return self._trail

    def create_tail(self):
        """
            Create the initial trail, of size self._trail_size
        """
        for trail_piece in range(self._trail_size):
            self.add_trail()

    def get_trail_ahead(self, piece_index):
        """
            Returns the Collision Actor that is ahead of the Trail_Piece 
             given the piece_index position in the self._trail list.
        """
         # The piece ahead of the new Trail Piece
        ahead = None
        if piece_index == 0:
            # The first Trail Piece follows the Player.
            ahead = self
        else:             
            # Follow the Trail Piece at the end of the Trail.
            # If _trail[1], ahead is trail[0]
            # If _trail[n], ahead is trail[n - 1]
            ahead = self._trail[piece_index - 1]
        return ahead

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

    def move_trail(self):
        """
            Updates the position of each Trail Piece.
        """
        for trail_index in range(0, len(self._trail)):
            ahead = self.get_trail_ahead(trail_index)
            self._trail[trail_index].set_velocity(ahead.get_previous_velocity())
            self._trail[trail_index].move(ahead)
           
    def get_velocity(self):
        """
            Gets the current velocity of the Player. Relies on Player Input. 
            If Player Input is [0, 0], continues travelling in the previous direction.
        """
        self._velocity_prev = self._velocity[:]
        new_velocity = self._player_input.get_direction()
        
        # If there has been user input to change the direction,
        if not (new_velocity == [0, 0]):
            # Update the player to move the direction the user has specified.
            self._velocity = new_velocity
        return self._velocity

    def move(self):
        """
            Moves the Player based on keyboard input, loops to other side of the screen.
        """
        super().move()
        
        # Update the positions of the Trail Pieces.
        self.move_trail()

    def get_score(self):
        """
            Returns the Player's Score object.
        """
        return self._score

    def set_color(self, color):
        """
            Sets the color of the Player and the Trail Pieces.
        """
        self._color = Color(color)
        for trail_piece in self._trail:
            trail_piece.set_color(color)

class Player2(Player):
    def __init__(self, max_x, max_y, font_size, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        # Overrite the Base Color, Color
        self._base_color = Color("GREEN")
        self._color = self._base_color
        
        # Overrite the Player_Input (different Keyset than Player)
        self._player_input = Player_Input([pyray.KEY_I, pyray.KEY_J, pyray.KEY_K, pyray.KEY_L])
        
        # Overrite the Spawn Point, Position
        self._spawn_point = Point(max_x, max_y, int(max_x * 2/3), max_y//2)
        self._position = self._spawn_point
        
        # Overrite the Score and its Position
        self._score = Score(max_x, max_y, self._font_size, "Player Two:")   
        self._score.move(int(max_x * 7/12), 0)
