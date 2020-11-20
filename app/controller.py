from flask import render_template, request, redirect
from app import app
from app.models.player import *
from app.models.game import *

@app.route('/<hand1>/<hand2>')
def play_game(hand1, hand2):
    player_1 = Player("Player 1", hand1)
    player_2 = Player("Player 2", hand2)
    current_game = Game(player_1, player_2)
    winner = current_game.get_winner()
    return render_template("results.html", winner=winner)

    # get winner variable into a form somehow?
    #  winner = winner in route?


#    