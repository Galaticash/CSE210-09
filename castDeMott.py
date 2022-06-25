class Cast():
    """
        A collection of Actors and Messages to display on the GUI.
    """
    def __init__(self):
        self._players = []
        self._messages = []

    def add_player(self, new_player):
        """
            Adds a new player to the Cast's list of Players.
        """
        new_player.create_tail()
        self._players.append(new_player)
        self.add_message(new_player.get_score())

    def get_players(self):
        """
            Returns the list of Players.
        """
        return self._players

    def add_message(self, new_message):
        """
            Adds a new message to the Cast's list of Messages.
        """
        self._messages.append(new_message)

    def get_messages(self):
        """
            Returns the list of Messages.
        """
        return self._messages

    def move(self):
        """
            Moves the Players.
        """
        for player in self._players:
            player.move()