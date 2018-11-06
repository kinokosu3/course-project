import sqlite3


def student_write(student_num, name, gender, stay_time, room_id, class_num, department_name,apartment_name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (student_num, name, gender, stay_time, room_id, class_num, department_name,apartment_name)
    cursor.execute('''
            insert into student values (?,?,?,?,?,?,?,?);
    ''', data)
    conn.commit()
    conn.close()


def student_search(apartment_name, student_name, student_num):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (apartment_name, student_name, student_num)
    results = cursor.execute('''
        select * from student where apartment_name=? and name =? and student_num=?
    ''', data).fetchall()
    conn.commit()
    conn.close()
    return results

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
