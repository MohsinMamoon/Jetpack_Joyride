from bullet import Bullet
from colorama import Fore


class Ice(Bullet):

    def __init__(self, x, y, board):
        self._shape = [[Fore.MAGENTA + chr(162), Fore.MAGENTA + '~']]
        super().__init__(x, y, board)

    @property
    def name(self):
        return "iceball"
