# S = 'abcdjj'
# print(S[2].isalpha())


# basket = {'apple', 'orange', 'apple', 'pear', 'banana', 'orange'}
# print(basket)

# a = set('abracadabra')
# b = set('alacazam')
# # print(a)
# # print(b)
# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# thisset = set(("Google", "Runoob", "Taobao"))
# # thisset.add("Facebook")
# thisset.update([1, 2], [1, 4])
# print(thisset)
# # thisset.remove("7")
# thisset.discard("7")
# thisset.clear()
# print(thisset)

# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# # x.intersection_update(y, z)
# r = x.intersection(y, z)
# print(r, x, y, z)


# for i in range(10, -1, -1):
#     print(i)

# res = [2, 3, 2, 3, 1, 5]
# print(list(set(res)))


# 生成器
# def countdown(x):
#     while x >= 0:
#         yield x
#         x -= 1


# for i in countdown(10):
#     print(i)


# import numpy as np

# A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# U, S, V = np.linalg.svd(np.dot(A.T, A))
# print(S)

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(len(dict))
# print(dict.items())
# print(dict.keys())
# print(dict.values())

# a = set('abracadabra')
# b = set('alacazam')
# print(a, b)
# print(a.difference(b))
# c = list(a)
# c.sort()
# print(c)


# list = [1, 2, 3, 4]
# it = iter(list)
# for x in it:
#     print(x, end=" ")


# prefix = {"A", "B", "AB", "ABC"}
# postfix = {"ABC"}
# print(postfix & prefix)
# print(len(((postfix & prefix)or {""}).pop()))


# def kmp_match(s, p):
#     m = len(s)
#     n = len(p)
#     cur = 0
#     table = partial_table(p)
#     while cur <= m - n:
#         for i in range(n):
#             if s[i + cur] != p[i]:
#                 cur += max(i - table[i - 1], 1)
#                 break
#         else:
#             return True
#     return False


# def partial_table(p):
#     prefix = set()
#     postfix = set()
#     res = [0]
#     for i in range(1, len(p)):
#         prefix.add(p[:i])
#         postfix = {p[j:i + 1] for j in range(1, i + 1)}
#         res.append(len((prefix & postfix or {""}).pop()))
#     return res


# print(partial_table("ABCDABD"))
# print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
