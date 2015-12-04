# coding=utf-8
# __author__ = 'chengliang'
import sys
# from pprint import pprint
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

    def __init__(self, **actions_dict):
        for json_data_key in self.__json_data_info:
            if json_data_key in actions_dict.keys():
                exec('self.'+self.__json_data_info[json_data_key]+'="'+actions_dict[json_data_key]+'"')

    def __repr__(self):
        user_info = '<User info [AppName:%r, Uuid:%r, IPAdd:%r, AppEdition:%r, AccessType:%r, PassportId:%r,' \
                    ' MobType:%r, MobOS:%r, AppStore:%r, GeoLoc:%r]>]' % (self.AppName, self.Uuid, self.IPAdd,
                                                                          self.AppEdition, self.AccessType,
                                                                          self.PassportId, self.MobType, self.MobOS,
                                                                          self.AppStore, self.GeoLoc)
        return user_info


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

    def __init__(self, **actions_dict):
        UserInfo.__init__(self, **actions_dict)
        if self.__action_tag in actions_dict.keys():
            for action_dict in actions_dict[self.__action_tag]:
                for action_key in action_dict:
                    self.__action[self.__json_data_action[action_key]] = action_dict[action_key]
                self.Actions.append(self.__action)

    def __repr__(self):
        user_info = '\n<User info \n[AppName:%r, Uuid:%r, IPAdd:%r, AppEdition:%r, AccessType:%r, PassportId:%r, ' \
                    'MobType:%r, MobOS:%r, AppStore:%r, GeoLoc:%r]>' % (self.AppName, self.Uuid, self.IPAdd,
                                                                        self.AppEdition, self.AccessType,
                                                                        self.PassportId, self.MobType, self.MobOS,
                                                                        self.AppStore, self.GeoLoc)
        user_actions = '\n<User actions \n'
        for action in self.Actions:
            user_actions += '['
            for action_key in sorted(action):
                user_actions = user_actions + action_key + ":'" + action[action_key] + "',"
            user_actions += ']\n'
        user_actions += '>'
        return user_info+user_actions
