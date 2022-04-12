import unittest
import pygame
#from ui.main_menu import Main_Menu
#from ui.gameplay import Gameplay

class TestGame(unittest.TestCase):
    def setUp(self):
        self.menu = Main_Menu()
        self.game = Gameplay()
        self.RED = (255, 0, 0)

    def test_red_assigned_correctly(self):
        self.assertEqual(self.RED, (255, 0, 0))
