#定义一个run函数，让start可执行文件执行
from lib.conf.config import settings
from src.client import SaltSSH,Agent

def run():
    if settings.MODE=='AGENT':
        obj=Agent()
    else:
        obj=SaltSSH()
    obj.execute()