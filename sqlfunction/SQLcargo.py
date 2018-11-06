import sqlite3


def cargo_re(ID, apartment_name,cargo_id, time, origin, direction, duty_man):
    conn = sqlite3.connect('main.db')
    data = (ID,apartment_name,cargo_id, time, origin, direction, duty_man)
    cursor = conn.cursor()
    cursor.execute('''
        insert into cargo_register values (?,?,?,?,?,?,?);
    ''', data)
    conn.commit()
    conn.close()

