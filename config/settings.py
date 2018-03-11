# 配置文件---用户自定义配置文件
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

PLUGINS_DICT = {
    'basic': 'src.plugins.basic.Basic',
    'board': 'src.plugins.board.Board',
    'cpu': 'src.plugins.cpu.CPU',
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.Nic',

}
CERT_PATH = os.path.join(BASEDIR, 'files\cert_file')

MODE = "AGENT"
HOSTNAME = 'root'
PASSWORD = 'woaini520'
PORT = 22
API = ' http://127.0.0.1:8000/get_asserts/'
USERNAME = 'root'
