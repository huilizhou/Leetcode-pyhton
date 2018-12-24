# 颠倒二进制位
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # return int('{:032b}'.format(n)[::-1], 2)

        return int(bin(n)[2:].zfill(32)[::-1], 2)


print(Solution().reverseBits(12345))
