import sqlite3


def apartment_search(apartment_name, value):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (apartment_name,value)
    result = cursor.execute('''
        select * from apartment_manage where name = ? and value = ?;
    ''', data).fetchall()
    conn.commit()
    conn.close()
    return result


def apartment_delete():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    conn.commit()
    conn.close()
    pass


def apartment_write(ID, apartment_name, value):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (ID, apartment_name, value)
    cursor.execute('''
         insert into apartment_manage values (?,?,?);
    ''', data)
    conn.commit()
    conn.close()


