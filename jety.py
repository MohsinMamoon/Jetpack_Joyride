from textures import jety_left, jety_right, jety_sheild
from object import Object


class Jety(Object):

    __shapes = [jety_left, jety_right, jety_sheild]
    __state = "right"
    __lives = 3
    __time = 120
    __score = 0

    def __init__(self, x, y, board):
        self._shape = self.__shapes[1]
        super().__init__(x, y, board)
        self._size = (3, 4)

    def move(self, x, y, board):
        board.remove(self._shape, self._pos['x'], self._pos['y'])
        board.place(self._shape, x, y)
        self._pos = {"x": x, "y": y}

    def attack(self):
        print("attacking")

    def die(self):
        self.__lives = self.__lives - 1

    def inc_score(self, item="none"):
        add = 0
        if item == "none":
            add = 5
        elif item == "firebeam":
            add = 10
        elif item == "magnet":
            add = 15
        elif item == "coin":
            add = 20
        elif item == "dragon":
            add = 100
        self.__score = self.__score + add

    def tick(self):
        self.__time = self.__time - 1

    def ch_state(self, state):
        if state in ["left", "sheild", "right"]:
            self.__state = state
            if self.__state == "left":
                self._shape = self.__shapes[0]
            elif self.__state == "right":
                self._shape = self.__shapes[1]
            elif self.__state == "sheild":
                self._shape = self.__shapes[2]
            

    def print_stats(self):
        print("\033[u", end="")
        print("Time: " + str(self.__time) + "s\t\t\t\t\t\t\t\t Score: " + str(self.__score) + "\n"\
              + "\t\t\t\t\t Lives: " + str(self.__lives) + "\n")
