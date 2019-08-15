# 全排列
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 库函数
        # if len(nums) <= 1:
        #     return [nums]
        # import itertools
        # return list(itertools.permutations(nums, len(nums)))

        # # 递归法
        res = []
        if len(nums) <= 1:
            return [nums]
        for i in range(len(nums)):
            num = nums[i]
            newnums = nums[:i] + nums[i + 1:]
            for item in self.permute(newnums):
                res.append([num] + item)
        return res

        # 回溯法
        # if not nums:
        #     return []
        # res = []
        # n = len(nums)
        # visited = [0] * n

        # def backtrack(i, tmp_list):
        #     if i == n:
        #         res.append(tmp_list)
        #     for j in range(n):
        #         if visited[j]:
        #             continue
        #         visited[j] = 1
        #         backtrack(i + 1, tmp_list + [nums[j]])
        #         visited[j] = 0

        # backtrack(0, [])
        # return res


print(Solution().permute([1, 2, 3]))
