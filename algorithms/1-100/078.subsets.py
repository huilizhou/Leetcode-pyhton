# 子集
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # # 人家的解法，不断遍历
        # res = [[]]
        # for num in nums:
        #     for temp in res[:]:
        #         x = temp[:]
        #         x.append(num)
        #         res.append(x)
        # return res

        # 人家的解法，回溯算法
        res = []
        self.dfs(0, nums, res, [])
        return res

    def dfs(self, idx, nums, res, path):
        res.append(path)
        for i in range(idx, len(nums)):
            self.dfs(i + 1, nums, res, path + [nums[i]])
        return


print(Solution().subsets([1, 2, 3]))
