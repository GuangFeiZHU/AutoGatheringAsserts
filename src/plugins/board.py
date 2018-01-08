#获取主板信息
import os
from config.settings import BASEDIR

class Board():
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self,cmd_func,debug):
        if debug:
            file_path_board = os.path.join(BASEDIR, 'files', 'board.out')
            f = open(file_path_board, 'r',encoding='utf-8')
            out_put = f.read()
        else:
            out_put=cmd_func("sudo dmidecode -t1")
        return self.parase(out_put)

    def parase(self,content):
        content_list = content.split('\n')
        response_dict = {}
        pattern = {'Manufacturer':'manufacturer', 'Product Name':'model', 'Serial Number':'sn'}
        for board_item in content_list[4:]:
            board_item_list = board_item.split(':')
            if board_item_list[0].strip() in pattern:
                response_dict[pattern[board_item_list[0].strip()]] = board_item_list[1].strip()
        return response_dict