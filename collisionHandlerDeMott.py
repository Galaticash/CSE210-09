class Collision_Handler():
    def __init__(self, cast):
        self._cast = cast
        self._players = self._cast.get_players()
    
    def update_colliders(self):
        self._colliders = self._cast.get_players()

    def check_head_collision(self, player):
        """
            Checks if the Player's head has collided with the other Player.
        """
        # Check that there are two Players.
        assert(len(self._colliders) == 2)
        player_two = self._players[1]
        if player == self._players[1]:
            player_two = self._players[0]
        
        # Check if there has been a head to head collision.
        if player.is_hit(player_two):
            return True

        # Check if the player has hit a tail_piece of the other player
        for tail_piece in player_two.get_trail():
            if player.is_hit(tail_piece):
                return True

    def check(self):
        self.update_colliders()
        
        # TODO: More dynamically check collisions, check only close ones? Check each one against each other collider (VERY inefficient)?
        # TODO: Different return values to tell Director which Player won/lost

        # Checks if the Player heads have collided with anything.
        if self.check_head_collision(self._players[0]): 
            # Set each Player's color to White
            for player in self._players:
                player.set_color("WHITE")
            return True
        elif self.check_head_collision(self._players[1]):
            # Set each Player's color to White
            for player in self._players:
                player.set_color("WHITE")
            return True
        else:
            # Color doesn't need to be reset, game_over when there is a collision.
            #for player in self._players:
            #    player.reset_color()
            return False
        
        # A more generalized Collision Handler
        # # TODO: More effectivley handle color reset, only reset the color if /was/ hit but currently not hit
        #   colliders_one = self._colliders
        #   colliders_two = self._colliders [1: -1]
        # for collider_one in colliders_one:
        #     # Check every collider in list one against those in list two, 
        #     # removing items from two if they are the same (no comparison needed)
        #     for collider_two in colliders_two:
        #         #if collider_one == colliders_two:
        #         #    colliders_two.pop(collider_two)
        #         #else:
        #         colliders = [collider_one, collider_two]
        #         if collider_one.is_hit(collider_two):
        #             # Indicate there has been a collision.
        #             for collider in colliders:
        #                 collider.set_color("RED")
        #             return True
        #         else:
        #             for collider in colliders:
        #               # Check for only those with was_hit == True?
        #                 collider.reset_color()
        #             return False