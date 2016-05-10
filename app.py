#!usr/bin/python
from flask import Flask

app = Flask(__name__)
guesses = ['Python', 'Java', 'C++']

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

@app.route('/guess/<int:id>')
def index():
    return ('<h1>Hello world!</h1>'
            '<p>My guess: {0}</p>').format(guesses[id])

if __name__ == '__main__':
    app.run(debug=True)
