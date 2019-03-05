# -*- coding:utf-8 -*-
# 数组中的逆序对


class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        temp = [i for i in data]
        return self.mergeSort(temp, data, 0, len(data) - 1) % 1000000007

    def mergeSort(self, temp, data, low, high):
        if low >= high:
            temp[low] = data[low]
            return 0
        mid = (high + low) // 2
        left = self.mergeSort(data, temp, low, mid)
        right = self.mergeSort(data, temp, mid + 1, high)

        count = 0
        i = low
        j = mid + 1
        index = low
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                temp[index] = data[j]
                i += 1
            else:
                temp[index] = data[j]
                count += mid - i + 1
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= high:
            temp[index] = data[j]
            j += 1
            index += 1
        return count + left + right


print(Solution().InversePairs([2, 3, 4, 5, 6, 7, 0]))
