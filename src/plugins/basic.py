
class Basic():
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        '定义一个钩子'
        return cls()
    def process(self,cmd_func,debug):
        if debug:
            out_put = {
                'os_platform': "linux",
                'os_version': "CentOS release 6.6 (Final)\nKernel \r on an \m",
                'hostname': 'c1.com'
            }
        else:
            out_put={
                'os_platform':cmd_func('uname'),
                'os_version':cmd_func('cat /etc/issue').strip().split('\n')[0],
                'hostname':cmd_func('hostname').strip()
            }
        return out_put

