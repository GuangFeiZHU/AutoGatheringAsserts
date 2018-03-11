# 提交数据到api的方法
import requests
from src.plugins import PluginManage
from lib.conf.config import settings
from concurrent.futures import ThreadPoolExecutor


class Base():  # 通用的提交数据到API的方法
    def post_data(self, server_info):
        print(server_info, 'server_info-----')
        requests.post(settings.API, json=server_info)


class Agent(Base):
    '以agent方式提交数据到api'

    def execute(self):
        server_info = PluginManage().exec_plugins()
        # 如果是Agent模式，会出现一个唯一标识的问题，将主机名作为唯一标识，会在装机时建立
        hostname = server_info['basic']['data']['hostname']
        certname = open(settings.CERT_PATH, 'r', encoding='utf-8').read().strip()
        if not certname:
            with open(settings.CERT_PATH, 'w', encoding='utf-8') as f:
                f.write(hostname)
        else:
            server_info['basic']['data']['hostname'] = certname
        self.post_data(server_info)


class SaltSSH(Base):
    def get_hostnames(self):
        '获取没有被采集的主机的列表'
        import json
        host_names = requests.get(settings.API)
        result = json.loads(host_names.text)  # "{status:'True',data: ['c1.com','c2.com']}"
        if not result['status']:
            return
        return result['data']

    # def execute(self):
    #     for host in self.get_hostnames():   #循环没有被采集的主机，将采集信息上抛
    #         server_info=PluginManage(hostname=host).exec_plugins()
    #         self.post_data(server_info)

    # 开启多线程采集数据，agent模式不需要
    def run(self, host):
        server_info = PluginManage(hostname=host).exec_plugins()
        self.post_data(server_info)

    def execute(self):
        p = ThreadPoolExecutor(10)
        for host in self.get_hostnames():
            p.submit(self.run, host)
