from textures import jety_left, jety_right, jety_sheild
from person import Person
from board import PLAYERS


class Jety(Person):

    __shapes = [jety_left, jety_right, jety_sheild]
    _time = 180
    _score = 0
    _sheild_time = 10
    _sheild_timeout = 0
    _powerup_time = 10
    _gravity = 1

    @property
    def name(self):
        return "jety"

    def __init__(self, x, y, board):
        self._state = "right"
        self._shape = self.__shapes[1]
        super().__init__(x, y, board)
        self._size = [3, 4]
        PLAYERS.append(self)

    def tick(self):
        self._time -= 1
        if self._time == 0:
            print("GAME OVER: \nYOU RAN OUT OF TIME\n")
            quit()
        if self._powerup_time > 0:
            self._powerup_time -= 1
            if self._powerup_time == 0:
                self._speed = 1

        if self._sheild_timeout > 0:
            self._sheild_timeout -= 1

        if self._state == "sheild":
            if self._sheild_time > 0:
                self._sheild_time -= 1
            if self._sheild_time == 0:
                self._sheild_time = 10
                self.ch_state("right", 1)
                self._sheild_timeout = 60

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
        self._score = self._score + add

    def ch_state(self, state="", sh_off=0):
        if state in ["left", "sheild", "right"] and\
           (self._state != "sheild" or sh_off):
            if state == "left":
                self._shape = self.__shapes[0]
            elif state == "right":
                self._shape = self.__shapes[1]
            elif state == "sheild":
                if self._sheild_timeout == 0:
                    self._sheild_time = 10
                    self._shape = self.__shapes[2]
                else:
                    return
            self._state = state
        elif state == "":
            return self._state

    def gravity(self, status=""):
        if status == "":
            return self._gravity
        else:
            self._gravity = status
            self.grav_const('reset')

    def powerup(self):
        self._powerup_time = 10
        self._speed = 6

    def stats(self):
        return self._time, self._score, self._lives, self._sheild_timeout, self._sheild_time, self._powerup_time
