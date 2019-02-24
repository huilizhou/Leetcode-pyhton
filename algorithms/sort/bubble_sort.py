# 冒泡排序
'''
20190116 恪穆整理

1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''


# class Solution:
#     def bubble_sort(self, list):
#         length = len(list)
#         for index in range(length):
#             for j in range(1, length - index):
#                 if list[j - 1] > list[j]:
#                     list[j - 1], list[j] = list[j], list[j - 1]
#         return list

# 改进后的
class Solution:
    def bubble_sort_flag(self, list):
        length = len(list)
        for index in range(length):
            flag = True
            for j in range(1, length - index):
                if list[j - 1] > list[j]:
                    list[j - 1], list[j] = list[j], list[j - 1]
                    flag = False
            if flag:
                return list
        return list


print(Solution().bubble_sort_flag([3, 2, 4, 1, 5, 6, 10, 8]))
