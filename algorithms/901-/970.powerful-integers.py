class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        for i in range(18):
            for j in range(18):
                v = x**i + y**j
                if v <= bound:
                    res.append(v)
        return list(set(res))


print(Solution().powerfulIntegers(x=2, y=3, bound=10))
