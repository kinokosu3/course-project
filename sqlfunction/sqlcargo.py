import sqlite3


def cargo_re(ID, cargo_id, time, origin, direction, duty_man):
    conn = sqlite3.connect('main.db')
    data = (ID, cargo_id, time, origin, direction, duty_man)
    cursor = conn.cursor()
    cursor.execute('''
        insert into cargo_register values (?,?,?,?,?,?);
    ''', data)
    conn.commit()
    conn.close()

