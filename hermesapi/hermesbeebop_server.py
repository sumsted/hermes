from bottle import get, route, request, response, run, post
from hermesbeebop import HermesBeebop


def handle_padded(handler):
    def decorator(**kwargs):
        r = handler
        try:
            callback = request.query.get('callback')
        except Exception as e:
            callback = None
        if callback is None:
            return r(kwargs)
        else:
            response.content_type = 'text/javascript'
            return "%s(%r);" % (callback, r)
    return decorator

hermes = HermesBeebop()

@get('/HermesBeebop___init__')
@handle_padded
def HermesBeebop___init__(kargs):
    r = {'return_value': hermes.__init__()}
    return r


@get('/HermesBeebop_connect')
@handle_padded
def HermesBeebop_connect(kargs):
    r = {'return_value': hermes.connect()}
    return r


@get('/HermesBeebop_disconnect')
@handle_padded
def HermesBeebop_disconnect(kargs):
    r = {'return_value': hermes.disconnect()}
    return r


@get('/HermesBeebop_take_off')
@handle_padded
def HermesBeebop_take_off(kargs):
    r = {'return_value': hermes.take_off()}
    return r


@get('/HermesBeebop_land')
@handle_padded
def HermesBeebop_land(kargs):
    r = {'return_value': hermes.land()}
    return r


@get('/HermesBeebop_emergency')
@handle_padded
def HermesBeebop_emergency(kargs):
    r = {'return_value': hermes.emergency()}
    return r


@get('/HermesBeebop_flat_trim')
@handle_padded
def HermesBeebop_flat_trim(kargs):
    r = {'return_value': hermes.flat_trim()}
    return r


@get('/HermesBeebop_navigate_home')
@handle_padded
def HermesBeebop_navigate_home(kargs):
    r = {'return_value': hermes.navigate_home()}
    return r


@get('/HermesBeebop_move_by/<dx>/<dy>/<dz>/<dr>')
@handle_padded
def HermesBeebop_move_by(kargs):
    r = {'return_value': hermes.move_by(int(kargs['dx']), int(kargs['dy']), int(kargs['dz']), int(kargs['dr']))}
    return r


@get('/HermesBeebop_max_altitude/<m>')
@handle_padded
def HermesBeebop_max_altitude(kargs):
    r = {'return_value': hermes.max_altitude(int(kargs['m']))}
    return r


@get('/HermesBeebop_max_tilt/<d>')
@handle_padded
def HermesBeebop_max_tilt(kargs):
    r = {'return_value': hermes.max_tilt(int(kargs['d']))}
    return r


@get('/HermesBeebop_max_distance/<m>')
@handle_padded
def HermesBeebop_max_distance(kargs):
    r = {'return_value': hermes.max_distance(int(kargs['m']))}
    return r


@get('/HermesBeebop_autonomous_flight_max_horizontal_speed/<ms>')
@handle_padded
def HermesBeebop_autonomous_flight_max_horizontal_speed(kargs):
    r = {'return_value': hermes.autonomous_flight_max_horizontal_speed(int(kargs['ms']))}
    return r


@get('/HermesBeebop_autonomous_flight_max_vertical_speed/<ms>')
@handle_padded
def HermesBeebop_autonomous_flight_max_vertical_speed(kargs):
    r = {'return_value': hermes.autonomous_flight_max_vertical_speed(int(kargs['ms']))}
    return r


@get('/HermesBeebop_autonomous_flight_max_horizontal_acceleration/<mss>')
@handle_padded
def HermesBeebop_autonomous_flight_max_horizontal_acceleration(kargs):
    r = {'return_value': hermes.autonomous_flight_max_horizontal_acceleration(int(kargs['mss']))}
    return r


@get('/HermesBeebop_autonomous_flight_max_vertical_acceleration/<mss>')
@handle_padded
def HermesBeebop_autonomous_flight_max_vertical_acceleration(kargs):
    r = {'return_value': hermes.autonomous_flight_max_vertical_acceleration(int(kargs['mss']))}
    return r


@get('/HermesBeebop_autonomous_flight_max_rotation_speed/<ms>')
@handle_padded
def HermesBeebop_autonomous_flight_max_rotation_speed(kargs):
    r = {'return_value': hermes.autonomous_flight_max_rotation_speed(int(kargs['ms']))}
    return r


@get('/HermesBeebop_max_vertical_speed/<ms>')
@handle_padded
def HermesBeebop_max_vertical_speed(kargs):
    r = {'return_value': hermes.max_vertical_speed(int(kargs['ms']))}
    return r


@get('/HermesBeebop_max_rotation_speed/<ms>')
@handle_padded
def HermesBeebop_max_rotation_speed(kargs):
    r = {'return_value': hermes.max_rotation_speed(int(kargs['ms']))}
    return r


@get('/HermesBeebop_set_home/<lat>/<lon>/<alt>')
@handle_padded
def HermesBeebop_set_home(kargs):
    r = {'return_value': hermes.set_home(int(kargs['lat']), int(kargs['lon']), int(kargs['alt']))}
    return r


@get('/HermesBeebop_get_location')
@handle_padded
def HermesBeebop_get_location(kargs):
    r = {'return_value': hermes.get_location()}
    return r


@get('/HermesBeebop_get_state')
@handle_padded
def HermesBeebop_get_state(kargs):
    r = {'return_value': hermes.get_state()}
    return r


run(host='0.0.0.0', port=8080, debug=True)
