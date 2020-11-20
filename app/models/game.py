class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def get_winner(self):
        if self.player_1.hand == "rock" and self.player_2.hand == "scissors":
           return "player 1 wins"
        elif self.player_1.hand == "scissors" and self.player_2.hand == "rock":
            return "player 2 wins!"
        elif self.player_1.hand == "rock" and self.player_2.hand == "rock":
            return "draw"
        elif self.player_1.hand == "scissors" and self.player_2.hand == "scissors":
            return "draw"
        elif self.player_1.hand == "rock" and self.player_2.hand == "paper":
            return "player 2 wins!"
        elif self.player_1.hand == "paper" and self.player_2.hand == "rock":
            return "player 1 wins!"
        elif self.player_1.hand == "paper" and self.player_2.hand == "paper":
            return "draw"
        elif self.player_1.hand == "scissors" and self.player_2.hand == "paper":
            return "player 1 wins!"
        elif self.player_1.hand == "paper" and self.player_2.hand == "scissors":
            return "player 2 wins!"
        
        
  


