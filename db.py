import mysql.connector
import iniconfig

ini = iniconfig.IniConfig('./config.ini')

conn = mysql.connector.connect(
        host=ini['DEFAULT']['DBHost'],
        user=ini['DEFAULT']['DBUser'],
        password=ini['DEFAULT']['DBPasswd'],
        db='flask')


def get():
    cur = conn.cursor(dictionary=True)
    cur.execute('SELECT * FROM test_tb')
    datas = cur.fetchall()
    cur.close()
    return datas


def post(text):
    cur = conn.cursor()
    cur.execute('SELECT MAX(id) FROM test_tb')
    _id = cur.fetchone()
    if _id[0] != None:
        _id = int(_id[0]) + 1
    else:
        _id = 1
    cur.execute('INSERT INTO test_tb VALUE ({}, "{}")'.format(_id, text))
    conn.commit()
    cur.close()
