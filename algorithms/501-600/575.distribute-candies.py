class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) // 2)


print(Solution().distributeCandies([1, 1, 2, 3, 4, 5]))
