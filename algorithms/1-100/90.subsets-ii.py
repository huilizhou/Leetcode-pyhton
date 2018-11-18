class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        sorted_nums = sorted(nums)
        for num in sorted_nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                if x not in res:
                    res.append(x)
        return res


print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))
