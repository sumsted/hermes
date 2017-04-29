from unittest import TestCase
from hermes.hermes import Hermes


class TestHermes(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.h = Hermes()

    @classmethod
    def tearDownClass(cls):
        cls.h.disconnect()

    def test_Hermes_disconnect(self):
        self.assertTrue(self.h.disconnect())

    def test_Hermes_move(self):
        speed = 100
        turn = 0
        self.assertTrue(self.h.move(speed, turn))
        speed = 0
        turn = 50
        self.assertTrue(self.h.move(speed, turn))

    def test_Hermes_change_posture(self):
        posture_type = 0
        self.assertTrue(self.h.change_posture(posture_type))
        posture_type = 1
        self.assertTrue(self.h.change_posture(posture_type))

    def test_Hermes_jump(self):
        jump_type = 1
        self.assertTrue(self.h.jump(jump_type))

    def test_Hermes_jump_load(self):
        self.assertTrue(self.h.jump_load())

    def test_Hermes_jump_cancel(self):
        self.assertTrue(self.h.jump_cancel())

    def test_Hermes_jump_stop(self):
        self.assertTrue(self.h.jump_stop())

    def test_Hermes_simple_animation(self):
        animation_type = 3
        self.assertTrue(self.h.simple_animation(animation_type))

    def test_Hermes_stop(self):
        self.assertTrue(self.h.stop())

