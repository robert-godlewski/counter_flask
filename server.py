from flask import Flask, render_template, redirect, session


app = Flask(__name__)

app.secret_key = 'hello'

@app.route('/')
def counter(): 
    if 'count' not in session: session['count'] = 0
    else: session['count'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session(): 
    session.clear()
    return redirect('/')

@app.route('/double_count')
def double_count():
    session['count'] += 1
    return redirect('/')


if __name__ == "__main__": app.run(debug=True, port=8000)
