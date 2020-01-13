from time import sleep
from textures import cloud, broken_wall
from object import symbs 
import os

columns = int(os.popen("stty size", 'r').read().split()[1])

FIREBEAMS = []
COINS = []
MAGNETS = []


class Board():

    def __init__(self, x, y):
        self.__size = [x, y]
        self.__start = 0
        self.__grid = [[' ' for i in range(y)] for j in range(x)]
        # making the ground and sky:
        j = 0
        for i in range(y):
            self.__grid[x-1][i] = '%'
            self.__grid[x-2][i] = '%'
            self.__grid[0][i] = '~'
            if i > 1:
                self.__grid[1][i] = cloud[0][j]
                j = (j+1) % 9
        # making boundaries:
        for i in range(x):
            for j in [0, 1, y-1, y-2]:
                self.__grid[i][j] = '|'
        # print("\033[s")
        self.print_board()
        sleep(2)
        self.place(broken_wall, x-7, 0)
        self._position = 0

    def print_board(self):
        for i in self.__grid:
            for j in range(self.__start, min(self.__size[1], self.__start + columns)):
                print(i[j], end="")
            print("")

    def get_bounds(self):
        return [self.__start, min(self.__size[1], self.__start + columns)]

    def get_size(self):
        return self.__size

    def update_range(self, change):
        new_start = self.__start + change
        new_start = max(0, new_start)
        if new_start + columns > self.__size[1]:
            new_start = self.__size[1] - columns
        # print("Updating range to: ", new_start)
        self.__start = new_start

    def place(self, item, x, y):
        __x = x
        __y = y
        for i in item:
            for j in i:
                self.__grid[__x][__y] = j
                __y = __y + 1
            __x = __x + 1
            __y = y

    def remove(self, item, x, y):
        __x = x
        __y = y
        for i in item:
            for j in i:
                self.__grid[__x][__y] = ' '
                __y = __y + 1
            __x = __x + 1
            __y = y

    def check_collision(self, size, position, direct, is_sheild):

        num = 0
        obj = "none"
        start = 0
        end = 0
        constant = 0

        if direct == "none":
            return obj, num

        elif direct == "up":
            # print("Collision from up", end = " ")
            start = position[1]
            end = position[1] + size[1]
            constant = position[0]

        elif direct == "down":
            # print("Collision from down", end = " ")
            start = position[1]
            end = position[1] + size[1]
            constant = position[0] + size[0] - 1

        elif direct == "right":
            # print("Collision from right", end = " ")
            start = position[0]
            end = position[0] + size[0]
            constant = position[1] + size[1] - 1

        elif direct == "left":
            # print("Collision from left", end = " ")
            start = position[0]
            end = position[0] + size[0]
            constant = position[1]

        for i in range(start, end):
            j = i
            if direct == "left" or direct == "right":
                i = constant
                constant = j
            if self.__grid[constant][i] in symbs["coin"]:
                obj = "coin"
                num = num + 1
            elif self.__grid[constant][i] in symbs["firebeam"]:
                obj = "firebeam"
                for j in FIREBEAMS:
                    j.check_collision(self, constant, i, is_sheild)
                num = is_sheild
                break
            # elif self.__grid[constant][i] in symbs["dragon"]:
            #     obj = "dragon"
            #     num = is_sheild
            #     break
            elif self.__grid[constant][i] in symbs["magnet"]:
                obj = "magnet"
                for j in MAGNETS:
                    j.check_collision(self, constant, i, is_sheild)
            if direct == "left" or direct == "right":
                constant = i
                i = j
        # print("with " + str(num) + " " + str(obj))
        return obj, num
