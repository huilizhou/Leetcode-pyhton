class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 最简单的做法
        if len(nums) <= 1:
            return [nums]
        import itertools
        return list(itertools.permutations(nums, len(nums)))

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

        # 我的另一种想法
        # if len(nums) <= 1:
        #     return [nums]
        # ans = []
        # for i, num in enumerate(nums):
        #     n = nums[:i] + nums[i + 1:]
        #     for temp_list in self.permute(n):
        #         ans.append([num] + temp_list)
        # return ans


print(Solution().permute([1, 2, 3]))
