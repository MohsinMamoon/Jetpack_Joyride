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

    save = inp
    speed = 1
    if inp in ['d', 'a', 'w']:
        if player.name == "jety":
            speed = player.speed
    for ss in range(speed):

        __move = 0
        nxt = [0, 0]
        prs = player.get_pos()
        pl_size = player.get_size()
        brd_range = board.get_bounds()
        brd_size = board.get_size()

        if inp == " ":
            player.ch_state("sheild")
            return
        elif inp == "b":
            player.attack(board)
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
            if player.name == "jety":
                player.gravity(0)
            nxt[0], nxt[1] = prs[0]-1, prs[1]
        elif inp == 'down':
            nxt[0], nxt[1] = prs[0]+1, prs[1]
        elif inp == 'q':
            quit()
        else:
            inp = "none"
            nxt[0], nxt[1] = prs[0], prs[1]
        if brd_range[1] == brd_size[1]:
            brd_range[1] -= 2
        nxt[0] = min(brd_size[0] - 2 - pl_size[0], nxt[0])
        nxt[0] = max(2, nxt[0])
        if player.name == 'jety':
            if nxt[0] == prs[0] and inp == "down":
                player.gravity(0)
            else:
                player.grav_const(0.5)
            nxt[1] = max(9, brd_range[0], nxt[1])
            nxt[1] = min(nxt[1], brd_range[1] - pl_size[1])

        if player.name == "jety":
            is_sheild = (player.ch_state() == "sheild")
        else:
            is_sheild = 1
        collides, num = board.check_collision(pl_size, nxt, inp, 0)

        if collides == "none" or collides == "coin" or collides == "po_up":
            __move = 1

            for i in range(num):
                if player.name == "jety":
                    player.inc_score("coin")

            if collides == "po_up" and player.name == "jety":
                player.powerup()

        if collides == "dragon" or collides == "firebeam" or collides == "iceball":
            if not is_sheild:
                player.die(board)

        if collides == "fireball":
            if player.name == "dragon":
                player.die(board)

        if __move:
            player.move(nxt[0], nxt[1], board)
            if nxt == [6, brd_size[1] - 6]:
                print("GAME OVER:\nYOU WIN\n")
                quit()
        else:
            if player.name == "jety" and inp == "down":
                player.gravity(0)
        inp = save


def boardmove(board, player):
    board.update_range(1)

    pl_pos = player.get_pos()
    brd_range = board.get_bounds()

    if pl_pos[1] < brd_range[0]+5:
        playermove(board, player, 'd')


def bulletmove(board, player, bullet, gravity=0):

    speed = 1
    if bullet.name == "fireball" and not gravity:
        speed = player.speed
    for i in range(speed):
        nxt = [0, 0]
        prs = bullet.get_pos()
        brd_range = board.get_bounds()
        brd_size = board.get_size()
        if not gravity:
            if bullet.state == "right":
                nxt[0], nxt[1] = prs[0], prs[1] + 1
                if nxt[1] >= brd_range[1] - 3:
                    bullet.die(board)
                    return
            elif bullet.state == "left":
                nxt[0], nxt[1] = prs[0], prs[1] - 1
                if nxt[1] <= brd_range[0]:
                    bullet.die(board)
                    return
        else:
            nxt[0], nxt[1] = prs[0] + 1, prs[1]
            if nxt[0] >= brd_size[0]:
                bullet.die(board)
                return

        nxt[0] = min(brd_size[0] - 4, nxt[0])
        nxt[0] = max(2, nxt[0])
        nxt[1] = max(2, brd_range[0], nxt[1])
        nxt[1] = min(nxt[1], brd_range[1] - 3)

        collides, num = board.check_collision(bullet.get_size(), nxt, bullet.state, bullet.name)

        if collides == "none" or collides == "coin":
            bullet.move(nxt[0], nxt[1], board)

        elif collides == "firebeam":
            if bullet.name == "fireball":
                if player.name == "jety":
                    player.inc_score("firebeam")

        elif collides == "magnet":
            if bullet.name == "fireball":
                if player.name == "jety":
                    player.inc_score("magnet")

        elif collides == "dragon":
            if bullet.name == "fireball":
                if player.name == "jety":
                    player.inc_score("dragon")

        if collides != "none":
            bullet.die(board)
            return
