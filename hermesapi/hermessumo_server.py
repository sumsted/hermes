from bottle import get, route, request, response, run, post
from hermessumo import HermesSumo


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


hermes = HermesSumo()


@get('/HermesSumo_disconnect')
@handle_padded
def HermesSumo_disconnect(kargs):
    r = {'return_value': hermes.disconnect()}
    return r


@get('/HermesSumo_move/<speed>/<turn>')
@handle_padded
def HermesSumo_move(kargs):
    r = {'return_value': hermes.move(int(kargs['speed']), int(kargs['turn']))}
    return r


@get('/HermesSumo_change_posture/<posture_type>')
@handle_padded
def HermesSumo_change_posture(kargs):
    r = {'return_value': hermes.change_posture(int(kargs['posture_type']))}
    return r


@get('/HermesSumo_jump/<jump_type>')
@handle_padded
def HermesSumo_jump(kargs):
    r = {'return_value': hermes.jump(int(kargs['jump_type']))}
    return r


@get('/HermesSumo_jump_load')
@handle_padded
def HermesSumo_jump_load(kargs):
    r = {'return_value': hermes.jump_load()}
    return r


@get('/HermesSumo_jump_cancel')
@handle_padded
def HermesSumo_jump_cancel(kargs):
    r = {'return_value': hermes.jump_cancel()}
    return r


@get('/HermesSumo_jump_stop')
@handle_padded
def HermesSumo_jump_stop(kargs):
    r = {'return_value': hermes.jump_stop()}
    return r


@get('/HermesSumo_simple_animation/<animation_type>')
@handle_padded
def HermesSumo_simple_animation(kargs):
    r = {'return_value': hermes.simple_animation(int(kargs['animation_type']))}
    return r


@get('/HermesSumo_stop')
@handle_padded
def HermesSumo_stop(kargs):
    r = {'return_value': hermes.stop()}
    return r


run(host='0.0.0.0', port=8080, debug=True)
