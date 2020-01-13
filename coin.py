from textures import coins_hor as hor,\
                     coins_vert as vert,\
                     coins_square as square,\
                     coins_trap as trap,\
                     coins_slant_right as slant_right,\
                     coins_slant_left as slant_left
from object import Object


class Coins(Object):

    __shapes = [hor, square, trap, slant_left, slant_right, vert]

    def __init__(self, x, y, typ, board):
        self._pos = {"x": x, "y": y}
        self._shape = self.__shapes[typ]
        self._size = [1, 1]
        super().__init__(x, y, board)
        self.add_symbols("coin")
