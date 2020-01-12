import signal

from alarmexception import AlarmException
from getch import _getChUnix as getchar


def playermove(board, player):

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

    inp = user_input()

    nxt = (0, 0)
    prs = player.get_pos()

    if inp == 'd':
        player.ch_state("right")
        nxt[0], nxt[1] = prs[0], prs[1]+1
    if inp == 'a':
        player.ch_state("left")
        nxt[0], nxt[1] = prs[0], prs[1]-1
    if inp == 'w':
        nxt[0], nxt[1] = prs[0]+1, prs[1]

    collides = board.check_collision(player.get_size(), nxt)
    
    if collides == "none":
        player.move(nxt[0], nxt[1], board)
    
    if collides == "coin":
        player.move(nxt[0], nxt[1], board)
        player.inc_score("coin")

    if collides == "powerup":
        player.move(nxt[0], nxt[1], board)