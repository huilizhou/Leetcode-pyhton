# 快速排序
'''
20190120 恪穆整理

1.从数列中挑出一个元素，称为“基准”（pivot），
2.重新排序数列，所有比基准值小的元素摆放在基准前面，
所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。
在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作。
3.递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归到最底部时，数列的大小是零或一，也就是已经排序好了。
这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

'''

'''python的简单版本'''
# class Solution:
#     def quick_sort(self, list):
#         if len(list) <= 1:
#             return list
#         less = []
#         greater = []
#         pivot = list.pop()
#         for item in list:
#             if item < pivot:
#                 less.append(item)
#             else:
#                 greater.append(item)
#         list.append(pivot)
#         return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

# 人家的简便写法
# class Solution:
#     def quick_sort(self, arr):
#         if len(arr) < 1:
#             return arr
#         else:
#             pivot = arr[0]
#             return self.quick_sort([x for x in arr[1:] if x < pivot]) + [pivot] + self.quick_sort([x for x in arr[1:] if x >= pivot])


class Solution:
    def quick_sort(self, list):
        # list = list[:]
        n = len(list)

        def partition(list, start, end):
            i = start - 1
            pivot = list[end]
            for j in range(start, end):
                if list[j] < pivot:
                    i = i + 1
                    list[i], list[j] = list[j], list[i]
            list[i + 1], list[end] = list[end], list[i + 1]
            return i + 1

        def sort(list, start, end):
            if start >= end:
                return
            p = partition(list, start, end)
            sort(list, start, p - 1)
            sort(list, p + 1, end)

        sort(list, 0, n - 1)
        return list


print(Solution().quick_sort([9, 1, 2, 5, 8, 3, 4, 7, 10, 6]))


#  pivot 取第一个语言版本类似的
# class Solution:
#     def quick_sort(self, list):
#         n = len(list)

#         def partitons(list, left, right):
#             pivot = list[left]
#             while left < right:
#                 while left < right and list[right] >= pivot:
#                     right -= 1
#                 list[left] = list[right]
#                 while left < right and list[left] <= pivot:
#                     left += 1
#                 list[right] = list[left]
#             list[left] = pivot
#             return left

#         def q_sort(list, left, right):
#             if left < right:
#                 p = partitons(list, left, right)
#                 q_sort(list, left, p - 1)
#                 q_sort(list, p + 1, right)
#         q_sort(list, 0, n - 1)
#         return list


# print(Solution().quick_sort([5, 9, 1, 11, 6, 7, 2, 4]))
