# coding=utf-8
# __author__ = 'chengliang'

from applog import logfile, user_actions, db
from pprint import pprint
import sys
import os
import subprocess
import signal
import threading
import time


def exec_shell_SQL_LoadData(data_file, header):
    proc = subprocess.Popen(["/bin/sh" + os.getcwd() + "/sql.sh " + data_file + header ], shell = True, stdout = subprocess.PIPE)
    script_response = proc.stdout.read()
    print("Shell_subprocess load data: " + script_response)


def myhandle(signalNun, currentStackFrame):
    print("%s exit (%d)." % (sys.argv[0], signalNun))
    sys.exit(0)


def process_applog(log_file,fp):
    log_dict = logfile.load_logfile(log_file)
    userActions_obj = user_actions.UserActions(log_dict)
    if userActions_obj.checkAvailable():
        return False
    dbconn = db.db_conn()
    for action_line in userActions_obj.actionsFormat():
        fp.write(action_line+'\n')
        if DB_OPT == 'insert':
            print("insert data: " + action_line)
            db.db_InsertData(dbconn,action_Header, action_line)
    db.db_close(dbconn)
    fp.flush()
    logfile.logfile_rename(log_file)

DT = sys.argv[1]
LOG_PATH = '/Users/chengliang/Documents/work/dev/test/log'
DB_OPT = sys.argv[2]
if len(sys.argv) > 3:
    LOG_PATH = sys.argv[3]
DAY_LOG_PATH = LOG_PATH + '/day'
DATA_FILE = DAY_LOG_PATH + '/applog_' + DT + '.log'

threads = []
t = threading

if __name__ == "__main__":
    signal.signal(signal.SIGINT, myhandle)
    if not os.path.isdir(DAY_LOG_PATH):
        os.mkdir(DAY_LOG_PATH)
    userActions = user_actions.UserActions()
    action_Header = userActions.actionHeader()
    fp = open(DATA_FILE, 'w')
    fp.write(action_Header +'\n')
    print(int(time.time()))
    for log_file in logfile.list_logfiles(LOG_PATH, DT):
        #print(log_file)
        threads.append(threading.Thread(target=process_applog, args=(log_file, fp)))
        if len(threads) >= 5:
            for t in threads:
                t.setDaemon(True)
                t.start()
            t.join()
            threads = []
        #process_applog(log_file, fp)
    if len(threads) > 0:
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()
    fp.close()
    print(int(time.time()))
    if DB_OPT == 'loaddata':
        exec_shell_SQL_LoadData(DATA_FILE, action_Header)
