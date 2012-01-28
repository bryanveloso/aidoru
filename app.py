from flask import Flask, jsonify


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    d = {
        'resources': {
            '/random': 'A random picture of a Japanese idol.',
            '/count': 'The number of idols we have.'
        },
        'source': 'https://github.com/bryanveloso/aidoru'
    }
    return jsonify(d)


@app.route('/random')
def random_idol():
    pass


@app.route('/count')
def count_idols():
    pass


if __name__ == '__main__':
    app.run()
