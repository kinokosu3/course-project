import sqlite3


def quit_list():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    ql = cursor.execute('''
        select hash,id_num,name,location,visit_time from visit_register where quit_time == 'NULL';
    ''').fetchall()
    conn.commit()
    conn.close()
    return ql


def write_quit(ID, quit_time):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (quit_time, ID)
    cursor.execute('''
            update visit_register set quit_time = ? where hash = ?;
    ''', data)
    conn.commit()
    conn.close()


def search(ID):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()


def write_visit(ID, id_num, name, origin, visit_time):
    conn = sqlite3.connect('main.db')
    data = (ID, id_num, name, origin, visit_time, 'NULL')
    cursor = conn.cursor()
    cursor.execute('''
            insert into visit_register values (?,?,?,?,?,?);
        ''', data)
    conn.commit()
    conn.close()