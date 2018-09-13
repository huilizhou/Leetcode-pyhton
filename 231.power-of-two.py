class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return bin(n).count("1") == 1


print(Solution().isPowerOfTwo(-16))
