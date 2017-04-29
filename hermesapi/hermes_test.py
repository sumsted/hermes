from unittest import TestCase, main
from hermes_client import *


class TestHermes(TestCase):
    def test_Hermes___init__(self):
        self.assertEqual(Hermes___init__(), None)

    def test_Hermes_connect(self):
        self.assertEqual(Hermes_connect(), None)

    def test_Hermes_disconnect(self):
        self.assertEqual(Hermes_disconnect(), None)

    def test_Hermes_move(self):
        speed = None
        turn = None
        self.assertEqual(Hermes_move(speed, turn), None)

    def test_Hermes_change_posture(self):
        posture_type = None
        self.assertEqual(Hermes_change_posture(posture_type), None)

    def test_Hermes_jump(self):
        jump_type = None
        self.assertEqual(Hermes_jump(jump_type), None)

    def test_Hermes_jump_load(self):
        self.assertEqual(Hermes_jump_load(), None)

    def test_Hermes_jump_cancel(self):
        self.assertEqual(Hermes_jump_cancel(), None)

    def test_Hermes_jump_stop(self):
        self.assertEqual(Hermes_jump_stop(), None)

    def test_Hermes_simple_animation(self):
        animation_type = None
        self.assertEqual(Hermes_simple_animation(animation_type), None)

    def test_Hermes_stop(self):
        self.assertEqual(Hermes_stop(), None)

if __name__ == '__main__':
    main()
