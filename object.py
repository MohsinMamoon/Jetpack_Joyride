from board import symbs
from board import FIREBEAMS, MAGNETS, DRAGONS, PLAYERS, BULLETS, POWERUPS


class Object():

    _shape = []
    _pos = {"x": -1, "y": -1}
    _size = [0, 0]
    _grav_const = 1

    def grav_const(self, change=''):
        if change == '':
            return int(self._grav_const)
        elif change == 'reset':
            self._grav_const = 1
        else:
            self._grav_const += change

    def __init__(self, x, y, board):
        board.place(self._shape, x, y)

    def move(self, x, y, board):
        board.remove(self._shape, self._pos['x'], self._pos['y'])
        board.place(self._shape, x, y)
        self._pos = {"x": x, "y": y}

    def attack(self):
        pass

    def check_collision(self, board, x, y):
        for i in range(self._pos["x"], self._pos["x"] + self._size[0]):
            for j in range(self._pos['y'], self._pos['y'] + self._size[1]):
                if i == x and j == y:
                    self.die(board)

    def die(self, board):
        board.remove(self._shape, self._pos['x'], self._pos['y'])
        self.del_from_board()

    def get_pos(self):
        return [self._pos['x'], self._pos['y']]

    def get_size(self):
        return self._size

    def print(self):
        for i in self._shape:
            for j in i:
                print(j, end="")
            print("")

    def add_symbols(self, name):
        for i in self._shape:
            for j in i:
                if j != " ":
                    symbs[name].add(j)

    def del_from_board(self):
        for i in [FIREBEAMS, MAGNETS, BULLETS, DRAGONS, PLAYERS, POWERUPS]:
            try:
                i.remove(self)
            except:
                pass
