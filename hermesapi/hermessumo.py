import sys

import time

from bybop.bybop import Bybop_Device
from bybop.bybop.Bybop_Discovery import Discovery, DeviceID, get_name


class HermesSumo():
    def __init__(self):
        self.drone = None
        self.connect()

    def connect(self):
        discovery = Discovery(DeviceID.ALL)
        discovery.wait_for_change()
        devices = discovery.get_devices()
        discovery.stop()
        if not devices:
            print 'Oops ...'
            sys.exit(1)

        device = devices.itervalues().next()

        print 'Will connect to ' + get_name(device)

        d2c_port = 54321
        controller_type = "PC"
        controller_name = "bybop shell"

        self.drone = Bybop_Device.create_and_connect(device, d2c_port, controller_type, controller_name)
        if self.drone is None:
            print 'Unable to connect to a product'
            sys.exit(1)

        self.drone.dump_state()

    def disconnect(self):
        self.stop()
        self.drone = None
        return True

    def move(self, speed, turn):
        self.drone.move(speed, turn)
        return True

    def change_posture(self, posture_type):
        self.drone.change_posture(posture_type)
        return True

    def jump(self, jump_type):
        self.drone.jump(jump_type)
        return True

    def jump_load(self):
        self.drone.jump_load()
        return True

    def jump_cancel(self):
        self.drone.jump_load()
        return True

    def jump_stop(self):
        self.drone.jump_load()
        return True

    def simple_animation(self, animation_type):
        self.drone.simple_animation(animation_type)
        return True

    def stop(self):
        self.drone.stop()
        return True

if __name__=='__main__':
    b = Hermes()
    b.change_posture(0)
    for i in range(10):
        b.move(50, 0)
        time.sleep(.25)
    b.move(50, 50)
    for i in range(10):
        b.move(50, 0)
        time.sleep(.25)
    b.change_posture(1)
    b.stop()
