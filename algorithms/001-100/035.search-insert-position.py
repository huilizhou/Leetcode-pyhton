# 搜索插入的位置
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 我的想法
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     return sorted(nums).index(target)

        # # 不用内置函数的做法
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if target == nums[mid]:
        #         return mid
        #     if target > nums[mid]:
        #         l += 1
        #     else:
        #         r -= 1
        # return l

        # # 人家的写法，很不错
        for index, value in enumerate(nums):
            if target == value:
                return index
            else:
                if target < value:
                    return index
                elif target > nums[-1]:
                    return len(nums)


print(Solution().searchInsert([1, 3, 5, 6], 4))
