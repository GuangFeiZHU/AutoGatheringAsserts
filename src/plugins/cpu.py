import os
from config.settings import BASEDIR

class CPU():
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        '定义一个钩子'
        return cls()

    def process(self, cmd_func,debug):
        if debug:
            file_path_cpu = os.path.join(BASEDIR, 'files', 'cpuinfo.out')
            f = open(file_path_cpu, 'r',encoding='utf-8')
            out_put=f.read()
        else:
            out_put=cmd_func('cat /proc/cpuinfo')
        return self.parse(out_put)

    def parse(self,content):
        response = {'cpu_count': 0, 'cpu_physical_count': 0, 'cpu_model': ''}
        cpu_physical_set=set()
        for item in content.split('\n'):
            item_list = item.split(':')
            if item_list[0] == 'processor\t':
                response['cpu_count'] += 1
            elif item_list[0] == 'physical id\t':
                cpu_physical_set.add(item_list[1])            #使用集合去重，获取CPU physical
            elif item_list[0] == 'model name\t':
                if not response['cpu_model']:
                    response['cpu_model'] = item_list[1]
            response['cpu_physical_count'] = len(cpu_physical_set)
        return response



