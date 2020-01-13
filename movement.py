import signal

from alarmexception import AlarmException
from getch import _getChUnix as getchar


def playermove(board, player, inp=""):

    def alarmhandler(signum, frame):

        raise AlarmException

    def user_input(timeout=0.15):

        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            text = getchar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    if inp == "":
        inp = user_input()

    __move = 0
    nxt = [0, 0]
    prs = player.get_pos()
    pl_size = player.get_size()
    brd_range = board.get_bounds()
    brd_size = board.get_size()
    # print("Current Position: ", prs[0], ", ", prs[1])

    if inp == " ":
        player.ch_state("sheild")
        return
    elif inp == 'd':
        inp = "right"
        player.ch_state(inp)
        nxt[0], nxt[1] = prs[0], prs[1]+1
        if nxt[1] >= brd_range[1]-pl_size[1] - 10:
            board.update_range(1)
            brd_range = board.get_bounds()
    elif inp == 'a':
        inp = "left"
        player.ch_state(inp)
        nxt[0], nxt[1] = prs[0], prs[1]-1
        if nxt[1] <= brd_range[0] + 14:
            board.update_range(-1)
            brd_range = board.get_bounds()
    elif inp == 'w':
        inp = "up"
        player.gravity = 0
        nxt[0], nxt[1] = prs[0]-1, prs[1]
    elif inp == 'down':
        nxt[0], nxt[1] = prs[0]+1, prs[1]
    elif inp == 'q':
        quit()
    else:
        inp = "none"
        nxt[0], nxt[1] = prs[0], prs[1]
    if brd_range[1] == brd_size[1]:
        brd_range[1] = brd_range[1] - 2
    nxt[0] = min(brd_size[0] - 2 - pl_size[0], nxt[0])
    nxt[0] = max(2, nxt[0])
    nxt[1] = max(9, brd_range[0], nxt[1])
    nxt[1] = min(nxt[1], brd_range[1] - pl_size[1])

    # print("New postion: ", nxt[0], ", ", nxt[1])
    collides, num = board.check_collision(pl_size, nxt, inp, player.ch_state() == "sheild")

    if collides == "none":
        __move = 1

    if collides == "coin":
        __move = 1
        for i in range(num):
            player.inc_score("coin")

    if collides == "firebeam":
        if num:
            __move = 1
            player.inc_score("firebeam")
        else:
            player.die(board)

    # if collides == "dragon":
    #     if not num:
    #         player.die()

    if collides == "magnet":
        if num:
            __move = 1
            player.inc_score("magnet")

    if __move:
        player.move(nxt[0], nxt[1], board)


def boardmove(board, player):
    board.update_range(1)

    pl_pos = player.get_pos()
    brd_range = board.get_bounds()

    if pl_pos[1] < brd_range[0]+5:
        playermove(board, player, 'd')
