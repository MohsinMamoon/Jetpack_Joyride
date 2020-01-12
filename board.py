from time import sleep
from textures import cloud, broken_wall
import os

columns = min(200, int(os.popen("stty size", 'r').read().split()[1]))


class Board():

    def __init__(self, x, y):
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
        self.print_board(0)
        sleep(2)
        self.place(broken_wall, x-7, 0)
        self._position = 0

    def print_board(self, start):
        for i in self.__grid:
            for j in range(start, start + columns):
                print(i[j], end="")
            print("")

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
