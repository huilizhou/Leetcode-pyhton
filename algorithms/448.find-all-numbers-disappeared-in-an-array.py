class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 超时了。
        # res = []
        # for i in range(1, len(nums) + 1):
        #     if i not in nums:
        #         res.append(i)
        # return res

        # return list(set(range(1, len(nums) + 1)) - set(nums))

        return [i for i in range(1, len(nums) + 1) if i not in set(nums)]


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
