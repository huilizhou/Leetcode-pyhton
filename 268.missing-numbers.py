class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums) + 1):
            res.append(i)
        a = set(res) - set(nums)
        for e in a:
            return e

        # return sum(range(len(nums) + 1)) - sum(nums)


print(Solution().missingNumber([0]))
