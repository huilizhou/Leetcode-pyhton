# 堆排序
"""
20190116 恪穆整理

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆是一个近似完全二叉树的结构，并同时满足堆积的性质：
即子结点的键值或索引总是小于（或者大于）它的父节点。

堆节点的访问
通常堆是通过一维数组来实现的。在数组的起始位置为0的情形中：
- 父节点i的左子节点的位置(2i+1)
- 父节点i的右子节点的位置(2i+2)
- 子节点i的父节点位置为(i-1)//2


1.创建最大堆:将堆所有数据重新排序，使其成为最大堆
2.最大堆调整:作用是保持最大堆的性质，是创建最大堆的核心子程序
3.堆排序:移除位在第一个数据的根节点，并做最大堆调整的递归运算

"""


class Solution:
    def heap_sort(self, list):
        def sift_down(start, end):
            """最大堆调整"""
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and list[child] < list[child + 1]:
                    child += 1
                if list[root] < list[child]:
                    list[root], list[child] = list[child], list[root]
                    root = child
                else:
                    break

    # 创建最大堆
        for start in range((len(list) - 2) // 2, -1, -1):
            sift_down(start, len(list) - 1)

    # 堆排序
        for end in range(len(list) - 1, 0, -1):
            list[0], list[end] = list[end], list[0]
            sift_down(0, end - 1)
        return list


# class Solution:
#     def heap_sort(self, list):
#         # 创建最大堆
#         for start in range((len(list) - 2) // 2, -1, -1):
#             self.sift_down(start, len(list) - 1, list)

#     # 堆排序
#         for end in range(len(list) - 1, 0, -1):
#             list[0], list[end] = list[end], list[0]
#             self.sift_down(0, end - 1, list)
#         return list

#     def sift_down(self, start, end, list):
#         """最大堆调整"""
#         root = start
#         while True:
#             child = 2 * root + 1
#             if child > end:
#                 break
#             if child + 1 <= end and list[child] < list[child + 1]:
#                 child += 1
#             if list[root] < list[child]:
#                 list[root], list[child] = list[child], list[root]
#                 root = child
#             else:
#                 break


print(Solution().heap_sort([9, 2, 1, 7, 6, 8, 5, 3, 4]))
