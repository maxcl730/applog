# coding=utf-8
# __author__ = 'chengliang'

from applog import logfile, user_actions
from pprint import pprint

if __name__ == "__main__":
    LOG_PATH = '/Users/chengliang/Documents/work/dev/test/log'
    #pprint(logfile.list_logfiles(LOG_PATH))
    for log_file in logfile.list_logfiles(LOG_PATH, '2015-11-27'):
        print(log_file)
        log_dict = logfile.load_logfile(log_file)
        userActions = user_actions.UserActions(**log_dict)
        #pprint(userActions.Actions)
