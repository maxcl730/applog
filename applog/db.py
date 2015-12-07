# coding=utf-8
# __author__ = 'chengliang'
import pymysql


def db_conn():
    conn = pymysql.connect(host='192.168.1.245', port=3306, user='ipad', passwd='Zaq1xsw@', db='app_action',charset='utf8')
    return conn


def db_InsertData(conn,header,values):
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO app_user_behavior(" + header + ") VALUES (" + values + ")"
            #print(sql)
            cur.execute(sql)
        conn.commit()
    finally:
        cur.close()


def db_close(conn):
    conn.close()
