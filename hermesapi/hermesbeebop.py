import sys

import time

from bybop.bybop import Bybop_Device
from bybop.bybop.Bybop_Discovery import Discovery, DeviceID, get_name


class HermesBeebop():
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

    def take_off(self):
        self.drone.take_off()
        return True

    def land(self):
        self.drone.land()
        return True

    def emergency(self):
        self.drone.emergency()
        return True

    def flat_trin(self):
        self.drone.flat_trim()
        return True

    def navigate_home(self):
        self.drone.navigate_home()
        return True

    def move_by(self, dx, dy, dz, dr):
        self.drone.move_by(dx, dy, dz, dr)
        return True

    def max_altitude(self, m):
        self.drone.max_altitude(m)
        return True

    def max_tilt(self, d):
        self.drone.max_tilt(d)
        return True

    def max_distance(self, m):
        self.drone.max_distance(m)
        return True

    def autonomous_flight_max_horizontal_speed(self, ms):
        self.drone.autonomous_flight_max_horizontal_speed(ms)
        return True

    def autonomous_flight_max_vertical_speed(self, ms):
        self.drone.autonomous_flight_max_vertical_speed(ms)
        return True

    def autonomous_flight_max_horizontal_acceleration(self, mss):
        self.drone.autonomous_flight_max_horizontal_speed(mss)
        return True

    def autonomous_flight_max_vertical_acceleration(self, mss):
        self.drone.autonomous_flight_max_vertical_acceleration(mss)
        return True

    def autonomous_flight_max_rotation_speed(self, ms):
        self.drone.autonomous_flight_max_rotation_speed(ms)
        return True

    def max_vertical_speed(self, ms):
        self.drone.max_vertical_speed(ms)
        return True

    def max_rotation_speed(self, ms):
        self.drone.max_rotation_speed(ms)
        return True

    def set_home(self, lat, lon, alt):
        self.drone.set_home(lat, lon, alt)
        return True

    def get_location(self):
        return self.drone.get_location()

    def get_state(self):
        return self.drone.get_state()

if __name__=='__main__':
    b = HermesBeebop()
    pass
    b.emergency()
