import csv

import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
matplotlib.use('tkagg')
plt.figure(figsize=(10, 5), dpi=150)
plt.style.use(['tableau-colorblind10'])
score = csv.reader(open('student.csv', 'r', encoding='utf-8'))
nv = 0
nan = 0
for student in score:
    if student[3] == '男':
        nan += 1
    else:
        nv += 1
data = [nan, nv]
labels = ["男：" + str(nan), "女：" + str(nv)]
plt.pie(x=data, labels=labels)
plt.title('性别比例分布图')
plt.show()
plt.close()
