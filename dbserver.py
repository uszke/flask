from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3898@localhost/iot_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)


class Iotdata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.Numeric(80), unique=True)
    gpsx = db.Column(db.Numeric(20, 6))
    gpsy = db.Column(db.Numeric(20, 6))
    # messtype = db.Column(db.String(50))
    # messvalue = db.Column(db.Numeric(20, 2))
    ts = db.Column(db.TIMESTAMP)

    def __init__(self, deviceid, gpsx, gpsy, ts):
        self.deviceid = deviceid
        self.gpsx = gpsx
        self.gpsy = gpsy
        self.ts = ts

    def __repr__(self):
        return '<User %r>' % self.gpsx + '<id %r>' % self.gpsy


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/showgata_gps')
def data_output():
    return render_template('showdata_gps.html')


@app.route('/map')
def map_render():
    return render_template('map.html')


@app.route('/savedata_gps')
def saveddata():
    return render_template('savedata_gps.html')


@app.route('/add')
def addbike():
    return render_template('add.html')


@app.route('/post_coordinates', methods=['POST'])  # the post form from html
def post_user():
    deviceid = request.form['deviceid']
    print(deviceid)
    try:
        if deviceid == '666':
            return redirect('savedata_gps')
        else:
            return render_template('add.html')
    except:
        deviceid


@app.route('/showdata_gps')
def showdata():
    myIotdata = Iotdata.query.all()
    myIotorder = Iotdata.query.order_by('-id').first()
    myIotdata = Iotdata.query.limit(1).all()
    myIotdata = Iotdata.query.filter('id')
    myIotdata = Iotdata.query.first()
    print(myIotdata[0].deviceid)
    return render_template('showdata_gps.html', myIotdata=myIotdata)


if __name__ == "__main__":
    app.run()
