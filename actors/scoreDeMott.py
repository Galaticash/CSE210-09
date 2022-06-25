from actors.messageDeMott import Message
from color import Color

class Score(Message):
    def __init__(self, max_x, max_y, font_size, message, color="WHITE"):
        super().__init__(max_x, max_y, font_size, message, color)
        self._color = Color("WHITE")
        self._score = 0

    def add_points(self, points):
        self._score += points

    def get_score(self):
        return self._score

    def get_display(self):
        return f"{self._message} {self._score}"