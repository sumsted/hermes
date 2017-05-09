from unittest import TestCase, main
from hermesbeebop_client import *


class TestHermesbeebop(TestCase):
    def test_HermesBeebop___init__(self):
        self.assertEqual(HermesBeebop___init__(), None)

    def test_HermesBeebop_connect(self):
        self.assertEqual(HermesBeebop_connect(), None)

    def test_HermesBeebop_disconnect(self):
        self.assertEqual(HermesBeebop_disconnect(), None)

    def test_HermesBeebop_take_off(self):
        self.assertEqual(HermesBeebop_take_off(), None)

    def test_HermesBeebop_land(self):
        self.assertEqual(HermesBeebop_land(), None)

    def test_HermesBeebop_emergency(self):
        self.assertEqual(HermesBeebop_emergency(), None)

    def test_HermesBeebop_flat_trim(self):
        self.assertEqual(HermesBeebop_flat_trim(), None)

    def test_HermesBeebop_navigate_home(self):
        self.assertEqual(HermesBeebop_navigate_home(), None)

    def test_HermesBeebop_move_by(self):
        dx = None
        dy = None
        dz = None
        dr = None
        self.assertEqual(HermesBeebop_move_by(dx, dy, dz, dr), None)

    def test_HermesBeebop_max_altitude(self):
        m = None
        self.assertEqual(HermesBeebop_max_altitude(m), None)

    def test_HermesBeebop_max_tilt(self):
        d = None
        self.assertEqual(HermesBeebop_max_tilt(d), None)

    def test_HermesBeebop_max_distance(self):
        m = None
        self.assertEqual(HermesBeebop_max_distance(m), None)

    def test_HermesBeebop_autonomous_flight_max_horizontal_speed(self):
        ms = None
        self.assertEqual(HermesBeebop_autonomous_flight_max_horizontal_speed(ms), None)

    def test_HermesBeebop_autonomous_flight_max_vertical_speed(self):
        ms = None
        self.assertEqual(HermesBeebop_autonomous_flight_max_vertical_speed(ms), None)

    def test_HermesBeebop_autonomous_flight_max_horizontal_acceleration(self):
        mss = None
        self.assertEqual(HermesBeebop_autonomous_flight_max_horizontal_acceleration(mss), None)

    def test_HermesBeebop_autonomous_flight_max_vertical_acceleration(self):
        mss = None
        self.assertEqual(HermesBeebop_autonomous_flight_max_vertical_acceleration(mss), None)

    def test_HermesBeebop_autonomous_flight_max_rotation_speed(self):
        ms = None
        self.assertEqual(HermesBeebop_autonomous_flight_max_rotation_speed(ms), None)

    def test_HermesBeebop_max_vertical_speed(self):
        ms = None
        self.assertEqual(HermesBeebop_max_vertical_speed(ms), None)

    def test_HermesBeebop_max_rotation_speed(self):
        ms = None
        self.assertEqual(HermesBeebop_max_rotation_speed(ms), None)

    def test_HermesBeebop_set_home(self):
        lat = None
        lon = None
        alt = None
        self.assertEqual(HermesBeebop_set_home(lat, lon, alt), None)

    def test_HermesBeebop_get_location(self):
        self.assertEqual(HermesBeebop_get_location(), None)

    def test_HermesBeebop_get_state(self):
        self.assertEqual(HermesBeebop_get_state(), None)

if __name__ == '__main__':
    main()
