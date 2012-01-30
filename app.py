import random

from flask import Flask, jsonify
from images import images


app = Flask(__name__)
app.debug = True

# The number of idols we drop by default.
DEFAULT_BOMB = 5


@app.route('/')
def index():
    d = {
        'resources': {
            '/random': 'A random picture of a Japanese idol.',
            '/bomb': 'Bomb idols.',
            '/count': 'The number of idols we have.'
        },
        'source': 'https://github.com/bryanveloso/aidoru'
    }
    return jsonify(d)


@app.route('/random')
def random_idol():
    idol = random.sample(images, 1)
    return jsonify({'idol': idol})


@app.route('/bomb')
def bomb_idols():
    idols = random.sample(images, DEFAULT_BOMB)
    return jsonify({'idols': idols})


@app.route('/count')
def count_idols():
    count = len(images)
    return jsonify({'count': count})


if __name__ == '__main__':
    app.run()
