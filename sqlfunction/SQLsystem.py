import sqlite3


def system_everything(table):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    everything = cursor.execute('select * from '+table+';').fetchall()
    conn.commit()
    conn.close()
    return everything


def system_apartment_write(apartment_name, apartment_dir, floor):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    num = cursor.execute('select count(*) from apartment').fetchone()[0]
    data = (num+1, apartment_name, apartment_dir, floor)
    cursor.execute('insert into apartment values (?,?,?,?)', data)
    conn.commit()
    conn.close()


def system_room_write(room_id, student_count, face, orientation, floor_num, apartment_name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    num = cursor.execute('select count(*) from room').fetchone()[0]
    data = (num+1, room_id, student_count, face, orientation, floor_num, apartment_name)
    cursor.execute('insert into room values (?,?,?,?,?,?,?)', data)
    conn.commit()
    conn.close()


def system_class_write(class_num, class_name, profession, grade, department_name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (class_num, class_name, profession, grade, department_name)
    cursor.execute('insert into class values (?,?,?,?,?)', data)
    conn.commit()
    conn.close()


def system_department_write(department_name, department_leader):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    num = cursor.execute('select count(*) from department').fetchone()[0]
    data = (num+1, department_name, department_leader)
    cursor.execute('insert into department values (?,?,?)', data)
    conn.commit()
    conn.close()


def system_apartment_delete(ID):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('delete from apartment where apartment_id = ?;', (ID,))
    conn.commit()
    conn.close()


def system_room_delete(ID):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('delete from room where room_id = ?;', (ID,))
    conn.commit()
    conn.close()


def system_class_delete(ID):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('delete from class where class_num = ?;', (ID,))
    conn.commit()
    conn.close()


def system_department_delete(ID):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('delete from department where department_num = ?;', (ID,))
    conn.commit()
    conn.close()
