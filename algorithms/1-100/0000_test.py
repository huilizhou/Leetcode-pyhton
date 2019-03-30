# dict = {-1: 2, 0: 1, 1: 1, 2: 1, -4: 1}
# neg = list(filter(lambda x: x < 0, dict))
# print(neg)

# pos_dict = [3, 2, 4, 5, 1, 4]

# for i, v in enumerate(pos_dict):
#     print(i, v)

# L = ["flower", "flow", "flight"]
# print(min(L))
# print(max(L))


# str = "aner"
# print(list(str))


# L = ['a', 'b', 'c', 'b', 'a']
# s = "".join(L)
# print(s)

# print(ord("f"))

# for i in ["eat", "tea", "tan", "ate", "nat", "bat"]:
#     s = list(i)
#     print(s)

# i = "acb"
# a = "".join(sorted(i))

# print(a)


# matrix = [[0 for _ in range(4)]for _ in range(4)]
# print(matrix)


# res = 0
# nums2 = "23"
# for i in range(len(nums2) - 1, -1, -1):
#     print(nums2[i], i)

# n = 3
# factor = [0] * n
# # print(factor)
# factor[0] = 1
# for i in range(1, n):
#     factor[i] = factor[i - 1] * i
# print(factor)

# names = ["Cecilia", "Lise", "Marie"]
# letters = [len(n) for n in names]

# # # print(letters)

# longest_name = None
# max_letters = 0

# # for i in range(len(names)):
# #     count = letters[i]
# #     if count > max_letters:
# #         longest_name = names[i]
# #         max_letters = count
# # print(longest_name)

# for i, name in enumerate(names):
#     count = letters[i]
#     if count > max_letters:
#         longest_name = name
#         max_letters = count
# print(longest_name)

# for name, count in zip(names, letters):
#     if count > max_letters:
#         longest_name = name
#         max_letters = count
# print(longest_name)

# names.append("Rosalind")
# for name, count in zip(names, letters):
#     print(name)

# # a = [1, 2, 3]
# # b = [4, 5, 6]
# # c = [4, 5, 6, 7, 8]
# # print(list(zip(a, b)))
# # print(list(zip(a, c)))

# a1, a2 = zip(*[(1, 2), (3, 4), (5, 6)])
# print(list(a1))
# print(list(a2))

# idx = [(2, 3), (3, 4)]
# idx.append((1, 2))

# print(idx.pop())

# j = 1
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# for k in matrix:
#     k[j] = 0
#     print(k)

# print(bin(-4).count("1"))

# a = [[1, 2, 3], [2, 3, 4]]
# # a = a + a
# # print(a)
# a.reverse()
# print(a)

# def zhuanzhi(matrix):
#     matrix.reverse()
#     for i in range(len(matrix)):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     return matrix


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a[:] = map(list, zip(*a[::-1]))
# print(a)

# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
# print(list(zip(m, n)))

# a = ([1, 2, 3], [1, 1, 1]), ([4, 5, 6], [2, 2, 2])
# print((*zip(a)))

# x = ['a', '1']
# y = ['b', '2']
# z = list(zip(x, y))
# print(z)
# print(list(zip(*z)))
