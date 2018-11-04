# pip install -i https://pypi.douban.com/simple pycryptodomex
import sqlite3


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
                              hash int primary key not null,
                              id_num int not null,
                              name TEXT not null,
                              location TEXT,
                              visit_time TEXT not null,
                              quit_time TEXT
        );
    ''')

    conn.commit()
    conn.close()


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


# 学生管理
def student_manage():
    pass

