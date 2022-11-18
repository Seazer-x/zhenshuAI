import csv

import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
matplotlib.use('tkagg')
plt.figure(figsize=(10, 5), dpi=150)
plt.style.use(['tableau-colorblind10'])
movie = ['雷神3:诸神黄昏', '正义联盟', '大耳朵图图', '误杀2', '死神', '其他']
x = movie
y = [3545, 2434, 6345, 6654, 8794, 5343]
plt.bar(x, y, width=0.5, color=['b', 'g', 'r', 'y', 'c', 'm'])
plt.savefig("1.jpg")
plt.show()
plt.close()

x = ['雷神3:诸神黄昏', '正义联盟', '大耳朵图图', '误杀2', '死神', '其他']
y = [3545, 2434, 6345, 6654, 8794, 5343]
plt.plot(x, y)
plt.savefig("2.jpg")
plt.show()
plt.close()

labels = ['美国', '中国', '英国', '法国', '荷兰']
data = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
plt.pie(x=data, labels=labels)
plt.title("国家占比分布图")
plt.savefig("3.jpg")
plt.show()
plt.close()

x = [2, 6, 8, 3, 5, 9, 3, 4]
y = [5, 3, 1, 7, 1, 2, 3, 5]
plt.scatter(x, y)
plt.savefig("4.jpg")
plt.show()
plt.close()

students = [
    {"学号": 1, "年龄": 18, "姓名": '陈聪', "性别": '男', "班级": 1, "语文": 96, "数学": 86, "英语": 35, "物理": 50},
    {"学号": 2, "年龄": 19, "姓名": '刘梅梅', "性别": '女', "班级": 2, "语文": 98, "数学": 86, "英语": 64, "物理": 60},
    {"学号": 3, "年龄": 16, "姓名": '曾令刚', "性别": '男', "班级": 3, "语文": 67, "数学": 56, "英语": 53, "物理": 63},
    {"学号": 4, "年龄": 20, "姓名": '朱恒义', "性别": '男', "班级": 4, "语文": 78, "数学": 67, "英语": 86, "物理": 61},
    {"学号": 5, "年龄": 21, "姓名": '陈欣悦', "性别": '女', "班级": 2, "语文": 89, "数学": 78, "英语": 57, "物理": 67},
    {"学号": 6, "年龄": 17, "姓名": '龚勇帆', "性别": '男', "班级": 1, "语文": 89, "数学": 45, "英语": 87, "物理": 87},
    {"学号": 7, "年龄": 17, "姓名": '余家成', "性别": '男', "班级": 2, "语文": 90, "数学": 34, "英语": 58, "物理": 78},
    {"学号": 8, "年龄": 18, "姓名": '江明泉', "性别": '男', "班级": 3, "语文": 76, "数学": 67, "英语": 97, "物理": 76},
    {"学号": 9, "年龄": 18, "姓名": '邱鑫', "性别": '男', "班级": 4, "语文": 45, "数学": 34, "英语": 75, "物理": 97},
    {"学号": 10, "年龄": 19, "姓名": '周晓宇', "性别": '男', "班级": 1, "语文": 89, "数学": 65, "英语": 64, "物理": 67},
    {"学号": 11, "年龄": 20, "姓名": '陈黄勇', "性别": '男', "班级": 2, "语文": 78, "数学": 86, "英语": 84, "物理": 56},
    {"学号": 12, "年龄": 21, "姓名": '刘星', "性别": '男', "班级": 1, "语文": 67, "数学": 97, "英语": 24, "物理": 87},
]
labels = ['男', '女']
nan = 0
nv = 0
for i in students:
    if i["性别"] == "女":
        nv += 1
    else:
        nan += 1

sex = [nan, nv]
plt.pie(x=sex, labels=labels)
plt.title("男女比例")
plt.show()
plt.close()

gre = ['优', '良', "中", "差"]
x = range(len(gre))
y = [0, 0, 0, 0]
for i in students:
    if i["语文"] >= 90:
        y[0] += 1
    elif 90 > i["语文"] >= 60:
        y[1] += 1
    elif 60 > i["语文"] >= 50:
        y[2] += 1
    elif 50 > i["语文"] > 0:
        y[3] += 1

plt.bar(gre, y, width=0.5, color=['b', 'g', 'r', 'y'])
plt.xticks(x, gre)
plt.show()
plt.close()

gre = ['一班', '二班', "三班", "四班"]
x = range(len(gre))
y = [0, 0, 0, 0]
person = [0, 0, 0, 0]
for i in students:
    if i["班级"] == 1:
        y[0] += i["语文"] + i["数学"] + i["英语"] + i["物理"]
        person[0] += 1
    elif i["班级"] == 2:
        y[1] += i["语文"] + i["数学"] + i["英语"] + i["物理"]
        person[1] += 1
    elif i["班级"] == 3:
        y[2] += i["语文"] + i["数学"] + i["英语"] + i["物理"]
        person[2] += 1
    elif i["班级"] == 4:
        y[3] += i["语文"] + i["数学"] + i["英语"] + i["物理"]
        person[3] += 1
pingjin = [0, 0, 0, 0]
for i in range(4):
    pingjin[i] = y[i] / person[i]
plt.bar(gre, pingjin, width=0.5, color=['b', 'g', 'r', 'y'])
plt.xticks(x, gre)
plt.show()
plt.close()

x = []
y = []
for i in students:
    x.append(i["语文"])
    y.append(i["英语"])
plt.scatter(x, y)
plt.xlabel("语文")
plt.ylabel("英语")
plt.show()
plt.close()

gre = [16, 17, 18, 19, 20, 21]
x = range(len(gre))
y = [0, 0, 0, 0, 0, 0]
person = [0, 0, 0, 0, 0, 0]
for i in students:
    if i["年龄"] == 16:
        y[0] += i["数学"]
        person[0] += 1
    elif i["年龄"] == 17:
        y[1] += i["数学"]
        person[1] += 1
    elif i["年龄"] == 18:
        y[2] += i["数学"]
        person[2] += 1
    elif i["年龄"] == 19:
        y[3] += i["数学"]
        person[3] += 1
    elif i["年龄"] == 20:
        y[4] += i["数学"]
        person[4] += 1
    elif i["年龄"] == 21:
        y[5] += i["数学"]
        person[5] += 1
pingjun = [0, 0, 0, 0, 0, 0]
for i in range(6):
    pingjun[i] = y[i] / person[i]
plt.plot(gre, pingjun)
plt.xlabel("年龄")
plt.ylabel("平均分")
plt.show()
plt.close()

gre = [16, 17, 18, 19, 20, 21]
x = range(len(gre))
ydit = dict({})
person = dict({})
for i in students:
    if ydit.get(str(i["年龄"])):
        ydit[str(i["年龄"])] += i["数学"]
        person[str(i["年龄"])] += 1
    else:
        ydit[str(i["年龄"])] = i["数学"]
        person[str(i["年龄"])] = 1
pingjun = [0, 0, 0, 0, 0, 0]
for index, i in enumerate(["16", "17", "18", "19", "20", "21"]):
    pingjun[index] = ydit[i] / person[i]
plt.plot(gre, pingjun)
plt.xlabel("年龄")
plt.ylabel("平均分")
plt.show()
plt.close()

headrs = list(students[0].keys())
with open('student.csv', 'w+', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headrs)
    writer.writeheader()
    for i in students:
        writer.writerow(i)
