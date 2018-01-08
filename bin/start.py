#可执行文件
import os
os.environ['USER_SETTINGS']='config.settings'

from src.script import run

if __name__ == '__main__':
    run()