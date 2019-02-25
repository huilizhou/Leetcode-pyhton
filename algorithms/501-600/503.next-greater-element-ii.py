# 下一个更大的元素
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 人家的解法
        res = [-1] * len(nums)
        stack = []
        for i in list(range(len(nums))) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


print(Solution().nextGreaterElements([1, 2, 1]))
