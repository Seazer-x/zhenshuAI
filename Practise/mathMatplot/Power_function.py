import numpy as np
import matplotlib.pyplot as plt
import random

# 幂函数
x = np.arange(-10, 10, 0.1)
y = x ** 2
plt.plot(x, y)
plt.show()

# 常函数
x = np.arange(-1000, 1000, 0.1)
y = x * 0 + 1
plt.plot(x, y)
plt.show()

# 对数函数
x = np.arange(0.1, 10, 0.1)
y1 = np.log(1 / x)
y2 = np.log(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.axhline(0)
plt.show()

# 三角函数
x = np.arange(-10, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y5 = np.tan(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y5)
plt.show()

# Sigmoid函数
x = np.arange(-10, 10, 0.1)
y = 1 / (1 + np.e ** (-x))
plt.plot(x, y)
plt.show()

x = np.arange(-10, 10, 0.1)
y = np.maximum(0, x)
plt.plot(x, y)
plt.show()

x = np.arange(-10, 10, 0.1)
y = np.tanh(x)
plt.plot(x, y)
plt.show()


# 梯度下降法
# xw + b = h
# loss = (y - h) ** 2
_x = [i / 100 for i in range(100)]
_y = [3 * e + 10 + random.random() for e in _x]
w = random.random()
b = random.random()

plt.ion()
for i in range(1000):
    for x, y in zip(_x, _y):
        z = w * x + b
        loss = (z - y) ** 2
        dw = -2 * (z - y) * x
        db = -2 * (z - y)
        w = w + 0.001 * dw
        b = b + 0.001 * db
    plt.cla()
    plt.plot(_x, _y, ".")
    v = [w * e + b for e in _x]
    plt.plot(_x, v)
    plt.pause(0.01)
    # print(w, b)
plt.ioff()
plt.show()
