import numpy as np
#
# print(np.array([1, 2, 3]))
# print(np.array([[1, 2], [3, 4]]))
# print(np.array([1, 2, 3, 4, 5], ndmin=5))
# print(np.array([1, 2, 3], dtype=str))
#
# dt = np.dtype(np.int64)
# dt8 = np.dtype('i8')
# dt4 = np.dtype('i4')
# dt2 = np.dtype('i2')
# dt1 = np.dtype('i1')
#
# print(np.array([1342, 223123, 33534], dtype=dt))
# print(np.array([1342, 223123, 33534], dtype=dt8))
# print(np.array([1342, 223123, 33534], dtype=dt4))
# print(np.array([1342, 223123, 33534], dtype=dt2))
# print(np.array([1342, 223123, 33534], dtype=dt1))
#
# dt = np.dtype([('age', np.int32)])
# a = np.array([(18,), (19,), (20,), (21,)], dtype=dt)
# print(a)
# print(dt)
# print(a['age'])
# print("===========================\n")
#
# a = np.array([("abc",), (19,), (20,), (21,)], dtype=dt)
# print(a)
# b = np.array([("100",), (19,), (20,), (21,)], dtype=dt)
# print(b)
#
# person = np.dtype([('name', 'S20'), ('height', 'f'), ('age', 'i')])
# print(person)
# me = np.array([("fbp", 1.7, 23), ("lyh", 1.69, 22)], dtype=person)
# print(me)
#
# a = np.array([(1, 2, 3), (4, 5, 6)])
# print("维度：", a.ndim)
# print("形状：", a.shape)
# print("大小：", a.size)
# print("元素大小：", a.itemsize)
# print("对象的内存信息：", a.flags)
# print("实部：", a.real)
# print("虚部：", a.imag)
#
# a = np.arange(24)
# print(a)  # a 现只有一个维度
# # 现在调整其大小
# b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
# print(b)
#
# a = np.empty([2, 3], dtype=int)
# print(a)
# b = np.zeros(5)
# print(b)
# c = np.zeros([5, 5])
# print(c)
# d = np.ones((5, 10, 10))
# print(d)
# e = np.arange(10, 21, 2)
# print(e)
# print(e.ndim)
# e.shape = (3, 2)
# print(e)
# print(e.ndim)
#
# a = np.arange(1, 20, 2)
# b1 = a[5:9:2]
# b2 = slice(5, 9, 2)
# print(a)
# print(a[..., :2])
# print(a[..., :9:2])
# print(b1)
# print(a[b2])
#
# x = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]])
# y = x[[1, 2, 0], [0, 2, 2]]
# print(y)
#
# x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
# rows = np.array([[0], [0], [3], [3]])
# cols = np.array([[0], [4], [0], [4]])
# y = x[rows, cols]
# print('4*5的四个角是：')
# print(y)
#
# x = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
# b = np.array([[1, 2, 3], [1, 4, 3]])
# print(x + b)
#
# a = np.arange(9)
# b = a.reshape(3, 3)
# print(b)
# for x in np.nditer(b, order="F"):
#     print(x, end="")
#
# a = np.arange(1, 10).reshape(3, 3)
# b = np.array([1, 2, 3], dtype=int)
#
# for x, y in np.nditer([a, b]):
#     print("%d - %d" % (x, y))
#
# s = np.ones([2, 4])
# print(s.dtype)
# print(np.arange(10, 5, -1))
# a = np.array(["100", "2000"], dtype=np.str_)
# print(a.dtype)
# # print(a)
# a = np.array([1, 2, 3, 4])
# print(a * 2)
# print(a > 2)
# b = np.array([2, 4, 6, 8])
# print(a * b)
# print(a > b)
#
# a = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])
# print(a.ndim)
# print(a.shape)
# print(a[1, 0, 1])
#
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a[:2][:1][:1])
# print(a[:2, :1].ndim)
#
# a = np.array([1, 2, 3, 4, 5, 6])
# b = np.array([True, False, True, False, True, False])
# print(a[b])
# a = np.array([1, 2, 3, 4, 5, 6])
# b = a[[0, 1, 2]]
# print(b)
#
# x = np.array([[1], [2], [3]])
# y = np.array([4, 5, 6])
# r, c = np.broadcast(x, y).iters
# print(r[:])
# print(c[:])
# for i in range(9):
#     print(next(r))
#
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])
# print(np.concatenate((x, y), axis=0))
# print(np.concatenate((x, y), axis=1))
#
# x = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(np.append(x, [[7, 8, 9]], axis=0))
# print(np.append(x, [[7, 8, 9], [10, 11, 12]], axis=1))
#
# a = np.arange(3, 15).reshape(3, 4)
# print(a)
# print(np.delete(a, 5))
# print("删除第二行")
# print(np.delete(a, 1, axis=0))
# print("删除第二列")
# print(np.delete(a, 1, axis=1))
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(np.delete(a, np.s_[::2]))
#
# a = np.arange(24).reshape(2, 3, 4)
# print(a)
# print(a.ndim)
# a = a.transpose(2, 1, 0)
# print(a.shape)
# print(a)
# a = a.swapaxes(2, 0)
# print(a.shape)
#
# # 两个数组对应下标元素的乘积和
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# print(a.dot(b))
#
# # amin()&amax() 用于计算数组中的元素沿指定轴的最小&大值
# # axis=0，X轴动；axis=1，Y轴动
#
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.amin(a))
# print(np.amin(a, axis=0))  # 0动
# print(np.amin(a, axis=1))
# print(np.amax(a))
# print(np.amax(a, axis=0))  # 0动
# print(np.amax(a, axis=1))  # 1动
#
# # 加减乘除: add()、subtract()、multiply()、divide()
# # 广播机制
# a = np.arange(9, dtype=np.int8).reshape(3, 3)
# b = np.array([10, 10, 10])
# print(np.add(a, b))
# print(np.subtract(a, b))
# print(np.multiply(a, b))
# print(np.divide(a, b))
#
# x = np.arange(9)
# y = np.where(x > 3)  # 取出大于3的元素
# print(y)
# print(x[y])  # 索引
#
# a = np.array([[2, 4], [3, 1]])
# print(np.sort(a))  # 排序函数
#
# print(np.char.add(['hello'], [' xyz']))  # 类似于字符拼接
# print(np.char.multiply('hello', 3))  # 乘法（与python内置语法效果一致）
# print(np.char.center('abc', 20, fillchar='*'))  # 字符居中空位用*填充
# print(np.char.capitalize("abcdef"))  # 首字母大写
# print(np.char.title('i like python'))  # 每个单词首字母大写
# print(np.char.split('www.ai.com', sep='.'))  # 分割（与python内置语法效果一致）
# print(np.char.join(['*', '='], ['microsoft', 'huawei']))  # join（与python内置语法效果不同）
# print(np.char.replace('你是日本人', '日本人', '***'))  # 替换函数（与python内置语法效果一致）
