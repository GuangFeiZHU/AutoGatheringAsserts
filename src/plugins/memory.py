import os
from config.settings import BASEDIR
class Memory():

    def __init__(self):
        pass

    @classmethod
    def initial(cls):
         return cls()

    def process(self,cmd_func,debug):
        if debug:
            file_path_memory = os.path.join(BASEDIR, 'files', 'memory.out')
            f = open(file_path_memory, 'r',encoding='utf-8')
            out_put = f.read()
        else:
            out_put=cmd_func("sudo dmidecode  -q -t 17 2>/dev/null")
        return self.parase(out_put)


    def parase(self,content):
        content_list = content.split('\n\n')
        response_dict = {}
        pattern = {'Size':'size', 'Type':'model', 'Speed':'speed', 'Manufacturer':'manufacturer', 'Serial Number':'sn'}
        for memory_item in content_list:
            tem_dict = {}
            for sub_item in memory_item.split('\n'):
                if sub_item.strip() == 'Memory Device':
                    continue
                sub_item_list = sub_item.split(':')
                if sub_item_list[0].strip() == 'Locator':
                    response_dict[sub_item_list[1].strip()] = tem_dict
                    tem_dict['slot'] = sub_item_list[1].strip()
                elif sub_item_list[0].strip() in pattern:
                    tem_dict[pattern[sub_item_list[0].strip()]] = sub_item_list[1].strip()
        return response_dict