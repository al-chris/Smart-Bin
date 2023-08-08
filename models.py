from SmartBin import db, app
from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    time = db.Column(db.DateTime, default = datetime.now())
    percent = db.Column(db.Numeric)
    location = db.Column(db.String(50))
