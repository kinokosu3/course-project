from flask import Flask, request, session, redirect, url_for, flash, g
from flask import render_template
from auth import load_logged_in, auth
from sqlfunction.sqlcargo import cargo_re
from sqlfunction.exists import exists, apartment_list
from sqlfunction.sqlvisit import write_visit, quit_list, write_quit
from sqlfunction.SQLapartment import apartment_write, apartment_delete,apartment_search,apartment_everything
from sqlfunction.SQLstudent import student_write, student_delete, student_search, department_list
import hashlib
import functools

app = Flask(__name__)
app.config['SECRET_KEY'] = 'huangtingfeng'


def sha(data):
    sha1 = hashlib.sha1()
    sha1.update(data.encode('utf-8'))
    ID = sha1.hexdigest()
    return ID



def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("you don't login")
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
    return render_template('index.html', name=name)


# 管理界面
@app.route('/manage')
@login_required
def manage(name=None):
    return render_template('manage.html')


# 登录界面
@app.route('/login', methods=('GET', 'POST'))
def login(name=None):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username, password)
        error = None
        user = auth(username=username, password=password, status='username if have')

        if user is None:
            error = 'Incorrect username'
            flash(error)
            return redirect(url_for('login'))
        status = auth(username=username, password=password, status='verify')
        if status is None:
            error = 'Incorrect password'
            flash(error)
            return render_template('login.html')
        elif status is True:
            session.clear()
            session['user_id'] = username
            flash("login finish")
            return redirect(url_for('index'))
    return render_template('login.html')


# 注册界面
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

# @app.route('/')


@app.route('/student', methods=['GET', 'POST'])
@app.route('/student/<name>', methods=['GET', 'POST'])
@login_required
def student(name=None):
    ap_list = apartment_list()
    department_name = None
    if name == 'write':
        department_name = department_list()
        if request.method == 'POST':
            student_name = request.form['student_name']
            student_num = request.form['student_num']
            gender = request.form['gender']
            stay_time = request.form['stay_time']
            room_id = request.form['room_id']
            class_num = request.form['class_num']
            department = request.form['department']
            if not exists(room_id, 'room', 'room_id'):
                flash('宿舍号出现错误')
            if not exists(class_num, 'class', 'class_num'):
                flash('班级出现错误')
        return render_template('student.html', name=name, department_name=department_name, ap_list=ap_list)
    # if name == 'condition-search':
    #     results =
    if name == 'everything':
        pass

    return render_template('student.html', name=None)



# @app.route('')
#
# def information_search():



@app.route('/apartment', methods=['GET', 'POST'])
@app.route('/apartment/<name>', methods=['GET', 'POST'])
@login_required
def apartment(name=None):
    ap_list = apartment_list()
    if name == 'write':
        if request.method == 'POST':
            property_name = request.form['name']
            apartment_name = request.form['apartment_name']
            value = request.form['value']
            string = apartment_name+value
            ID = sha(string)
            if not exists(ID, 'apartment_manage', 'id'):
                apartment_write(ID, name=property_name,apartment_name=apartment_name, value=value)
                flash('写入OK')
                return redirect('/apartment/write')
            else:
                flash('该财产已经存在')
        return render_template('apartment.html', name=name, ap_list=ap_list)
    if name == 'everything':
        results = apartment_everything()
        return render_template('apartment.html', name=name, results=results)
    if name == 'condition-search':
        results = None
        if request.method == 'POST':
            property_name = request.form['name']
            apartment_name = request.form['apartment_name']
            value = request.form['value']
            results = apartment_search(apartment_name=apartment_name, name=property_name, value=value)
            if not results:
                flash('没有合适条目')
        return render_template('apartment.html', name=name, results=results, ap_list=ap_list)
    return render_template('apartment.html', name=None)


@app.route('/apartment/delete/<name>')
@login_required
def apartment_del(name=None):
    apartment_delete(name)
    return redirect('/apartment/condition-search')


@app.route('/outin')
@login_required
def outin():
    return render_template('outin.html')


@app.route('/outin/visit', methods=['GET', 'POST'])
@app.route('/outin/visit/<name>', methods=['GET', 'POST'])
@login_required
def visit(name=None):
    ap_list = apartment_list()
    if name == 'quit-list':
        ql = quit_list()
        return render_template('visit.html', ql=ql, name=name)
    elif name is not None:
        if request.method == 'POST':
            quit_time = request.form['quit_time']
            write_quit(ID=name, quit_time=quit_time)
            return redirect((url_for('outin')))
        return render_template('visit.html', name=name)
    if request.method == 'POST':
        apartment_name = request.form['apartment_name']
        id_num = request.form['id_num']
        name = request.form['name']
        origin = request.form['origin']
        visit_time = request.form['visit_time']
        string = id_num+name+origin+visit_time+visit_time
        ID = sha(string)
        if not exists(ID, table_name='visit_register', row_name='hash'):
            write_visit(ID=ID, apartment_name=apartment_name,id_num=id_num, name=name, origin=origin, visit_time=visit_time)
    return render_template('visit.html', name=None, ap_list=ap_list)


@app.route('/outin/cargo', methods=['GET', 'POST'])
@login_required
def cargo():
    ap_list = apartment_list()
    if request.method == 'POST':
        apartment_name = request.form['apartment_name']
        cargo_id = request.form['cargo_id']
        time = request.form['time']
        origin = request.form['origin']
        direction = request.form['direction']
        duty_man = request.form['duty_man']
        string = apartment_name+cargo_id+time+origin+direction+duty_man
        ID = sha(string)
        if not exists(ID, table_name='cargo_register', row_name='ID'):
            cargo_re(ID=ID, apartment_name=apartment_name,cargo_id=cargo_id, time=time, origin=origin, direction=direction,duty_man=duty_man)
        else:
            flash('已经存在该记录')
    return render_template('cargo.html', ap_list=ap_list)

