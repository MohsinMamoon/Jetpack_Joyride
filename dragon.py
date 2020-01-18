from textures import dragon
from board import DRAGONS
from person import Person
from movement import playermove


class Dragon(Person):

    def __init__(self, x, y, board):
        self._shape = dragon
        super().__init__(x, y, board)
        self._size = [9, 37]
        DRAGONS.append(self)

    @property
    def name(self):
        return "dragon"

    def follow(self, board, player):
        if player._pos['x'] > self._pos['x'] + 6:
            playermove(board, self, 'down')
        elif player._pos['x'] + 2 < self._pos['x'] + 6:
            playermove(board, self, 'w')
