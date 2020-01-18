from textures import coins_hor as hor,\
                     coins_vert as vert,\
                     coins_square as square,\
                     coins_trap as trap,\
                     coins_slant_right as slant_right,\
                     coins_slant_left as slant_left
from object import Object
from random import random


class Coins(Object):

    __shapes = [hor, square, trap, slant_left, slant_right, vert]

    def __init__(self, x, y, typ, board):
        self._pos = {"x": x, "y": y}
        self._shape = self.__shapes[typ]
        self._size = [1, 1]
        super().__init__(x, y, board)
        self.add_symbols("coin")


def place_coins(board):

    for i in range(board.get_size()[0]):
        for j in range(board.get_size()[1]):
            k = random() * 100
            if k < 0.25:
                s = random() * 100
                if s < 16.666:
                    if board.fits(hor, i, j):
                        Coins(i, j, 0, board)
                elif s >= 16.66 and s < 16.66 * 2:
                    if board.fits(square, i, j):
                        Coins(i, j, 1, board)
                elif s >= 16.66 * 2 and s < 16.66 * 3:
                    if board.fits(trap, i, j):
                        Coins(i, j, 2, board)
                elif s >= 16.66 * 3 and s < 16.66 * 4:
                    if board.fits(slant_left, i, j):
                        Coins(i, j, 3, board)
                elif s >= 16.66 * 4 and s < 16.66 * 5:
                    if board.fits(slant_right, i, j):
                        Coins(i, j, 4, board)
                elif s >= 16.66 * 5 and s < 101:
                    if board.fits(vert, i, j):
                        Coins(i, j, 5, board)
