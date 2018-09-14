class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1], 2)
        # return int(bin(n)[len((bin(n))) - 1:1:-1], 2)


print(Solution().reverseBits(12345))
