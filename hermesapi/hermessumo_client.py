import requests

host = 'http://0.0.0.0:8080'


def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


def HermesSumo___init__():
    return g('HermesSumo___init__', )['return_value']


def HermesSumo_connect():
    return g('HermesSumo_connect', )['return_value']


def HermesSumo_disconnect():
    return g('HermesSumo_disconnect', )['return_value']


def HermesSumo_move(speed, turn):
    return g('HermesSumo_move', speed, turn)['return_value']


def HermesSumo_change_posture(posture_type):
    return g('HermesSumo_change_posture', posture_type)['return_value']


def HermesSumo_jump(jump_type):
    return g('HermesSumo_jump', jump_type)['return_value']


def HermesSumo_jump_load():
    return g('HermesSumo_jump_load', )['return_value']


def HermesSumo_jump_cancel():
    return g('HermesSumo_jump_cancel', )['return_value']


def HermesSumo_jump_stop():
    return g('HermesSumo_jump_stop', )['return_value']


def HermesSumo_simple_animation(animation_type):
    return g('HermesSumo_simple_animation', animation_type)['return_value']


def HermesSumo_stop():
    return g('HermesSumo_stop', )['return_value']


if __name__ == '__main__':
    pass
