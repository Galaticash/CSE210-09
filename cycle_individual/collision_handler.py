from Actors.cycle import Cycle, Cycle2

# TODO: Move Cast
class Cast():
    def __init__(self):
        self._players = []
        self._messages = {}

    def add_player(self, actor_attributes, num = 1):
        new_actor = None
        if num == 2:
            # Set up the Cycle as player 2
            new_actor = Cycle2(actor_attributes[0], actor_attributes[1], actor_attributes[2])
        else:
            # Set up the Cycle as player 1
            new_actor = Cycle(actor_attributes[0], actor_attributes[1], actor_attributes[2])
        self.add_messages(f"Score{num}", new_actor.get_score())
        self._players.append(new_actor)

    def get_players(self):
        return self._players

    def add_messages(self, name, message):
        self._messages[name] = message

    def update_message(self, name, message):
        self._messages[name].set_message(message)

    def get_messages(self):
        return self._messages

    def move(self):
        for actor in self._players:
            actor.move()

class Collision_Handler():
    def __init__(self):
        pass

    def check(self):
        """
            Check yourself before you wreck yourself.
        """
        pass