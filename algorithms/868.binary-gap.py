class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        # 我的思路与此类似，20181008，没有想到
        # s = bin(N)[2:].strip('0')
        # if s.count('1') < 2:
        #     return 0
        # s = s.split('1')
        # s = [len(x) for x in s]
        # return max(s) + 1

        # 人家的解法，位操作。这种思路比较好。
        result = 0
        last = None
        for i in range(32):
            if (N >> i) & 1:
                if last is not None:
                    result = max(result, i - last)
                last = i
        return result
