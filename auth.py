# pip install -i https://pypi.douban.com/simple pycryptodomex
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