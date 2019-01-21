# 归并排序
"""
20190118 恪穆整理

是创建在归并操作上的一种有效的排序算法。1945年由约翰·冯·诺伊曼首次提出。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。

采用 divide-and-conquer approach:
Divide: 把长度为 n 的 array 分成两半。
Conquer: 把左半边 array 及右半边 array 分别以 Merge Sort 进行 sorting。 (recursive)
Combine: merge 左半边及右半边 sorted array。

1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2.设定两个指针，最初位置分别为两个已经排序序列的起始位置
3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4.重复步骤3直到某一指针达到序列尾
5.将另一序列剩下的所有元素直接复制到合并序列尾
"""
# 递归版


class Solution:
    def merge_sort(self, list):
        '''合并'''
        def merge(left, right):
            result = []
            while left and right:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            if left:
                result += left
            if right:
                result += right
            return result
        # 认为长度不大于1的数列是有序的
        if len(list) <= 1:
            return list
        # 二分列表
        middle = len(list) // 2
        left = self.merge_sort(list[:middle])
        right = self.merge_sort(list[middle:])
        # 最后一次合并
        return merge(left, right)


# class Solution:
#     def merge_sort(self, list):
#         # 认为长度不大于1的数列是有序的
#         if len(list) <= 1:
#             return list
#         # 二分列表
#         middle = len(list) // 2
#         left = self.merge_sort(list[:middle])
#         right = self.merge_sort(list[middle:])
#         # 最后一次合并
#         return self.merge(left, right)

#     def merge(self, left, right):
#         result = []
#         while left and right:
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#         if left:
#             result += left
#         if right:
#             result += right
#         return result


print(Solution().merge_sort([42, 20, 17, 13, 28, 14, 23, 15]))
