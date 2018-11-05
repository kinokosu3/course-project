import sqlite3


def apartment_search(apartment_name, name,value):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (name,value,apartment_name)
    result = cursor.execute('''
        select * from apartment_manage where name = ? and value = ? and apartment_name=?;
    ''', data).fetchall()
    conn.commit()
    conn.close()
    return result


def apartment_delete(ID):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('''
        delete from apartment_manage where ID = ?;
    ''', (ID,))
    conn.commit()
    conn.close()


def apartment_write(ID, name, apartment_name, value):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    data = (ID, name, value, apartment_name)
    cursor.execute('''
         insert into apartment_manage values (?,?,?,?);
    ''', data)
    conn.commit()
    conn.close()


def apartment_everything():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    everything = cursor.execute('''
        select * from apartment_manage;
    ''').fetchall()
    conn.commit()
    conn.close()
    return everything
