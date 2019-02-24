# 相对名次
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortedNums = sorted(nums, reverse=True)
        maps = {}
        for i in range(len(sortedNums)):
            maps[sortedNums[i]] = i + 1
        for i in range(len(nums)):
            if maps[nums[i]] == 1:
                nums[i] = "Gold Medal"
            elif maps[nums[i]] == 2:
                nums[i] = "Silver Medal"
            elif maps[nums[i]] == 3:
                nums[i] = "Brozen Medal"
            else:
                nums[i] = str(maps[nums[i]])
        return nums


print(Solution().findRelativeRanks([1, 2, 3, 4, 5]))
