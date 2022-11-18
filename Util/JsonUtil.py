import json
import os


# 查看json文本
def CheckJson(json_path):
    if not os.path.exists(json_path):
        print("文件不存在")
        return
    json_str = ""
    with open(json_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            json_str += line
    print(json_str)


# 为json文本添加键值对
def addJson(json_path, json_dict: dict):
    if os.path.exists(json_path):
        json_str = ""
        json_ex = []
        with open(json_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                json_str += line
            json_data = dict(json.loads(json_str))
            for i in json_dict.keys():
                if i in json_data.keys():
                    json_ex.append(i)
                    print(i + " 已存在")
            for item in json_ex:
                json_dict.pop(item)
                print(item, "已剔除")
            for k, v in json_dict.items():
                json_data[k] = v
    else:
        json_data = json_dict
    with open(json_path, "w") as f:
        f.write(json.dumps(json_data, ensure_ascii=False, indent=2, sort_keys=True))
    print("添加成功")


# 将json文本中指定的key删除
def delJson(json_path, json_key):
    if not os.path.exists(json_path):
        print("不存在此文件。。。")
        return
    json_str = ""
    with open(json_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            json_str += line
    json_data = dict(json.loads(json_str))
    if json_key in json_data.keys():
        json_data.pop(json_key)
    else:
        print("不存在此Key")
        return
    with open(json_path, 'w') as f:
        f.write(json.dumps(json_data, ensure_ascii=False, indent=2, sort_keys=True))
    print("删除成功")


# 更新json文本
def updateJson(json_path, json_dict: dict, add_ex=True):
    """
    :param json_path: json文件路径
    :param json_dict: 要更新的json字典
    :param add_ex: 是否添加json文本中不存在的json_dict
    :return: None
    """
    if os.path.exists(json_path):
        json_str = ""
        with open(json_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                json_str += line
            json_data = dict(json.loads(json_str))
            for i in json_dict.keys():
                if i in json_data.keys():
                    json_data[i] = json_dict[i]
                    print(i + " 已修改")
                else:
                    if add_ex:
                        json_data[i] = json_dict[i]
                        print(i + " 已添加")
    else:
        print("文件不存在")
        return
    with open(json_path, "w") as f:
        f.write(json.dumps(json_data, ensure_ascii=False, indent=2, sort_keys=True))
    print("修改成功")
