from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/post_user', methods=['POST'])
def post_user():
    messtype = request.form['username']
    messvalue = request.form['email']
    return "<h1 style='color: red'>hello flask - saved some data</h1>"

#@app.route('/post_iotdata', methods=['POST'])
#def post_iotdata():

#    iotdata = iotdata(gpsx = 100.23, gpsy = 101.24, messtype = request.form['message'], messvalue = request.form['iotdata'], ts = '2017-06-22 19:10:25-07')
#    db.session.add(iotdata)
#    db.session.commit()
#    return redirect(url_for('saveddata'))