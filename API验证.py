# API验证,作为客户端
import hashlib
import requests
import time

certi__time_key = 'dfsdfsdfsdfasdfwefewrew' + str(time.time())  # 生成动态令牌
print(certi__time_key)
hash_obj = hashlib.md5()
hash_obj.update(bytes(certi__time_key, encoding='utf-8'))
send_key = '%s|%s' % (hash_obj.hexdigest(), time.time())
print(send_key)
response = requests.get('http://127.0.0.1:8000/get_asserts/', headers={'OpenKey': send_key})
print(response.text)

api = 'http://127.0.0.1:8000/get_asserts/'


# 定义一个client端的装饰器，以便发送相应的验证数据到server端
def out_auto_api(api):
    def auto_api(func):
        def wrapper(*args, **kwargs):
            certi__time_key = 'dfsdfsdfsdfasdfwefewrew' + str(time.time())  # 生成动态令牌
            hash_obj = hashlib.md5()
            hash_obj.update(bytes(certi__time_key, encoding='utf-8'))
            send_key = '%s|%s' % (hash_obj.hexdigest(), time.time())
            response = requests.get(api, headers={'OpenKey': send_key})
            if response.text == 'false':
                raise Exception('验证不通过')
            func(*args, **kwargs)

        return wrapper

    return auto_api


# 测试一下
@out_auto_api(api)
def test():
    print('PPPPPP')


test()
