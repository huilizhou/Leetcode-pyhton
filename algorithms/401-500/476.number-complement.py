# 数字的补数
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        # 我的解法
        # z = bin(num)[2:]
        # z1 = ''
        # for i in z:
        #     if i == '1':
        #         z1 += '0'
        #     else:
        #         z1 += '1'
        # res = int(z1, 2)
        # return res

        # 人家的解法
        # i = 1
        # while num > i:
        #     num ^= i
        #     i <<= 1
        # return num

        # 人家的解法
        '''
        解题思路：找到一个二进制位数与num相同但每一位都为1的数，然后用这个数减去num。
        例如0b111-0b101=0b10,7-5=2,这里的7就是我们要找的数字。
        # 人家的解法
        # return 2 ** (len(bin(num)) - 2) - 1 - num
        '''
        i = 1
        while num >= i:
            i = i << 1
        return i - 1 - num


print(Solution().findComplement(2))
