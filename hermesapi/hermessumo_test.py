from unittest import TestCase, main
from hermessumo_client import *


class TestHermessumo(TestCase):
    def test_HermesSumo___init__(self):
        self.assertEqual(HermesSumo___init__(), None)

    def test_HermesSumo_connect(self):
        self.assertEqual(HermesSumo_connect(), None)

    def test_HermesSumo_disconnect(self):
        self.assertEqual(HermesSumo_disconnect(), None)

    def test_HermesSumo_move(self):
        speed = None
        turn = None
        self.assertEqual(HermesSumo_move(speed, turn), None)

    def test_HermesSumo_change_posture(self):
        posture_type = None
        self.assertEqual(HermesSumo_change_posture(posture_type), None)

    def test_HermesSumo_jump(self):
        jump_type = None
        self.assertEqual(HermesSumo_jump(jump_type), None)

    def test_HermesSumo_jump_load(self):
        self.assertEqual(HermesSumo_jump_load(), None)

    def test_HermesSumo_jump_cancel(self):
        self.assertEqual(HermesSumo_jump_cancel(), None)

    def test_HermesSumo_jump_stop(self):
        self.assertEqual(HermesSumo_jump_stop(), None)

    def test_HermesSumo_simple_animation(self):
        animation_type = None
        self.assertEqual(HermesSumo_simple_animation(animation_type), None)

    def test_HermesSumo_stop(self):
        self.assertEqual(HermesSumo_stop(), None)

if __name__ == '__main__':
    main()
