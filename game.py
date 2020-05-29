import io
import random
import webbrowser
import chess
import chess.svg
from flask import Flask, Response, request
app = Flask(__name__)

class NewGame:
    def __init__(self):
        self.board = chess.Board()

    def start(self):
        webbrowser.open("http://127.0.0.1:5000/")
        app.run(debug=True, use_reloader=False)

game = NewGame()

@app.route("/")
def index():
    """ Returns html with the img tag of the chess board"""
    return f"""
    <h1 style="text-align: center">Auto Chess</h1>
    <img style="display: block;margin-left: auto; margin-right: auto; width: 50%;" width=600 height=600 src="/load.svg">
    <a style="display: block;margin-left: auto; margin-right: auto; width: 50%;" href="/move.svg">Move</a>
    """

@app.route("/load.svg")
def loadBoard():
    return Response(chess.svg.board(board=game.board), mimetype='image/svg+xml')

@app.route("/move.svg")
def move():
    legal = game.board.legal_moves
    choice = None
    for move in legal:
        choice = move
    final_choice = chess.Move.from_uci(str(choice))
    game.board.push(final_choice)
    return Response(chess.svg.board(board=game.board), mimetype='image/svg+xml')

if __name__ == "__main__":
    
    game.start()
