import json
import os.path
from PIL import Image
import jieba
import cv2
import numpy as np
from Util.JsonUtil import *
from Util.OpenvUtil import *
from Util.StringUtil import *

# # jieba分词
# words = input("请输入要分词的句子：")
# cut_words = jieba.cut(words, cut_all=False)
# print("Default Mode: " + " ".join(cut_words))  # 精确模式
#
# # 字符去重
# words = "sdadwdfadfljukgjgJTHDawerSAFAWsfasfFFSE"
# list_words = list(words)
# set_words = set(list_words)
# print(set_words)
# sort_set = sorted(set_words)
# print(sort_set)
#
#
# # for i in range(3):
# #     print("{inter}".format(inter=" " * (3 - i)), "*" * ((i + 1) * 2 - 1))
# # for x in range(3, 0, -1):
# #     print("{inter}".format(inter=" " * (3 - x)), "*" * ((x + 1) * 2 - 1))
# # print("{inter}".format(inter=" " * 3), "*")
#
#
#
getDiamond(10)
#
# # 取最短字符
# list_word = ["nihao", "wo", "shi", "haonglinjin", "de", "sd", "ewesda"]
# min_len = 100
# min_word = ""
# for item in list_word:
#     lens = len(item)
#     if lens < min_len:
#         min_len = lens
#         min_word = item
# print(min_len)
# print(min_word)
#
# # 取最小五位
# list_word = [123, 4, 3, 34, 5, 56, 7, 567, 6, 5]
# list_word.sort()
# print(list_word[0:5])
#
# # 向文件添加字符
# file_dir = input("请输入文件路径：")
# words = input("请输入要添加的字符：")
# with open(file_dir, 'a+') as f:
#     f.writelines(words)
# with open(file_dir, 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)
#
#
# # 学生类
# class Student:
#     def __init__(self, name, age, address, no, python_score, java_score, php_score):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.no = no
#         self.python_score = python_score
#         self.java_score = java_score
#         self.php_score = php_score
#
#     # 获取总分，平均分，最高分
#     def getScore(self):
#         sum_score = self.python_score + self.java_score + self.php_score
#         av_score = sum_score / 3
#         max_score = max((self.python_score, self.java_score, self.php_score))
#         print("总分：", sum_score, "平均分：%2.1f" % av_score, "最高分：", max_score)
#
#
# student1 = Student("fbp", 23, "sda", 1312, 99, 89, 54)
# student1.getScore()
#
#
#
getStarAvatar("avatar.png").save("logo_avatar.png")
#
#
getBImage("avatar.png").save("BImage.png")
#
# from Util.OpenvUtil import *
# addLogo2Video()
#
# opencv画方形，椭圆，五角星
# img = cv2.imread("avatar.png", cv2.IMREAD_UNCHANGED)
# w, h = img.shape[0], img.shape[1]
# cv2.rectangle(img, (w // 2 - 50, h // 2 - 50), (w // 2 + 50, h // 2 + 50), color=(255, 0, 0), thickness=3)
# cv2.ellipse(img, axes=(100, 40), color=(255, 255, 0), center=(100, 100), angle=0, startAngle=0, endAngle=360,
#             thickness=3)
# lines = np.array([(170, 300), (330, 300), (200, 390), (250, 250), (300, 390)])
# cv2.polylines(img, [lines], isClosed=True, color=(255, 0, 255), thickness=2)
#
# cv2.imshow("ret_img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
addJson("json.txt", {".jk": 23, "nmb": ",b", "7856": 34})
CheckJson("json.txt")
updateJson("json.txt", {".jk": 324, "nmb": ",b54", "7856": 434})
CheckJson("json.txt")
delJson("json.txt", ".jk")
CheckJson("json.txt")
