import requests

host = 'http://0.0.0.0:8080'


def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


def HermesBeebop___init__():
    return g('HermesBeebop___init__', )['return_value']


def HermesBeebop_connect():
    return g('HermesBeebop_connect', )['return_value']


def HermesBeebop_disconnect():
    return g('HermesBeebop_disconnect', )['return_value']


def HermesBeebop_take_off():
    return g('HermesBeebop_take_off', )['return_value']


def HermesBeebop_land():
    return g('HermesBeebop_land', )['return_value']


def HermesBeebop_emergency():
    return g('HermesBeebop_emergency', )['return_value']


def HermesBeebop_flat_trim():
    return g('HermesBeebop_flat_trim', )['return_value']


def HermesBeebop_navigate_home():
    return g('HermesBeebop_navigate_home', )['return_value']


def HermesBeebop_move_by(dx, dy, dz, dr):
    return g('HermesBeebop_move_by', dx, dy, dz, dr)['return_value']


def HermesBeebop_max_altitude(m):
    return g('HermesBeebop_max_altitude', m)['return_value']


def HermesBeebop_max_tilt(d):
    return g('HermesBeebop_max_tilt', d)['return_value']


def HermesBeebop_max_distance(m):
    return g('HermesBeebop_max_distance', m)['return_value']


def HermesBeebop_autonomous_flight_max_horizontal_speed(ms):
    return g('HermesBeebop_autonomous_flight_max_horizontal_speed', ms)['return_value']


def HermesBeebop_autonomous_flight_max_vertical_speed(ms):
    return g('HermesBeebop_autonomous_flight_max_vertical_speed', ms)['return_value']


def HermesBeebop_autonomous_flight_max_horizontal_acceleration(mss):
    return g('HermesBeebop_autonomous_flight_max_horizontal_acceleration', mss)['return_value']


def HermesBeebop_autonomous_flight_max_vertical_acceleration(mss):
    return g('HermesBeebop_autonomous_flight_max_vertical_acceleration', mss)['return_value']


def HermesBeebop_autonomous_flight_max_rotation_speed(ms):
    return g('HermesBeebop_autonomous_flight_max_rotation_speed', ms)['return_value']


def HermesBeebop_max_vertical_speed(ms):
    return g('HermesBeebop_max_vertical_speed', ms)['return_value']


def HermesBeebop_max_rotation_speed(ms):
    return g('HermesBeebop_max_rotation_speed', ms)['return_value']


def HermesBeebop_set_home(lat, lon, alt):
    return g('HermesBeebop_set_home', lat, lon, alt)['return_value']


def HermesBeebop_get_location():
    return g('HermesBeebop_get_location', )['return_value']


def HermesBeebop_get_state():
    return g('HermesBeebop_get_state', )['return_value']


if __name__ == '__main__':
    pass
