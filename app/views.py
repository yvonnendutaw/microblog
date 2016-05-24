#!usr/bin/python
#!flask/bin/python
import os
from flask import Flask, render_template, request
from app import app

APP_ROOT = os.path.dirname(os.path.abspath((__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload")
def upload():
    target = os.path.join(APP_ROOT, "images/")
    print(target)
    @app.route("/upload")
    if not os.path.isdirname(target):
        os.mkdir(target)
    for file in request.files.getlist("file")
        print file
        filename = file.filename
        destination = "/".join([target,filename])
        print destination
        file.save(destination)
    return render_template("complete.html")

if __name__ ==" __main__":
app.run(debug=True)



