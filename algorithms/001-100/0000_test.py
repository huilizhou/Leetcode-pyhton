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


'''
选择排序
'''


# class Solution:
#     def selection_sort(self, nums):
#         n = len(nums)
#         for i in range(n):
#             minIndex = i
#             for j in range(i + 1, n):
#                 if nums[j] < nums[minIndex]:
#                     minIndex = j
#             if minIndex == i:
#                 pass
#             else:
#                 nums[i], nums[minIndex] = nums[minIndex], nums[i]

#         return nums


# print(Solution().selection_sort([2, 1, 3, 4, 9, 8, 7, 6]))


# class MonoSum:
#     def calcMonoSum(self, A, n):
#         # write code here
#         sum = 0
#         for i in range(n):
#             for j in range(i):
#                 if A[j] <= A[i]:
#                     sum += A[j]
#         return sum


# print(MonoSum().calcMonoSum([1, 3, 5, 2, 4, 6], 6))


# matrix = [[0] * 3] * 3
# print(matrix)


# matrix = [[0 for _ in range(3)]for _ in range(3)]


# import numpy as np

# A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# a = np.rank(A)
# print(a)

# U, S, V = np.linalg.svd(np.dot(A.T, A))
# print(S)


# def translter(s):
#     res = []
#     for i in range(len(s)):
#         if s[i].isalpha():
#             if (ord('a') <= ord(s[i]) < ord('z') or ord('A') <= ord(s[i]) < ord('Z')):
#                 res.append(chr(ord(s[i]) + 1))
#             elif s[i] == 'z':
#                 res.append('a')
#             elif s[i] == 'Z':
#                 res.append('A')
#         else:
#             res.append(s[i])
#     return ''.join(res)


# if __name__ == "__main__":
#     s = input()
#     # s = 'Hello! How are you!'
#     print(translter(s))

# n = int(input())
# print(bin(n)[2:])


# while True:
#     try:
#         a, d = int(input()), {}
#         for i in range(a):
#             x, y = map(int, input().split())
#             d[x] = y
#         for i in sorted(d.items(), key=lambda c: c[1]):
#             print(str(i[0]) + " " + str(i[1]))
#     except:
#         break

# def solve(d):
#     a = sorted(d.items(), key=lambda x: x[1])
#     for i in a:
#         print(str(i[0]) + " " + str(i[1]))


# if __name__ == "__main__":
#     n = 3
#     d = {1: 90, 2: 87, 3: 93}
#     solve(d)


# import numpy as np
# a = [1, 2, 3]
# v = [4, 5, 6]
# print(np.convolve(a, v))


# for i, v in enumerate(['tic', 'tac', 'toe'], 1):
#     print(i, v, end=" ")


# '''
# Kmp
# '''


# def kmp_match(s, p):
#     m = len(s)
#     n = len(p)
#     table = partial_table(p)
#     cur = 0
#     while cur <= m - n:
#         for i in range(len(p)):
#             if s[cur + i] != p[i]:
#                 cur += max(i - table[i - 1], 1)
#                 break
#         else:
#             return cur
#     return -1


# def partial_table(p):
#     prefix = set()
#     postfix = set()
#     ret = [0]
#     for i in range(1, len(p)):
#         prefix.add(p[:i])
#         postfix = {p[j:i + 1] for j in range(1, i + 1)}
#         ret.append(len((prefix & postfix or {""}).pop()))
#     return ret


# print(partial_table('ABCDABD'))
# print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))


# print([[]] + [[1]])

# print([] + [])


# import itertools

# print(list(itertools.combinations([1, 2, 3], 2)))


# import itertools

# print(list(itertools.permutations([], 0)))


# s = '12bb3nn4'
# print(s[-1:1])


# s = ["flower", "flow", "flight"]
# print(list(zip(*s)))
# # print(list(zip(s)))


# def joseph(n,m):
#     if n==1:
#         return n
#     return (joseph(n-1,m)+m-1)%n+1

# print(joseph(42,3))

# def solve(n, m):
#     # 自动身成列表,从0开始 到n-1
#     list = [_ for _ in range(n)]
#     m -= 1
#     k = m % n
#     while(len(list) > 1):
#         print(list[k])
#         del list[k]
#         k = (k + m) % len(list)
#     return list[0]


# print(solve(5, 2))


# def josephus(n, k):
#     if k == 1:
#         print(n)
#         return
#     p = 0
#     people = list(range(1, n + 1))
#     while True:
#         if len(people) == 1:
#             break
#         p = (p + (k - 1)) % len(people)
#         del people[p]
#     print(people[0])


# if __name__ == '__main__':
#     N = int(input())
#     josephus(N, 3)


# s = input()
# num, char, d = 0, 0, 0
# for i in s:
#     if i.isdigit():
#         num = num + 1
#     elif i.isalpha():
#         char = char + 1
#     else:
#         d = d + 1
# print(num, char, d)


nums = [1, - 2, 3, 4, 10, 9, -5, -10]
nums_sort = sorted(nums)
count = 0
res = 1
for i in nums_sort:
    if i < 0:
        count += 1
    else:
        break

if count % 2 != 0:
    for j in range(count - 1):
        # print(nums_sort[j])
        res *= nums_sort[j]
    for j in range(count, len(nums_sort)):
        # print(nums_sort[j])
        res *= nums_sort[j]
elif count % 2 == 0:
    for k in range(count):
        # print(nums_sort[k])
        res *= nums_sort[k]
    for k in range(count + 1, len(nums_sort)):
        # print(nums_sort[k])
        res *= nums_sort[k]


print(res)
