# 全排列
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 最简单的做法，调用itertools
        # if len(nums) <= 1:
        #     return [nums]
        # import itertools
        # return list(itertools.permutations(nums, len(nums)))

        # 人家的解法
    #     result = []
    #     used = [False] * len(nums)
    #     self.permuteRecu(result, used, [], nums)
    #     return result

    # def permuteRecu(self, result, used, cur, num):
    #     if len(cur) == len(num):
    #         result.append(cur[:])
    #         return
    #     for i in range(len(num)):
    #         if not used[i]:
    #             used[i] = True
    #             cur.append(num[i])
    #             self.permuteRecu(result, used, cur, num)
    #             cur.pop()
    #             used[i] = False

        # 我看了人家解法后的想法
        res = []
        if len(nums) <= 1:
            return [nums]
        for i in range(len(nums)):
            num = nums[i]
            newnums = nums[:i] + nums[i + 1:]
            for item in self.permute(newnums):
                res.append([num] + item)
        return res


print(Solution().permute([1, 2, 3]))
