from flask import Flask, render_template, redirect, session


app = Flask(__name__)

app.secret_key = 'hello'

@app.route('/')
def counter(): 
    if 'count' not in session: 
        print('\n', str(session))
        print('count doesn\'t exist.\nNow adding it in?')
        session['count'] = 0
        print(f'session details: {str(session)}')
        print(f"count in session: {str(session['count'])}")
    else: 
        session['count'] += 1
        print(f"\nCount is now: {str(session['count'])}")
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session(): 
    session.clear()
    print('\nRestarted the count.')
    return redirect('/')


if __name__ == "__main__": app.run(debug=True, port=8000)
