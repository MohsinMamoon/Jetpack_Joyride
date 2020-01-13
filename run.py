from board import Board
from jety import Jety
from time import sleep, time
from firebeam import Firebeam
from magnet import Magnet
from coin import Coins
from movement import playermove, boardmove
from board import MAGNETS

import os

input("\n\n\n\n\t\t\t\t\tPress any key to start: ")
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[sTime: 120s\t\t\t\t\t\t\t\t Score: 0\n"
      + "\t\t\t\t\t Lives: 3\n")
brd = Board(28, 2000)
player = Jety(23, 9, brd)
print("\033[uTime: 120s\t\t\t\t\t\t\t\t Score: 0\n"
      + "\t\t\t\t\t Lives: 3\n")
brd.print_board()
Magnet(10, 140, brd)
Firebeam(10, 10, "slant_right", brd)
# FIREBEAMS.append(fb_1)
cn_1 = Coins(20, 50, 0, brd)
sleep(1)
t = s = g = m = time()

while 1:
    if time() - m >= 0.05:
        for i in MAGNETS:
            i.attract(brd, player)
        m = time()
    player.print_stats()
    brd.print_board()
    playermove(brd, player)
    if time()-t >= 1:
        player.tick()
        t = time()
    # if time()-s >= 0.1:
    #     boardmove(brd, player)
    #     s = time()
    if player.gravity:
        if time()-g >= 0.005:
            playermove(brd, player, "down")
            g = time()
    else:
        player.gravity = 1




# j = 10
# k = 0
# jump = [23, 19, 17, 19, 23]
# t = s = time()
# i = 0
# end = min(200, 201 - int(os.popen("stty size", 'r').read().split()[1]))
# while i < end:
#     while k < len(jump) and i < end:
#         player.print_stats()
#         brd.start = i
#         brd.print_board()
#         if time() - s >= 0.1:
#             s = time()
#             player.move(jump[k], j, brd)
#             k = k + 1
#             i = i+1
#             j = j+1
#         if time() - t >= 1:
#             player.tick()
#             t = time()
#     k = 0
