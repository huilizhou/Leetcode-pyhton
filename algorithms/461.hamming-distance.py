class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c = x ^ y
        return bin(c).count('1')


print(Solution().hammingDistance(2, 3))
