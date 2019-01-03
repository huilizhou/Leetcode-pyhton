class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        count = 0
        maxcount = 0
        for _, seat in enumerate(seats):
            if seat == 1:
                if count > maxcount:
                    maxcount = count
                count = 0
            else:
                count += 1
        return max((maxcount + 1) // 2, count, seats.index(1))


print(Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
