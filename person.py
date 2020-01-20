from object import Object
from time import sleep
from fire_ball import Fire
from ice_ball import Ice
from textures import door


class Person(Object):

    _state = "left"
    _lives = 3
    _speed = 1

    @property
    def speed(self):
        return self._speed

    def __init__(self, x, y, board):
        self._pos = {"x": x, "y": y}
        super().__init__(x, y, board)
        self.add_symbols(self.name)

    def attack(self, board):
        if self.name == "jety":
            x = self._pos['x'] + 1
            if self._state == "left":
                y = self._pos['y'] - 2
            else:
                y = self._pos['y'] + 4
            Fire(x, y, self._state, board)
        elif self.name == "dragon":
            x = self._pos['x'] + 6
            y = self._pos['y'] - 2
            Ice(x, y, board)

    def die(self, board):
        self._lives -= 1
        if self._lives < 0:
            sleep(2)
            board.remove(self._shape, self._pos['x'], self._pos['y'])
            if self.name == "jety":
                print("GAME OVER: \nYOU LOST ALL YOUR LIVES\n")
                quit()
            elif self.name == "dragon":
                board.place(door, 5, board.get_size()[1] - 6)
                board.remove(self._shape, self._pos['x'], self._pos['y'])
                self.del_from_board()
        if self.name == "jety":
            sleep(1)
            self.move(23, 9, board)
            board.update_range(-board.get_size()[1])
