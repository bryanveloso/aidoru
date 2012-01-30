import random
import os

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
    return jsonify({'idol': str(idol)})


@app.route('/bomb')
def bomb_idols():
    idols = random.sample(images, DEFAULT_BOMB)
    return jsonify({'idols': idols})


@app.route('/count')
def count_idols():
    count = len(images)
    return jsonify({'count': count})


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
