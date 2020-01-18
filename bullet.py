from object import Object
from board import BULLETS


class Bullet(Object):

    _state = "left"

    def __init__(self, x, y, board):
        self._pos = {"x": x, "y": y}
        super().__init__(x, y, board)
        self._size = [1, 2]
        self.add_symbols(self.name)
        BULLETS.append(self)

    @property
    def state(self):
        return self._state
