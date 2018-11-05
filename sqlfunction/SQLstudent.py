import sqlite3


def student_write(student_num, name, gender, stay_time, room_id, class_num, department_name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (student_num, name, gender, stay_time, room_id, class_num, department_name)
    cursor.execute('''
            insert into student values (?,?,?,?,?,?,?);
    ''', data)
    conn.commit()
    conn.close()


def student_search():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('''
        select 
    ''')
    conn.commit()
    conn.close()


def student_delete():
    pass


def department_list():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    de_list = cursor.execute('''
        select department_name from department
    ''').fetchall()
    conn.commit()
    conn.close()
    return de_list
