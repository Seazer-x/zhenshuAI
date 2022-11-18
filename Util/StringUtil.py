import string
import random

rint = random.randint


# 生成随机字符串
def getRandomStr(num=4, digits=True, letters=True):
    str_all = ""  # 初始化字符串
    if num > 63:
        raise Exception("只能生成63位以下的随机字符")
    if digits:  # 包含数字
        str_all += string.digits
    if letters:  # 包含字母
        str_all += string.ascii_letters
    if not digits and not str_all:
        print("至少选择一类字符")
        return
    str_list = list(str_all)
    random.shuffle(str_list)
    return "".join(str_list[0:num])


# 生成随机字体颜色
def getFontColor():
    return rint(120, 240), rint(120, 240), rint(120, 240)


# 生成随机背景颜色
def getBackColor():
    return rint(120, 240), rint(120, 240), rint(120, 240)


# 字符钻石
def getDiamond(num=3):
    num = num * 2 + 1
    for loc in range(num):
        threshold = num // 2
        if loc < threshold:
            print(("*" * ((loc + 1) * 2 - 1)).center(num))
        else:
            print(("*" * ((num - loc) * 2 - 1)).center(num))
