from Actors.actor import Actor, pyray

class Message(Actor):
        def __init__(self, max_x, max_y, font_size, color):
            super().__init__(max_x, max_y, font_size, color)
            self._symbol = "This is the message"
            self._color = color

        def set_message(self, message):
            self._symbol = message

        def get_message(self):
            return self._symbol

class Score(Actor):
    def __init__(self, max_x, max_y, font_size, color):
        super().__init__(max_x, max_y, font_size, color)
        self._score = 0
        self._symbol = "Score: "

    def set_position(self, pos_x, pos_y):
        self._position.set_position(pos_x, pos_y)

    def get_score(self):
        return self._score

    def add_score(self, points):
        self._score += points

    def get_message(self):
        return f"{self._symbol}{self._score}"
