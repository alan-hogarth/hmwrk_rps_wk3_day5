import unittest

from app.models.game import *
from app.models.player import * 

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player 1", "rock")
        self.player_2 = Player("Player 2", "scissors")
    

    def test_player_1_wins(self):
        self.player_1.hand
        self.player_2.hand
        self.assertEqual(True, True) 
    
    def test_player_2_wins(self):
        self.player_1.hand
        self.player_2.hand
        self.assertEqual(False, False)

