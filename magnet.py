from textures import magnet
from object import Object
from board import MAGNETS
from movement import playermove


class Magnet(Object):

    def __init__(self, x, y, board):
        self._pos = {"x": x, "y": y}
        self._shape = magnet
        self._size = [3, 5]
        super().__init__(x, y, board)
        self.add_symbols("magnet")
        MAGNETS.append(self)

    def attract(self, board, player):
        pl_pos = player.get_pos()
        pl_size = player.get_size()
        if pl_pos[1] + pl_size[1] - 1 in\
           range(self._pos['y'] - 10, self._pos['y'] + self._size[1] + 10) or\
           pl_pos[1] in\
           range(self._pos['y'] - 10, self._pos['y'] + self._size[1] + 10):

            if pl_pos[1] + pl_size[1] <= self._pos["y"]:
                playermove(board, player, 'd')
            if self._pos["y"] + self._size[1] <= pl_pos[1]:
                playermove(board, player, 'a')

            if pl_pos[0] + pl_size[0] - 1 in\
               range(self._pos['x'] - 10, self._pos['x'] + self._size[0] + 10)\
               or pl_pos[0] in\
               range(self._pos['x'] - 10, self._pos['x'] + self._size[0] + 10):
                if pl_pos[0] + pl_size[0] <= self._pos['x']:
                    playermove(board, player, 'down')
                if self._pos["x"] + self._size[0] <= pl_pos[0]:
                    playermove(board, player, 'w')
