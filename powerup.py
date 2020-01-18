from object import Object
from board import POWERUPS
from random import random
from colorama import Fore


class Powerup(Object):

    def __init__(self, x, y, board):
        self._pos = {'x': x, 'y': y}
        self._shape = [[Fore.GREEN + chr(187) for i in range(2)] for j in range(2)]
        self._size = [2, 2]
        super().__init__(x, y, board)
        self.add_symbols("po_up")
        POWERUPS.append(self)


def place_powerup(board):

    for i in range(board.get_size()[0]):
        for j in range(board.get_size()[1]):
            k = random() * 100
            if k < 0.05:
                if board.fits([[' ', ' '], [' ', ' ']], i, j):
                    Powerup(i, j, board)
