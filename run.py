import os

from board import Board
from jety import Jety
from time import sleep, time
from firebeam import place_firebeam
from magnet import place_magnet
from coin import place_coins
from powerup import place_powerup
from dragon import Dragon
from movement import playermove, boardmove, bulletmove
from board import MAGNETS, BULLETS, DRAGONS, TIME, TIMEOUT
from random import random
from colorama import Back

input("\n\nControls:\n\t'w': Up\n\t'a': Left\n\t'd': Right\n\t'b': Shoot\n\t'space': Sheild\n\t'q': Quit\n\n\n\n\t\t\t\t\tPress ENTER to start: " + Back.LIGHTBLUE_EX)
os.system('cls' if os.name == 'nt' else 'clear')


brd = Board(28, 300)
player = Jety(23, 9, brd)
dragon = Dragon(10, 260, brd)


brd.print_board(120, 0, 3, -1, 0, 5, 0)

place_firebeam(brd)
place_magnet(brd)
place_powerup(brd)
place_coins(brd)

sleep(1)


def printing():

    stats = player.stats()
    drag_lives = -1

    brd_bnds = brd.get_bounds()
    if 260 in range(brd_bnds[0], brd_bnds[1]):
        drag_lives = dragon._lives

    brd.print_board(stats[0], stats[1], stats[2], drag_lives, stats[3], stats[4], stats[5])


def moving():

    for j in BULLETS:
        bulletmove(brd, player, j)
    for i in DRAGONS:
        i.follow(brd, player)
    playermove(brd, player)

    if 260 in range(brd.get_bounds()[0], brd.get_bounds()[1]):
        TIMEOUT["Attack"] = 1

    if time() - TIME["Speed"] >= TIMEOUT["Speed"]:
        boardmove(brd, player)
        TIME["Speed"] = time()


def magnet_action():

    if time() - TIME['Magnet'] >= TIMEOUT["Magnet"]:
        for i in MAGNETS:
            i.attract(brd, player)
        TIME['Magnet'] = time()


def clock():

    if time() - TIME['Time'] >= TIMEOUT["Time"]:
        player.tick()
        TIME['Time'] = time()


def gravity():

    if player.gravity():
        if time() - TIME['Gravity_jety'] >= TIMEOUT['Gravity_jety']:
            playermove(brd, player, "down")
            TIME['Gravity_jety'] = time()
    else:
        player.gravity(1)

    if time() - TIME['Gravity_bullets'] >= TIMEOUT["Gravity_bullets"]:
        for i in BULLETS:
            bulletmove(brd, player, i, 1)
        TIME['Gravity_bullets'] = time()


def drag_attack():

    if time() - TIME['Attack'] >= random() + TIMEOUT["Attack"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in DRAGONS:
            i.attack(brd)
        TIME['Attack'] = time()


while 1:

    printing()

    moving()

    magnet_action()

    clock()

    gravity()

    drag_attack()
