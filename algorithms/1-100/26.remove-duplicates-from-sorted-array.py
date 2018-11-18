# 删除排序数组的重复项并返回长度

# 输入的是一个数组，返回的是一个值。


# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return
#         l = 1
#         for i in range(len(nums) - 1):
#             if nums[i] != nums[i + 1]:
#                 nums[l] = nums[i + 1]
#                 l += 1
#         return l

# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         ret = index = 0
#         Current = None
#         while index < len(nums):
#             if(nums[index] != Current):
#                 nums[ret] = nums[index]
#                 ret += 1
#                 Current = nums[index]
#             index += 1
#         return ret


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 or n == 1:
            return n
        # nums[0,i]为非重复项
        i = 0
        j = i + 1
        while j <= n - 1:
            if nums[j] != nums[i]:
                # 指向同一个元素不需要赋值
                if i + 1 != j:
                    nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1, nums


print(Solution().removeDuplicates(nums=[0, 1, 1, 2]))
