from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from flask import redirect

app = Flask(__name__)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/post_user', methods=['POST'])
def post_user():
    messtype = request.form['username']
    messvalue = request.form['email']
    return "<h1 style='color: red'>hello flask - saved some data</h1>"


@app.route('/showdata')
def showdata():
    myIotdata = Iotdata.query.all()
    return render_template('showdata.html', myIotdata=myIotdata)


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
