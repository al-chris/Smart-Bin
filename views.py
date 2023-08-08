from SmartBin import app, db
from SmartBin.models import Data
from flask import render_template, url_for, request, make_response, jsonify

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')
    # return render_template('index.html', posts=posts)

@app.route('/', methods = ["POST"])
def info_stream():
    if request.method != 'POST':
        return render_template("index.html")
    
    location = request.form['location']
    percent = request.form['percent']
    # find out how many times they visit the bin by tracking usage pattern
    # estimate user waste pattern from the data
    # manage the grid 
    # but for now, use dummy data in the presentation

    
    entry = Data(percent=percent, location=location)
    db.session.add(entry)
    db.session.commit()

    return make_response(jsonify([{'response':'success'}]), 200)