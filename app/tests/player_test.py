import unittest

from app.models.game import *
from app.models.player import * 

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player 1", "rock")
        self.player_2 = Player("Player 2", "scissors")

    
    def test_player_1_has_name(self):
        self.assertEqual("Player 1", self.player_1.name)

    def test_player_2_has_hand(self):
        self.assertEqual("scissors", self.player_2.hand)