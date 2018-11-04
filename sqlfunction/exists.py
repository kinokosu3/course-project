import sqlite3


def exists(data, table_name, row_name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    finish = cursor.execute('select * from '+table_name+' where '+row_name+' = ?',
                         (data, )).fetchone()
    if finish is not None:
        return True
    else:
        return False