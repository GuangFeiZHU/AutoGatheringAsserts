# 配置信息---将用户自定义配置文件及默认配置文件合成一个

import importlib
import os
from lib.conf import global_settings


class Settings():
    def __init__(self):
        # 获取默认配置文件的内容写入到Settings类的名称空间
        for name in dir(global_settings):
            if name.isupper():
                value = getattr(global_settings, name)
                setattr(self, name, value)
        # 获取用户自定义配置的文件内容，写入到Settings类的名称空间
        user_settings = os.environ.get('USER_SETTINGS')
        if not user_settings:
            return
        # m = importlib.import_module('config.settings')
        m = importlib.import_module('config.settings')
        for name in dir(m):
            if name.isupper():
                value = getattr(m, name)
                setattr(self, name, value)


settings = Settings()
