# 删除排序数组的重复项并返回长度

# 输入的是一个数组，返回的是一个值。
# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         for i in range(0, len(nums) - 1):
#             if nums[i] == nums[i - 1]:
#                 del nums[i]
#         return len(nums)
#         # return len(set(nums))


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = index = 0
        Current = None
        while index < len(nums):
            if(nums[index] != Current):
                nums[ret] = nums[index]
                ret += 1
                Current = nums[index]
            index += 1
        return ret


print(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]))
