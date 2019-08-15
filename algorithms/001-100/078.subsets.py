# 子集
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 库函数 itertools.combinations()
        # import itertools
        # res = []
        # for i in range(len(nums) + 1):
        #     for tmp in itertools.combinations(nums, i):
        #         res.append(tmp)
        # return res

        # 人家的解法，迭代
        # res = [[]]
        # for num in nums:
        #     for temp in res[:]:
        #         x = temp[:]
        #         x.append(num)
        #         res.append(x)
        # return res

        # res = [[]]
        # for i in nums:
        #     res += [[i] + num for num in res]
        # return res

        # 回溯法
        res = []
        n = len(nums)

        def backtrack(i, tmp_list):
            res.append(tmp_list)
            for j in range(i, n):
                backtrack(j + 1, tmp_list + [nums[j]])
        backtrack(0, [])
        return res


print(Solution().subsets([1, 2, 3]))
