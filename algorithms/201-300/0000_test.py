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

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[0], a[1:] = a[-1], a[:-1]
# print(a)
# a.pop()
# print(a)
print(a[0:2])
