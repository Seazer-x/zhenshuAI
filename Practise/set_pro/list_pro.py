list1 = [0, 0, 0, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 7, 5]
print(list1)
print(set(list1))

# 将可迭代对象合并到列表中
tuple1 = (1, 2, 3)
set1 = {4, 5, 6}
list2 = [*tuple1, *set1]
print(list2)

# 用字典拆包合并两个字典
dict_a = {'one': 1, 'two': 2}
dict_b = {'three': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)
