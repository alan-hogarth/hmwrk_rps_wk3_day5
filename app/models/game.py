class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def get_winner(self):
        if self.player_1.hand == "rock" and self.player_2.hand == "scissors":
           return "Rock beats Scissors: player 1 wins"
        elif self.player_1.hand == "scissors" and self.player_2.hand == "rock":
            return "Rock beats Scissors: player 2 wins!"
        elif self.player_1.hand == "rock" and self.player_2.hand == "rock":
            return "Rock/Rock: It's a draw"
        elif self.player_1.hand == "scissors" and self.player_2.hand == "scissors":
            return "Scissors/Scissors: it's a draw"
        elif self.player_1.hand == "rock" and self.player_2.hand == "paper":
            return "Paper beats Rock: player 2 wins!"
        elif self.player_1.hand == "paper" and self.player_2.hand == "rock":
            return "Paper beats Rock: player 1 wins!"
        elif self.player_1.hand == "paper" and self.player_2.hand == "paper":
            return "Paper/Paper: it's a draw"
        elif self.player_1.hand == "scissors" and self.player_2.hand == "paper":
            return "Scissors beats Paper: player 1 wins!"
        elif self.player_1.hand == "paper" and self.player_2.hand == "scissors":
            return "Scissors beats Paper: player 2 wins!"
        
        
  


