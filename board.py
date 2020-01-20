import os

from colorama import Back, Fore
from time import sleep, time
from textures import cloud, broken_wall

back = Back.LIGHTBLUE_EX
symbs = {
    'dragon': set(),
    'coin': set(),
    'magnet': set(),
    'firebeam': set(),
    "jety": set(['#']),
    "fireball": set(),
    "iceball": set(),
    "po_up": set()
}

columns = int(os.popen("stty size", 'r').read().split()[1])
if columns < 31:
    print("\n\n\t\t\tError: The game could not launch!\n\t\t\tPlease resize your terminal window\n\n\n")
    quit()

FIREBEAMS = []
MAGNETS = []
DRAGONS = []
PLAYERS = []
BULLETS = []
POWERUPS = []


TIMEOUT = {
    "Time": 1,
    "Speed": 0.2,
    "Gravity_jety": 0.005,
    "Gravity_bullets": 0.5,
    "Magnet": 0.05,
    "Attack": 5,
    "Reset_screen": 5
}

TIME = {}
for i in TIMEOUT.keys():
    TIME[i] = time()


class Board():

    def __init__(self, x, y):
        self.__size = [x, y]
        self.__start = 0
        self.__grid = [[' ' for i in range(y)] for j in range(x + 10)]
        # making the ground and sky:
        j = 0
        for i in range(y):
            self.__grid[x-1][i] = Fore.RED + '%'
            self.__grid[x-2][i] = Fore.RED + '%'
            self.__grid[0][i] = Fore.LIGHTWHITE_EX + '~'
            if i > 1:
                self.__grid[1][i] = cloud[0][j]
                j = (j+1) % 9
        # making boundaries:
        for i in range(x):
            for j in [0, 1, y-1, y-2]:
                self.__grid[i][j] = Fore.RED + '|'

        print("\033[s")
        self.print_board(180, 0, 3, -1, 0, 10, 0)
        sleep(2)
        self.place(broken_wall, x-7, 0)
        self._position = 0

    def print_board(self, time, score, lives, drag_lives, s_timeout, s_time, p_time):

        print("\033[u")
        x = self.__size[0]
        y = self.__start
        top = Fore.BLACK + "Time: %3ds" % (time)
        bottom = Fore.BLACK + "Lives: %2s" % (lives)

        if columns - 25 < 20:
            for i in range(columns - 25):
                top += ' '
                bottom += ' '
        else:
            for i in range(int((columns - 45) / 2)):
                top += ' '
                bottom += ' '
            top += "   "

            if s_timeout > 0:
                top += Fore.LIGHTBLACK_EX + "Sheild: %3ds   " % (-s_timeout) + Fore.BLACK
            else:
                top += "Sheild: %3ds   " % (s_time)

            if p_time > 0:
                bottom += "   Powerup: %2d   " % (p_time)
            else:
                bottom += Fore.LIGHTBLACK_EX + "   Powerup:  0   " + Fore.BLACK

            for i in range(int((columns - 45) / 2)):
                top += ' '
                bottom += ' '

        top += "Score: %4d" % (score)

        if drag_lives >= 0:
            bottom += "Dragon Lives: %2d" % (drag_lives)
        else:
            bottom += Fore.LIGHTBLACK_EX + "Dragon Lives:  0" + Fore.BLACK

        self.__grid[x][y] = top
        self.__grid[x+1][y] = bottom

        for i in self.__grid:
            for j in range(self.__start, min(self.__size[1], self.__start + columns)):
                print(i[j], end="")
            print("")

    def fits(self, item, x, y):

        __x = x
        __y = y
        for i in item:
            for j in i:
                try:
                    if ((self.__grid[__x][__y] != ' ') or (__x < 2) or (__y >= 400) or (__x >= self.__size[0]-2)):
                        return 0
                except:
                    return 0
                __y += 1
            __x += 1
            __y = y
        return 1

    def get_bounds(self):
        return [self.__start, min(self.__size[1], self.__start + columns)]

    def get_size(self):
        return self.__size

    def update_range(self, change):
        new_start = self.__start + change
        new_start = max(0, new_start)
        if new_start + columns > self.__size[1]:
            new_start = self.__size[1] - columns

        x = self.__size[0]
        y = self.__start
        self.__grid[x][y] = ' '
        self.__grid[x+1][y] = ' '
        self.__start = new_start

    def place(self, item, x, y):
        __x = x
        __y = y
        for i in item:
            for j in i:
                self.__grid[__x][__y] = j
                __y += 1
            __x += 1
            __y = y

    def remove(self, item, x, y):
        __x = x
        __y = y
        for i in item:
            for j in i:
                self.__grid[__x][__y] = ' '
                __y += 1
            __x += 1
            __y = y

    def check_collision(self, size, position, direct, is_bullet):

        num = 0
        obj = "none"
        start = 0
        end = 0
        constant = 0

        if direct == "none":
            return obj, num

        elif direct == "up":
            start = position[1]
            end = position[1] + size[1]
            constant = position[0]

        elif direct == "down":
            start = position[1]
            end = position[1] + size[1]
            constant = position[0] + size[0] - 1

        elif direct == "right":
            start = position[0]
            end = position[0] + size[0]
            constant = position[1] + size[1] - 1

        elif direct == "left":
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
                if is_bullet == "fireball":
                    for j in FIREBEAMS:
                        j.check_collision(self, constant, i)
                break
            elif self.__grid[constant][i] in symbs["dragon"]:
                obj = "dragon"
                if is_bullet == "fireball":
                    for j in DRAGONS:
                        j.check_collision(self, constant, i)
                break
            elif self.__grid[constant][i] in symbs["magnet"]:
                obj = "magnet"
                if is_bullet == "fireball":
                    for j in MAGNETS:
                        j.check_collision(self, constant, i)
                    break
            elif self.__grid[constant][i] in symbs["fireball"]:
                obj = "fireball"
                for j in BULLETS:
                    j.check_collision(self, constant, i)
                break
            elif self.__grid[constant][i] in symbs["iceball"]:
                obj = "iceball"
                for j in BULLETS:
                    j.check_collision(self, constant, i)
                break
            elif self.__grid[constant][i] in symbs["po_up"]:
                obj = "po_up"
                for j in POWERUPS:
                    j.check_collision(self, constant, i)
                break
            elif self.__grid[constant][i] == '\x1b[31m=':
                obj = "door"
                break
            elif self.__grid[constant][i] in symbs["jety"]:
                if self.__grid[constant][i] != '#':
                    obj = "jety"
                    if is_bullet == "iceball":
                        for j in PLAYERS:
                            j.check_collision(self, constant, i)
                        break

            if direct == "left" or direct == "right":
                constant = i
                i = j
        return obj, num
