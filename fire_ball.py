from bullet import Bullet
from colorama import Fore


class Fire(Bullet):

    __shapes = [[[Fore.MAGENTA + '=', Fore.MAGENTA + '}']], [[Fore.MAGENTA + '{', Fore.MAGENTA + '=']]]

    def __init__(self, x, y, direct, board):

        if direct == "left":
            self._state = "left"
            self._shape = self.__shapes[1]
        else:
            self._state = "right"
            self._shape = self.__shapes[0]
        super().__init__(x, y, board)

    @property
    def name(self):
        return "fireball"
