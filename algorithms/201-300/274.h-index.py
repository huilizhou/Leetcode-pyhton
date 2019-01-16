class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        level = 0
        for i in range(len(citations)):
            level = max(level, min(len(citations) - i, citations[i]))
        return level


print(Solution().hIndex([3, 0, 6, 1, 5]))
