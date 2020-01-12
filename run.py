from board import Board
from jety import Jety
from time import sleep, time
import os

input("\n\n\n\n\t\t\t\t\tPress any key to start: ")
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[sTime: 120s\t\t\t\t\t\t\t\t Score: 0\n"
      + "\t\t\t\t\t Lives: 3\n")
brd = Board(20, 200)
player = Jety(15, 9, brd)
print("\033[uTime: 120s\t\t\t\t\t\t\t\t Score: 0\n"
      + "\t\t\t\t\t Lives: 3\n")
brd.print_board(0)
sleep(1)

j = 10
k = 0
jump = [15, 11, 9, 11, 15]
t = s = time()
i = 0
end = min(200, 201 - int(os.popen("stty size", 'r').read().split()[1]))
while i < end:
    while k < len(jump) and i < end:
        player.print_stats()
        brd.print_board(i)
        if time() - s >= 0.1:
            s = time()
            player.move(jump[k], j, brd)
            k = k + 1
            i = i+1
            j = j+1
        if time() - t >= 1:
            player.tick()
            t = time()
    k = 0
