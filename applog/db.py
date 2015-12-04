# coding=utf-8
# __author__ = 'chengliang'
import pymysql


def db_conn():
    conn = pymysql.connect(host='192.168.1.245', port=3306, user='ipad', passwd='Zaq1xsw@', db='app_action')
    cur = conn.cursor()
    cur.execute("desc app_user_behavior")
    #cur.execute("insert")
    #conn.commit()
    for r in cur:
        print(r)
    cur.close()
    conn.close()
