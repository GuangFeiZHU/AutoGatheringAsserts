import re
import os

from config import settings

print(settings.BASEDIR)
# 测试CPU
# now_path=os.path.abspath(__file__)
# file_path_cpu=os.path.join(os.path.dirname(now_path),'files','cpuinfo.out')
# f=open(file_path_cpu,'r')
# file_list=f.read().split('\n')
# response = {'cpu_count': 0, 'cpu_physical_count': 0, 'cpu_model': ''}
# for item in file_list:
#     item_list=item.split(':')
#     if item_list[0]=='processor\t':
#         response['cpu_count']+=1
#     elif item_list[0]=='physical id\t':
#         response['cpu_physical_count']+=1
#     elif item_list[0]=='model name\t':
#         if not response['cpu_model']:
#             response['cpu_model']=item_list[1]

# 测试disk
# des={'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
#
# now_path=os.path.abspath(__file__)
# file_path_cpu=os.path.join(os.path.dirname(now_path),'files','disk.out')
# f=open(file_path_cpu,'r')
# file_list=f.read().split('\n\n')
# response_dict={}
# for slot_item in file_list:
#     if len(slot_item.strip())<20:
#         continue
#     tem_dict={}
#     for sub_item in slot_item.split('\n'):
#         print(sub_item)
#         sub_item_list=sub_item.split(':')
#         if sub_item_list[0]=='Slot Number':
#             response_dict[sub_item_list[1]]=tem_dict
#             tem_dict['Slot Number']=sub_item_list[1]
#         elif sub_item_list[0]=='Raw Size':
#            raw_size=re.search('(\d+\.\d+)',sub_item_list[1].strip())
#            if raw_size:
#                tem_dict['capacity']=raw_size.group()
#            else:
#                tem_dict['capacity']=0
#         elif sub_item_list[0]=='Inquiry Data':
#             tem_dict['Inquiry Data']=sub_item_list[1].strip()
#         elif sub_item_list[0]=='PD Type':
#             tem_dict['PD Type']=sub_item_list[1]
# print(response_dict)

# #测试memory
# key_map = {
#     'Size': 'capacity','Locator': 'slot','Type': 'model','Speed': 'speed','Manufacturer': 'manufacturer',  'Serial Number': 'sn'
# }
# now_path=os.path.abspath(__file__)
# file_path_cpu=os.path.join(os.path.dirname(now_path),'files','memory.out')
# f=open(file_path_cpu,'r')
# file_list=f.read().split('\n\n')
# response_dict={}
# pattern=['Size','Type','Speed','Manufacturer','Serial Number']
# for memory_item in file_list:
#     tem_dict = {}
#     for sub_item in memory_item.split('\n'):
#         if sub_item.strip()=='Memory Device':
#             continue
#         sub_item_list=sub_item.split(':')
#         if sub_item_list[0].strip()=='Locator':
#             response_dict[sub_item_list[1].strip()]=tem_dict
#             tem_dict['Locator']=sub_item_list[1].strip()
#         elif sub_item_list[0].strip() in pattern:
#             tem_dict[sub_item_list[0].strip()]=sub_item_list[1].strip()
#
# print(response_dict,'----')

# key_map = {
#     'Manufacturer': 'manufacturer',
#     'Product Name': 'model',
#     'Serial Number': 'sn',
# }
#
# now_path=os.path.abspath(__file__)
# file_path_cpu=os.path.join(os.path.dirname(now_path),'files','board.out')
# f=open(file_path_cpu,'r')
# file_list=f.read().split('\n')
# response_dict={}
# pattern=['Manufacturer','Product Name','Serial Number']
# for board_item in file_list[4:]:
#     board_item_list=board_item.split(':')
#     if board_item_list[0].strip() in pattern:
#         response_dict[board_item_list[0].strip()]= board_item_list[1].strip()
#
# print(response_dict,'----')
