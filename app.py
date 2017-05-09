from hermes.hermesbeebop import HermesBeebop
from what3words.what3words import get_coords


class App:

    def __init__(self):
        self.drone = HermesBeebop()
        self.original_home = self.drone.get_location()
        self.base_altitude = self.original_home['altitude']

    def start(self, three_words):
        coords = get_coords(three_words)

        self.drone.set_home(coords[0], coords[1], self.base_altitude)
        self.drone.take_off()
        self.drone.move_by(0, 0, 2, 0)
        self.drone.navigate_home()
        self.drone.land()


if __name__ == '__main__':
    app = App()
    app.start()