# 插入排序
'''
20190116 恪穆整理

一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
'''


class Solution:
    def insert_sort(self, list):
        # n = len(list)
        # if n == 1:
        #     return list
        # for i in range(1, n):
        #     for j in range(i, 0, -1):
        #         if list[j] < list[j - 1]:
        #             list[j], list[j - 1] = list[j - 1], list[j]
        #         else:
        #             break
        # return list

        # 方法二
        n = len(list)
        for i in range(1, n):
            if list[i] < list[i - 1]:
                # 将这个数取出
                temp = list[i]
                # 保存下标
                index = i
                # 从后往前依次比较每个元素
                for j in range(i - 1, -1, -1):
                    # 和比取出元素大的元素交换
                    if list[j] > temp:
                        list[j + 1] = list[j]
                        index = j
                    else:
                        break
                # 插入元素
                list[index] = temp
        return list


print(Solution().insert_sort([42, 20, 17, 13, 28, 14, 23, 15]))
