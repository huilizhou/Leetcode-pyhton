class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        level = 0
        for i in range(len(citations)):
            level = max(level, min(len(citations) - i, citations[i]))
        return level
