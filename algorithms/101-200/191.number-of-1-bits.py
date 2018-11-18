class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # count = 0
        # for i in range(len(bin(n))):
        #     if bin(n)[i] == '1':
        #         count += 1
        # return count
        return bin(n).count("1")


print(Solution().hammingWeight(3))
