import sqlite3


def system_apartment():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    everything = cursor.execute('''
            select * from apartment;
        ''').fetchall()
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