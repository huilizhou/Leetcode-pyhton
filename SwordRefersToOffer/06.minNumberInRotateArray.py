# -*- coding:utf-8 -*-
# 旋转数组的最小数字


class Solution:
    def minNumberInRotateArray(self, nums):
        # write code here
        low, high = 0, len(nums) - 1
        while low < high:
            if nums[low] < nums[high]:
                return nums[low]

            mid = (low + high) // 2
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
