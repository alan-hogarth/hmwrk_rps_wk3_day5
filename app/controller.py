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

    # get winner variable into a form
    #  winner = winner as render_template parameter


@app.route('/welcome')
def rules():
    return render_template("welcome.html")

# @app.route('/play', methods=['GET', 'POST'])
# def play():
#     return render_template("play.html")

@app.route('/play', methods=['GET', 'POST'])
def game_play():
    return render_template("play.html")
    print(request.form)
    player_name = request.form["name"]
    player_move = request.form["hand"]

    player_submit = Game(player_name, player_move)
    player_result = player_submit.get_winner()
    return redirect("/results.html")
    