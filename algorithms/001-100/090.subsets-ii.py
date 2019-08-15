# 子集II
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 迭代法
        # res = [[]]
        # nums.sort()

        # for num in nums:
        #     for temp in res[:]:
        #         x = temp[:]
        #         x.append(num)
        #         if x not in res:
        #             res.append(x)
        # return res

        # 回溯法
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(i, n, tmp_list):
            if tmp_list not in res:
                res.append(tmp_list)
            for j in range(i, n):
                backtrack(j + 1, n, tmp_list + [nums[j]])

        backtrack(0, n, [])
        return res


print(Solution().subsetsWithDup([1, 2, 2]))
