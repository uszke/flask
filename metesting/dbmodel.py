from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:mateusz1@localhost/iotproject'
app.debug = True
db = SQLAlchemy(app)


class Iotdata(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    gpsx = db.Column(db.Numeric(20, 6))
    gpsy = db.Column(db.Numeric(20, 6))
    messtype = db.Column(db.String(50))
    messvalue = db.Column(db.Numeric(20, 2))
    ts = db.Column(db.TIMESTAMP)

    def __init__(self, gpsx, gpsy, messtype, messvalue, ts):
        self.gpsx = gpsx
        self.gpsy = gpsy
        self.messtype = messtype
        self.messvalue = messvalue
        self.ts = ts

    def __repr__(self):
        return self.messtype


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/post_iotdata', methods=['POST'])
def post_iotdata():
    iotdata = Iotdata(gpsx = 100.23, gpsy = 101.24, messtype=request.form['message'], messvalue=request.form['iotdata'], ts='2017-06-22 19:10:25-07')
    db.session.add(iotdata)
    db.session.commit()
    return redirect(url_for('saveddata'))