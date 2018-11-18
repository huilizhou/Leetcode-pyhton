class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # nums_sort = sorted(nums)
        # for i in range(0, len(nums_sort), 2):
        #     count += nums_sort[i]
        # return count

        return sum(sorted(nums)[::2])
