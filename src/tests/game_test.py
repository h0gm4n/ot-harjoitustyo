import unittest
import pygame
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.peli = Game()
        self.RED = (255, 0, 0)

    def test_red_assigned_correctly(self):
        self.assertEqual(self.RED, (255, 0, 0))