from flask import Flask
from flask import render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    game = GameOfLife()
    game.get_new_world()
    game.populate_world()
    return render_template('index.html')


@app.route('/life')
def life():
    game = GameOfLife()
    render = render_template('life.html', game=game)
    game.get_new_generation()
    return render


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
