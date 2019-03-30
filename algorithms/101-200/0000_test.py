# s = "the sky is blue"
# L = s.split()
# L = " ".join(L[::-1])
# print(L)

# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]

# # index = inorder.index(postorder[-1])
# # # print(index)
# # print(inorder[0:index], postorder[0:index])

# print(inorder[0:0])

# res = []
# for i in range(5):
#     res.append([1] * (i + 1))
# print(res)

# x = [
#     [2],
#     [3, 4],
#     [6, 5, 7],
#     [4, 1, 8, 3]
# ]
# f = [0] * (len(x) + 1)
# print(f)


# x = [2, 1]
# print(x.index(max(x)))


# a = {1, 2, 3, 4, 5, 6}
# print(a)

# 希尔排序
# class Solution:
#     def shell_sort(self, list):
#         n = len(list)
#         gap = n // 2
#         while gap > 0:
#             for i in range(gap, n):
#                 temp = list[i]
#                 j = i
#                 while j >= gap and list[j - gap] > temp:
#                     list[j] = list[j - gap]
#                     j -= gap
#                 list[j] = temp
#             gap = gap // 2
#         return list


# print(Solution().shell_sort([2, 1, 3, 7, 5, 6, 4]))


# # 堆排序
# class Solution:
#     def heap_sort(self, list):
#         '''最大堆调整'''
#         def shift_down(start, end):
#             root = start
#             while True:
#                 child = 2 * root + 1
#                 if child > end:
#                     break
#                 if child + 1 <= end and list[child] < list[child + 1]:
#                     child += 1
#                 if list[root] < list[child]:
#                     list[child], list[root] = list[root], list[child]
#                     root = child
#                 else:
#                     break

#         # 构建最大堆
#         for start in range((len(list) - 2) // 2, -1, -1):
#             shift_down(start, len(list) - 1)

#         # 堆排序
#         for end in range(len(list) - 1, 0, -1):
#             list[0], list[end] = list[end], list[0]
#             shift_down(0, end - 1)
#         return list


# print(Solution().heap_sort([9, 3, 2, 1, 4, 5, 6, 8, 7]))

# import sys
# n = sys.stdin.readlines()

# version1 = "1.002"
# ver1 = [int(token) for token in version1.split(".")]
# print(ver1)
