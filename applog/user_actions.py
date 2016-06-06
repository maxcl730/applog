# coding=utf-8
# __author__ = 'chengliang'
import sys
from applog import APP_VERSIONS
from pprint import pprint
reload(sys)
sys.setdefaultencoding('utf-8')


class UserInfo:
    AppName = ''
    Uuid = ''   # udid
    IPAdd = ''
    AppEdition = ''  # App版本
    AccessType = ''  # 网络类型(apn)
    PassportId = ''
    MobType = ''   # 手机型号
    MobOS = ''    # 系统及版本
    AppStore = ''   # market
    GeoLoc = ''  # 地理位置
    __json_data_info = {'appName': 'AppName',
                        'udid': 'Uuid',
                        'ip': 'IPAdd',
                        'appVersion': 'AppEdition',
                        'apn': 'AccessType',
                        'passportId': 'PassportId',
                        'model': 'MobType',
                        'os': 'MobOS',
                        'market': 'AppStore',
                        }

    def __init__(self, actions_dict = dict()):
        for json_data_key in self.__json_data_info:
            if json_data_key in actions_dict.keys():
                exec('self.'+self.__json_data_info[json_data_key]+'="'+actions_dict[json_data_key]+'"')

    def checkAvailable(self):
        if self.__json_data_info['appName'].upper() + '|' + self.__json_data_info['appVersion'].upper() in APP_VERSIONS:
            return True
        else
            return False

    def infoFormat(self):
        format_info = ''
        for key in sorted(self.__json_data_info):
            format_info += "'" + eval('self.'+self.__json_data_info[key]) + "',"
        return format_info[:-1]

    def infoHeader(self):
        info_header = ''
        for key in sorted(self.__json_data_info):
            info_header += self.__json_data_info[key] + ','
        return info_header[:-1]


class UserActions(UserInfo):
    Actions = list()
    __action_tag = 'body'
    __action = dict()
    __json_data_action = {'action': 'Action',
                          'category': 'Category',
                          'label': 'Label',
                          'uri': 'URI',
                          'clientTime': 'AccessDate',
                          'value': 'Value'
                          }

    def __init__(self, actions_dict = dict()):
        UserInfo.__init__(self, actions_dict):
        self.Actions = list()
        if self.__action_tag in actions_dict.keys():
            for action_dict in actions_dict[self.__action_tag]:
                for action_key in action_dict:
                    self.__action[self.__json_data_action[action_key]] = action_dict[action_key]
                self.Actions.append(self.__action)
                self.__action = dict()
        return True

    def actionsFormat(self):
        format_actions_list = list()
        format_info = UserInfo.infoFormat(self)
        for action in self.Actions:
            user_actions = ''
            for action_key in sorted(self.__json_data_action):
                if self.__json_data_action[action_key] in action:
                    if action_key == 'clientTime':
                        user_actions += action[self.__json_data_action[action_key]] + ","
                    else:
                        user_actions += "'" + action[self.__json_data_action[action_key]].decode() + "',"
                else:
                    if action_key == 'clientTime':
                        user_actions += ","
                    else:
                        user_actions += "'',"
            format_actions_list.append(format_info + ',' + user_actions[:-1])
        return format_actions_list

    def actionHeader(self):
        action_header = UserInfo.infoHeader(self) + ','
        for key in sorted(self.__json_data_action):
            action_header += self.__json_data_action[key] + ','
        return action_header[:-1]
