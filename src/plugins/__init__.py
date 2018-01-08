
import importlib
from lib.conf.config import settings
import traceback

class PluginManage():
    '插件管理'
    def __init__(self,hostname=None):
        self.hostname=hostname
        self.debug=settings.DEBUG
        self.plugin_dict=settings.PLUGINS_DICT
        self.mode=settings.MODE
        if self.mode=='SSH':
            self.hostname=hostname
            self.username=settings.USERNAME
            self.password=settings.PASSWORD
            self.port=settings.PORT
    def exec_plugins(self):
        response={}
        for key,value in self.plugin_dict.items():
            ret = {'status': True, 'data': None}
            try:
                module_path,class_name=value.rsplit('.',1)
                m=importlib.import_module(module_path)
                cls=getattr(m,class_name)     #获取类名
                if hasattr(cls,'initial'):
                    obj=cls.initial()
                else:
                    obj=cls()
                result=obj.process(self.command,self.debug)           #执行类的process方法，去获取资产采集结果
                ret['data']=result
            except Exception as e:
                ret['status']=False
                ret['data'] = "[%s][%s] 采集数据出现错误 : %s" % (
                self.hostname if self.hostname else "AGENT", key, traceback.format_exc())
            response[key]=ret
        return response
    def command(self,cmd):
        if self.mode=='AGENT':
            self.__agent(cmd)
        elif self.mode=='SSH':
            self.__ssh(cmd)
        elif self.mode=='SALT':
            self.__salt(cmd)
        else:
            raise Exception('只有三种模式，AGENT/SSH/SALT')

    def __agent(self,cmd):   #如果是agent方式，说明本软件部署在服务器上，直接执行subprocess
        import subprocess
        result=subprocess.getoutput(cmd)
        return result
    def __ssh(self,cmd):
        import paramiko
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=self.hostname,password=self.password,username=self.username,port=self.port)
        stdin, stdout, stderr=ssh.exec_command(cmd)
        result=stdout.read()
        ssh.close()
        return result
    def __salt(self,cmd):
        #由于salt的python代码支持py3不好，故使用paramiko模块执行salt命令
        import subprocess
        salt_cmd = "salt '%s' cmd.run '%s'" % (self.hostname, cmd,)
        result=subprocess.getoutput(salt_cmd)
        return result




