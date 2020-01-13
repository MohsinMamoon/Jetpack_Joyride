from textures import dragon
from object import Object


class Dragon(Object):

    def __init__(self, x, y, board):
        self._pos = {"x": x, "y": y}
        self._shape = dragon
        super().__init__(x, y, board)
        self._size = [9, 37]
        self.add_symbols("dragon")

    def attack(self):
        print("attacking")

    def die(self, board):
        board.remove(self._shape, self._pos["x"], self._pos["y"])
        print("Game Over: \nYOU WIN!\n")
