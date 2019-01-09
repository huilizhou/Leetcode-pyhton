class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        result = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            pre = result.pop()
            if nums[i] - pre[1] == 1:
                result.append([pre[0], nums[i]])
            else:
                result.append(pre)
                result.append([nums[i], nums[i]])
            print(result)
        return ['%s->%s' % (i[0], i[1]) if i[0] != i[1] else str(i[0]) for i in result]


print(Solution().summaryRanges([1, 4, 5, 6, 8, 9]))
