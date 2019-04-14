class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 位操作的方法
        '''
        4的幂一定是2的。
        4的幂和2的幂一样，只会出现一位1。但是，4的1总是出现在奇数位。
        0x5 = 0101b可以用来校验奇数位上的1。
        '''
        return ((num - 1) & num) == 0 and (num & 0x55555555) != 0

        # # 常规思路，和判断2的幂次方、判断3的幂次方类似。
        # if num <= 0:
        #     return False

        # while num % 4 == 0:
        #     num = num // 4

        # return num == 1

        # # 人家的写法
        # res = [1]
        # sum = 1
        # while(sum < 2**31):
        #     sum = sum * 4
        #     res.append(sum)
        # if num in res:
        #     return True
        # else:
        #     return False


print(Solution().isPowerOfFour(16))
