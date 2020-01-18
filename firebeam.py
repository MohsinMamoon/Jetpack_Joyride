from textures import firebeam_hor as hor,\
                     firebeam_vert as vert,\
                     firebram_slant_right as slant_right,\
                     firebram_slant_left as slant_left
from object import Object
from board import FIREBEAMS
from random import random


class Firebeam(Object):

    __shapes = [hor, vert, slant_right, slant_left]

    def __init__(self, x, y, typ, board):
        self._pos = {"x": x, "y": y}
        self._shape = self.__shapes[typ]
        if typ == 0:
            # self._shape = self.__shapes[0]
            self._size = [1, 6]
        elif typ == 1:
            # self._shape = self.__shapes[1]
            self._size = [4, 1]
        elif typ == 2 or typ == 3:
            # self._shape = self.__shapes[2]
            self._size = [4, 4]
        # elif typ == 3:
        #     self._size = [4, 4]
        super().__init__(x, y, board)
        self.add_symbols("firebeam")
        FIREBEAMS.append(self)

    def check_collision(self, board, x, y):
        for i in range(self._pos['x'], self._pos['x'] + self._size[0]):
            for j in range(self._pos['y'], self._pos['y'] + self._size[1]):
                if self._shape == self.__shapes[2]:
                    go = (i-self._pos['x'] == j-self._pos['y'])
                elif self._shape == self.__shapes[3]:
                    go = ((i-self._pos['x']) + (j-self._pos['y']) == 3)
                else:
                    go = True

                if go:
                    if i == x and j == y:
                        self.die(board)


def place_firebeam(board):

    for i in range(board.get_size()[0]):
        for j in range(board.get_size()[1]):
            k = random() * 100
            if k < 0.1:
                s = random() * 100
                if s < 25:
                    if board.fits(hor, i, j):
                        Firebeam(i, j, 0, board)
                elif s >= 25 and s < 25 * 2:
                    if board.fits(slant_left, i, j):
                        Firebeam(i, j, 3, board)
                elif s >= 25 * 2 and s < 25 * 3:
                    if board.fits(slant_right, i, j):
                        Firebeam(i, j, 2, board)
                elif s >= 25 * 3 and s < 101:
                    if board.fits(vert, i, j):
                        Firebeam(i, j, 1, board)
