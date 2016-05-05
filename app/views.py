#!usr/bin/python
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Yvonne'}  # fake user
    #renders the existing template ie the index.html template
    return render_template('index.html'
                           title='Home',
                           user=user)


