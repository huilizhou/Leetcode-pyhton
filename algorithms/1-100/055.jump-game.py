class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 我的想法
        # flag = 0
        # for i in range(len(nums)):
        #     if i > flag:
        #         return False
        #     flag = max(flag, nums[i] + i)
        # return True

        # 人家的解法，厉害
        # 从最后一位开始
        i = len(nums) - 1
        for j in range(len(nums) - 2, -1, -1):
            # 如果i位能被j位获取到
            if i - j <= nums[j]:
                # 我们的i位就往前挪
                i = j
        # 最后看i能不能到达第一位
        return i == 0


print(Solution().canJump([2, 1, 3, 0, 4]))
