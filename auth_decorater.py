# 验证api
def api_auth(func):
    import hashlib
    from django.shortcuts import HttpResponse
    import time
    def wrapper(request, *args, **kwargs):
        receiced_key, str_time = request.META.get('HTTP_OPENKEY').split('|')
        if time.time() - float(str_time) > 10:
            return HttpResponse('false')
        certi__time_key = 'dfsdfsdfsdfasdfwefewrew' + str_time  # 生成动态令牌
        hash_obj = hashlib.md5()
        hash_obj.update(bytes(certi__time_key, encoding='utf-8'))
        already_in_dict = {}  # 维护一个只保存10秒的字典
        for key in list(already_in_dict.keys()):  # 维护一个只保存10秒的字典
            if time.time() - already_in_dict[key] > 10:
                del already_in_dict[key]
        if hash_obj.hexdigest() != receiced_key:
            return HttpResponse('false')
        if receiced_key in already_in_dict:
            return HttpResponse('false')
        already_in_dict[receiced_key] = time.time()  # 将已经进入过的加密值记录下来
        res = func(request, *args, **kwargs)
        return res

    return wrapper


api = 'http://127.0.0.1:8000/get_asserts/'

# 定义一个client端的装饰器，以便发送相应的验证数据到server端
import requests
import hashlib
import time


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

    # test()



    # def api_auth(func):
    #     import hashlib
    #     from django.shortcuts import HttpResponse
    #     import time
    #     def wrapper(request,*args,**kwargs):
    #         receiced_key, str_time = request.META.get('HTTP_OPENKEY').split('|')
    #         if time.time() - float(str_time) > 10:
    #             return HttpResponse('第一关，时间超过十秒')
    #         certi__time_key = 'dfsdfsdfsdfasdfwefewrew' + str_time  # 生成动态令牌
    #         hash_obj = hashlib.md5()
    #         hash_obj.update(bytes(certi__time_key, encoding='utf-8'))
    #         already_in_dict = {}  # 维护一个只保存10秒的字典
    #         for key in list(already_in_dict.keys()):  # 维护一个只保存10秒的字典
    #             if time.time() - already_in_dict[key] > 10:
    #                 del already_in_dict[key]
    #         if hash_obj.hexdigest() != receiced_key:
    #             return HttpResponse('第二关，md5值验证失败')
    #         if receiced_key in already_in_dict:
    #             return HttpResponse('第三关，已经有人进入过了，验证失败')
    #         already_in_dict[receiced_key] = time.time()  # 将已经进入过的加密值记录下来
    #         res=func(request,*args,**kwargs)
    #         return res
    #     return wrapper
