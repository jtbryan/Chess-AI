""" Shows how to use flask and matplotlib together.
Shows SVG, and png.
The SVG is easier to style with CSS, and hook JS events to in browser.
python3 -m venv venv
. ./venv/bin/activate
pip install flask matplotlib
python flask_matplotlib.py
"""
import io
import random
import webbrowser
import chess
import chess.svg
from flask import Flask, Response, request
app = Flask(__name__)


@app.route("/")
def index():
    """ Returns html with the img tag for your plot.
    """
    num_x_points = int(request.args.get("num_x_points", 50))
    # in a real app you probably want to use a flask template.
    return f"""
    <h1 style="text-align: center">Flask and matplotlib</h1>
    <img style="display: block;margin-left: auto; margin-right: auto; width: 50%;" width=600 height=600 src="/board.svg">
    """
    # from flask import render_template
    # return render_template("yourtemplate.html", num_x_points=num_x_points)

@app.route("/board.svg")
def loadBoard():
    return Response(chess.svg.board(board=chess.Board()), mimetype='image/svg+xml')

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)
