from flask import render_template, request, redirect
from app import app
from app.models.player import *
from app.models.game import *
from random import choice

@app.route('/<hand1>/<hand2>')
def play_game(hand1, hand2):
    player_1 = Player("Player 1", hand1)
    player_2 = Player("Player 2", hand2)
    current_game = Game(player_1, player_2)
    winner = current_game.get_winner()
    
    if winner != None:
        result = winner.name
    else:
        result = None

    return render_template("results.html", player_1 = player_1.name, player_2 = player_2.name, hand1 = hand1, hand2 = hand2, result = result)


@app.route('/welcome')
def rules():
    return render_template("welcome.html")

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/add_move', methods=['GET', 'POST'])
def game_play():
    print(request.form)
    add_name = request.form["name"]
    add_move = request.form["hand"]
    return "logged"
   
# @app.route('/computer')
# def computer_play():
#     moves = ["rock", "paper", "scissors"]
#     random_move = choice(moves)
    
#     player_1 = Player("Player 1", "rock")
#     player_2 = Player("Computer", random_move)
#     current_game = Game(player_1, player_2)
#     winner = current_game.get_winner()
    
    
    