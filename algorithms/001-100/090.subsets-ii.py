# 子集II
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()

        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                if x not in res:
                    res.append(x)
        return res


print(Solution().subsetsWithDup([1, 2, 2]))
