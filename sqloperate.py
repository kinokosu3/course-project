import sqlite3
from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex


def load_logged_in(user_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    user = cursor.execute('''select * from user where username=?''', ('root',)).fetchone()
    conn.commit()
    conn.close()
    return user[0]


def create():
    conn = sqlite3.connect('main.db')

    cursor = conn.cursor()
    # 创建公寓
    cursor.execute('''
                        create table apartment(apartment_id INT PRIMARY KEY NOT NULL,
                                             apartment_name TEXT NOT NULL,
                                             apartment_dir  TEXT NOT NULL,
                                             floor int NOT null);
    ''')

    # 创建楼层

    cursor.execute('''
            create table floor(floor_id int primary key not null,
                               floor_num int not null,
                               room_num int not null
            );
    ''')
    # 创建宿舍
    cursor.execute('''
                create table room(id int primary key not null,
                                   room_id int primary key not null,
                                   student_count int not null,
                                   face TEXT not null,
                                   orientation text not null,
                                   floor_num int,
                                   foreign key(floor_num)
                                   references floor(floor_num)
                );
        ''')
    # 学生
    cursor.execute('''
                    create table student(student_num int primary key not null,
                                       name TEXT not null,
                                       gender TEXT not null,
                                       stay_time TEXT not null,
                                       room_id int,
                                       class_num int,
                                       department_name TEXT,
                                       foreign key (department_name)
                                       references department(department_num)
                                       foreign key (class_num)
                                       references class(class_num)
                                       foreign key (room_id)
                                       references room(room_id)
                    );
            ''')
    #
    # # 班级
    #
    cursor.execute('''
                        create table class(class_num int primary key not null,
                                           class_name TEXT not null,
                                           profession TEXT not null,
                                           grade TEXT not null,
                                           department_name TEXT,
                                           foreign key (department_name)
                                           references department(department_name)

                        );
                ''')

    # 院系

    cursor.execute('''
                            create table department(department_num int not null,
                                               department_name TEXT primary key not null,
                                               department_leader TEXT not null
                            );
                    ''')

    # 登记 cargo_register
    cursor.execute('''
        create table cargo_register(id int primary key not null,
                              cargo_id int not null,
                              time TEXT not null,
                              origin TEXT not null,
                              direction TEXT not null,
                              duty_man TEXT not null
        );
    ''')
    # # 公寓管理(财产)
    #
    cursor.execute('''
            create table apartment_manage(
                                      id int primary key not null,
                                      name TEXT not null,
                                      value TEXT not null
            );
    ''')
    #
    # 来访登记
    cursor.execute('''
        create table visit_register(
                              id int primary key not null,
                              name TEXT not null,
                              location TEXT,
                              visit_time TEXT not null,
                              quit_time TEXT not null
        );
    ''')

    conn.commit()
    conn.close()


def encryption(password, status):
    def pad(text):
        while len(text) % 16 != 0:
            text += ' '
        return text

    def pad_key(key):
        while len(key) % 16 != 0:
            key += ' '
        return key
    key = 'huangtingfeng'
    aes = AES.new(pad_key(key).encode(), AES.MODE_ECB)
    if status == 'add':
        encrypted_text = aes.encrypt(pad(password).encode())
        encrypted_text_hex = b2a_hex(encrypted_text)
        text = encrypted_text_hex.decode('utf-8')

        return text
    if status == 'decode':
        password = password.encode('utf-8')
        password = str(aes.decrypt(a2b_hex(password)), encoding='utf-8', errors="ignore").strip()
        return password


def auth(username, password, status):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    user = cursor.execute('''
                select * from user where username = ?
            ''', (username,)).fetchone()
    if status == 'username if have':
        if user is not None:
            print('user have')
            conn.commit()
            conn.close()
            return 'User {} is already registered'.format(username,)
        else:
            conn.commit()
            conn.close()
            return None
    elif status == 'registered':
        password = encryption(password, status='add')
        cursor.execute('''
            insert into user (username, password) values (?, ?)
        ''', (username, password))
        conn.commit()
        conn.close()
    elif status == 'verify':
        pwd = encryption(user[-1], status='decode')
        if pwd != password:
            conn.commit()
            conn.close()
            return None
        else:
            conn.commit()
            conn.close()
            return True

# 查询函数
def search():
    pass


# 分配寝室
def room_allocation():
    pass


# 信息查询
def information_search():
    pass


# 财产管理
def property_manage():
    pass


# 出入登记：外来人员
def outside_man(id, name, location, visit_time, quit_time):

    conn = sqlite3.connect('main.db')
    data = (id, name, location, visit_time, quit_time)
    cursor = conn.cursor()
    cursor.execute('''
        insert into visit_register values (?,?,?,?,?);
    ''', data)


# 货物
def cargo(id, cargo_id, time, origin, direction, duty_man):
    conn = sqlite3.connect('main.db')
    data = (id, cargo_id, time, origin, direction, duty_man)
    cursor = conn.cursor()
    cursor.execute('''
        insert into cargo_register values (?,?,?,?,?,?);
    ''', data)
    conn.commit()
    conn.close()

# 学生管理
def student_manage():
    pass


if __name__ == '__main__':

    auth('roo', '123')