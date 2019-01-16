# 希尔排序
"""
希尔排序是基于插入排序的以下两点性质而提出改进方法的：

插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位
"""


class Solution:
    def shell_sort(self, list):
        n = len(list)
        # 初始步长
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = list[i]
                j = i
                while j >= gap and list[j - gap] > temp:
                    list[j] = list[j - gap]
                    j -= gap
                list[j] = temp
            gap = gap // 2
        return list


print(Solution().shell_sort([2, 1, 3, 7, 5, 6, 4]))
