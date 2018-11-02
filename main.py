from flask import Flask, request, session, redirect, url_for, flash, g
from flask import render_template
from .sqloperate import auth, load_logged_in
import functools

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            print(g.user)
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = load_logged_in(user_id=user_id)


@app.route('/')
def index(name=None):
    return render_template('base.html', name=name)
# @app.route('/register')
# def register(name=None):
#     return render_template('register.html', name=name)
#
# @app.route('/register/cargo')
# def cargo(name=None):
#     return render_template('cargo.html', name=name)
#
# @app.route('/register/visit')
# def visit(name=None):
#     return render_template('visit.html', name=name)
# # if __name__ == '__main__':
# #     app.run(debug=True)


@app.route('/manage')
@login_required
def manage(name=None):
    print(g.user)
    return 'abc'


@app.route('/login', methods=('GET', 'POST'))
def login(name=None):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        error = None
        user = auth(username=username, password=password, status='username if have')

        if user is None:
            error = 'Incorrect username'
            flash(error)
            return redirect(url_for('login'))
        status = auth(username=username, password=password, status='verify')
        if status is None:
            error = 'Incorrect password'
            print('Incorrect password')
            flash(error)
            return render_template('login.html')
        elif status is True:
            session.clear()
            session['user_id'] = username
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            error = auth(username=username, password=None, status='username if have')
            if error is None:
                auth(username=username, password=password, status='registered')
                return redirect(url_for('login'))
            else:
                flash(error)
                return redirect(url_for('register'))
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



