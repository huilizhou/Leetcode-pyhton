class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))

        # 别人的解法
        list = [0 for i in range(len(nums))]
        for num in nums:
            if list[num] == 1:
                return num
            else:
                list[num] = list[num] + 1


print(Solution().findDuplicate([3, 1, 3, 4, 2]))
