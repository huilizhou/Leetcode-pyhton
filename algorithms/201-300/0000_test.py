# L = [1, 2, 3, 4, 5]
# print(L.pop(0))
# print(L.pop(0))
# print(L)


# class Solution:
#     def merge_sort(self, list):
#         """合并"""
#         def merge(left, right):
#             res = []
#             while left and right:
#                 if left[0] < right[0]:
#                     res.append(left.pop(0))
#                 else:
#                     res.append(right.pop(0))
#             if left:
#                 res += left
#             if right:
#                 res += right
#             return res

#         if len(list) <= 1:
#             return list
#         middle = len(list) // 2
#         left = self.merge_sort(list[:middle])
#         right = self.merge_sort(list[middle:])
#         return merge(left, right)


# print(Solution().merge_sort([2, 4, 3, 1, 9, 8, 6, 7]))

# # 快速排序
# class Solution:
#     def quick_sort(self, list):
#         list = list[:]
#         n = len(list)

#         def partition(list, start, end):
#             i = start - 1
#             pivotIndex = end
#             pivot = list[end]
#             for j in range(start, end):
#                 if list[j] < pivot:
#                     i = i + 1
#                     list[j], list[i] = list[i], list[j]
#             list[i + 1], list[pivotIndex] = list[pivotIndex], list[i + 1]
#             return i + 1

#         def sort(list, start, end):
#             if start >= end:
#                 return
#             p = partition(list, start, end)
#             sort(list, start, p - 1)
#             sort(list, p + 1, end)

#         sort(list, 0, n - 1)
#         return list


# print(Solution().quick_sort([2, 9, 3, 1, 5, 8, 7, 6]))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # a[0], a[1:] = a[-1], a[:-1]
# # print(a)
# # a.pop()
# # print(a)
# print(a[0:2])

# board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# for i in board:
#     i.insert(0, 0)
#     i.append(0)
# #     # print(i)
# board = [[0] * (len(board[0]))] + board + [[0] * (len(board[0]))]
# for i in board:
#     print(i)
# # print(board)
# board = [1, 2, 3, 4, 5]
# board.pop(0)
# board.pop(-2)
# print(board)


# s = "bac"

# print(list(s))

# import bisect

# a = [2, 3, 1, 5, 8, 6, 7]
# print(bisect.bisect_left(a, 5))
# print(a)
# print(bisect.bisect_right(a, 5))

# a = [3, 4, 6, 7, 9]
# b = bisect.bisect(a, 8)
# print(b)

# a.insert(b, 8)
# b = bisect.bisect(a, 8.0)
# print(a, b)

# class Solution:
#     def lengthOfLIS(self, nums):
#         if not nums:
#             return 0
#         res = [nums[0]]
#         for i in range(1, len(nums)):
#             if nums[i] > res[-1]:
#                 res.append(nums[i])
#             else:
#                 l, r = 0, len(res) - 1
#                 while l <= r:
#                     mid = (l + r) // 2
#                     if nums[i] > res[mid]:
#                         l = mid + 1
#                     else:
#                         r = mid - 1
#                 res[l] = nums[i]
#         return len(res)


# print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


# str = "dog cat cat dog"
# print(str)
# l = str.split(' ')
# print(l)
# z = zip(['a', 'b', 'b', 'a'], ['dog', 'cat', 'cat', 'dog'])
# print(list(z))
# sp = [x + y for x, y in z]
# print(sp)


# dic = {'a': 2, 'b': 1}
# dic1 = {'b': 1, 'a': 2}
# print(dic1 == dic)
# print(dic['a'])


print(list(zip('abb', 'egg')))

# print(list(zip(*zip('abb', 'egg'))))
