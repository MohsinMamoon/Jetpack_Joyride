from textures import firebeam_hor as hor,\
                     firebeam_vert as vert,\
                     firebram_slant_right as slant_right,\
                     firebram_slant_left as slant_left
from object import Object
from board import FIREBEAMS


class Firebeam(Object):

    __shapes = [hor, vert, slant_right, slant_left]

    def __init__(self, x, y, typ, board):
        self._pos = {"x": x, "y": y}
        if typ == "horizontal":
            self._shape = self.__shapes[0]
            self._size = [1, 6]
        elif typ == "vertical":
            self._shape = self.__shapes[1]
            self._size = [4, 1]
        elif typ == "slant_right":
            self._shape = self.__shapes[2]
            self._size = [4, 4]
        elif typ == "slant_left":
            self._shape = self.__shapes[3]
            self._size = [4, 4]
        super().__init__(x, y, board)
        self.add_symbols("firebeam")
        FIREBEAMS.append(self)

    def check_collision(self, board, x, y, is_sheild):
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
                        if is_sheild:
                            board.remove(self._shape, self._pos['x'], self._pos['y'])
