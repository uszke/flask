from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hell(name=None):
    return render_template('hello.html', name=name)