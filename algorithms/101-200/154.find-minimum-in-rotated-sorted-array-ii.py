# 寻找旋转排序数组中的最小值II
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[right]:  # 关键的去重，不能每次舍弃一半的元素，而只能逐个筛选
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


print(Solution().findMin([2, 2, 2, 0, 1]))
