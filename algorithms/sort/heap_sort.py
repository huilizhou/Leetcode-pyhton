# 堆排序
"""
20190116 恪穆整理

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆是一个近似完全二叉树的结构，并同时满足堆积的性质：
即子结点的键值或索引总是小于（或者大于）它的父节点。

1.创建最大堆:将堆所有数据重新排序，使其成为最大堆
2.最大堆调整:作用是保持最大堆的性质，是创建最大堆的核心子程序
3.堆排序:移除位在第一个数据的根节点，并做最大堆调整的递归运算

"""


class Solution:
    def heap_sort(self, lst):
        def sift_down(start, end):
            """最大堆调整"""
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and lst[child] < lst[child + 1]:
                    child += 1
                if lst[root] < lst[child]:
                    lst[root], lst[child] = lst[child], lst[root]
                    root = child
                else:
                    break

    # 创建最大堆
        for start in range((len(lst) - 2) // 2, -1, -1):
            sift_down(start, len(lst) - 1)

    # 堆排序
        for end in range(len(lst) - 1, 0, -1):
            lst[0], lst[end] = lst[end], lst[0]
            sift_down(0, end - 1)
        return lst


print(Solution().heap_sort([3, 2, 4, 1, 5, 6, 10, 8]))
