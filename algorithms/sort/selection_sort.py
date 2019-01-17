# 选择排序
'''
20190116 恪穆整理

是一种简单直观的排序算法。
它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

'''


class Solution:
    def selection_sort(self, list):
        # n = len(list)
        # for i in range(n):
        #     minIndex = i
        #     for j in range(i + 1, n):
        #         if list[j] < list[minIndex]:
        #             minIndex = j
        #             list[minIndex], list[i] = list[i], list[minIndex]
        # return list

        n = len(list)
        for i in range(n):
            minIndex = i
            for j in range(i + 1, n):
                if list[j] < list[minIndex]:
                    minIndex = j
            if i == minIndex:
                pass
            else:
                list[minIndex], list[i] = list[i], list[minIndex]
        return list


print(Solution().selection_sort([3, 2, 4, 1, 5, 6, 10, 8]))
