# 在排序数组中查找元素的第一个和最后一个位置
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 我的想法
        if target not in nums:
            return [-1, -1]
        while target in nums:
            if nums.count(target) == 1:
                return [nums.index(target), nums.index(target)]
            else:
                return [nums.index(target), nums.index(target) + nums.count(target) - 1]

        # # 人家的解法，二分查找
        # if len(nums) == 0:
        #     return [-1, -1]
        # elif target < nums[0] or target > nums[-1]:
        #     return [-1, -1]
        # else:
        #     l, r = 0, len(nums) - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if target > nums[mid]:
        #             l = mid + 1
        #         elif target < nums[mid]:
        #             r = mid - 1
        #         # 当找到相等的值时，把左右指针合并并分别向左向右依次遍历找出上下限
        #         elif target == nums[mid]:
        #             l = r = mid
        #             while l - 1 >= 0 and nums[l - 1] == target:
        #                 l -= 1
        #             while r + 1 <= len(nums) - 1 and nums[r + 1] == target:
        #                 r += 1
        #             return [l, r]
        # return [-1, -1]


print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
