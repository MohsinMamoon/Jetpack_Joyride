class Object():

    _shape = []
    _pos = {"x": -1, "y": -1}

    def __init__(self, x, y, board):
        self._pos["x"] = x
        self._pos["y"] = y
        board.place(self._shape, x, y)

    def move(self):
        pass

    def attack(self):
        pass

    def print(self):
        for i in self._shape:
            for j in i:
                print(j, end="")
            print("")
