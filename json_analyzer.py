import json
import os
os.chdir(r"C:\Users\dell\Desktop\ATMobile2020-1\jsons")
filedir = r"C:\Users\dell\Desktop\ATMobile2020-1\jsons"
f = open('1.json', 'r')
res = f.read()
datum = json.loads(res)
# 递归解析json
def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '
​
    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
​
    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
​
​
    return tmp_list
​
​
def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):  
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身
# reslist = []
# Rid_value = get_target_value('resource-id', datum, reslist)
# filed = filedir + '/' + '1'
# os.mkdir(filed)
# newDir = filed + '/' + 'res.txt'
# with open(newDir, 'w') as f:
    # f.write(str(Rid_value))
    # f.close()
filenames = os.listdir(filedir)
for filename in filenames:
    filepath = filedir + '/' + filename
    with open(filepath, 'r') as file:
        data = json.load(file)
        reslst = []
        res = get_target_value('resource-id', data, reslst)
        # print(res)
        # print("本json文件解析完成")
        filedi = filedir + '/' + os.path.splitext(filename)[0]
        os.mkdir(filedi)
        newDir = filedi + '/' + 'res.txt'
        with open(newDir, 'w') as f:
            f.write(str(res))
            f.close()
