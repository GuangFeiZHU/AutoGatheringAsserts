# 查看硬盘信息
import os
import re
from config.settings import BASEDIR


class Disk():
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self, cmd_func, debug):
        if debug:
            file_path_disk = os.path.join(BASEDIR, 'files', 'disk.out')
            f = open(file_path_disk, 'r', encoding='utf-8')
            out_put = f.read()
        else:
            out_put = cmd_func('MegaCli -PDList -aALL')
        return self.parse(out_put)

    def parse(self, content):
        content_list = content.split('\n\n')
        response_dict = {}
        for slot_item in content_list:
            if len(slot_item.strip()) < 20:
                continue
            tem_dict = {}
            for sub_item in slot_item.split('\n'):
                sub_item_list = sub_item.split(':')
                if sub_item_list[0] == 'Slot Number':
                    response_dict[sub_item_list[1]] = tem_dict
                    tem_dict['slot_number'] = sub_item_list[1]
                elif sub_item_list[0] == 'Raw Size':
                    raw_size = re.search('(\d+\.\d+)', sub_item_list[1].strip())
                    if raw_size:
                        tem_dict['capacity'] = raw_size.group()
                    else:
                        tem_dict['capacity'] = 0
                elif sub_item_list[0] == 'Inquiry Data':
                    tem_dict['inquiry_data'] = sub_item_list[1].strip()
                elif sub_item_list[0] == 'PD Type':
                    tem_dict['pd_type'] = sub_item_list[1]
        return response_dict
