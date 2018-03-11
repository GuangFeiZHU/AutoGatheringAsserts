from crypto.Cipher import AES


def encrypt(data):
    """
    将明文数据进行加密
    :param data: 需要被加密的内容
    :return:加密后的数据
    """
    key = b'qwertyuioplkjhgfdsazxcvbnm'
    bytes_data = bytearray(data, encoding='utf-8')
    l1 = len(bytes_data)
    l2 = l1 % 16  # 获取需要补充在bytes_data后面的数据，并用不足的数据进行填充
    if l2 == 0:
        l3 = 16
    else:
        l3 = 16 - l2
    for i in range(l3):
        bytes_data.append(l3)  # 填充数据
    cipher = AES.new(key, AES.MODE_CBC, key)  # 实例化一个加密对象
    encrypt_data = cipher.encrypt(bytes_data)  # 被加密的数据必须是16的倍数
    return encrypt_data


def decrypt(encrypt_data):
    '''
    将数据进行解密成明文
    :param encrypt_data: 被加密的文件
    :return:明文数据
    '''
    key = b'qwertyuioplkjhgfdsazxcvbnm'
    cipher = AES.new(key, AES.MODE_CBC, key)
    decrypt_result = cipher.decrypt(encrypt_data)  # 获取解密的结果
    decrypt_data = decrypt_result[0:-decrypt_result[-1]]  # 获取最终的数据，-decrypt_result[-1] 表示获取到最后填充数据的数字
    return decrypt_data
