import time

from hermes.hermes import Hermes


def start():
    b = Hermes()
    b.change_posture(0)
    for i in range(10):
        b.move(100, 0)
        time.sleep(.25)
    b.move(0, 50)
    time.sleep(.5)
    for i in range(10):
        b.move(100, 0)
        time.sleep(.25)
    b.change_posture(1)
    b.stop()


if __name__=='__main__':
    start()