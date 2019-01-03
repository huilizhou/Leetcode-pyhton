# 二分查找
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 我的解法
        # if target not in nums:
        #     return -1
        # return nums.index(target)

        # 根据题意来的写法
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        #  End Condition:left>right
        return -1


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2))
