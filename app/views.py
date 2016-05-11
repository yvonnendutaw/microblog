from flask import Flask, render_template
from app import app

guesses = ['Python', 'Java', 'C++']
@app.route('/')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': {'nickname': 'Jane'}, 
            'body': 'Hi i am Jane!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', 
                           guess=guesses[id])