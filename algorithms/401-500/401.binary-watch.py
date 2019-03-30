# 二进制手表
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # 直接求解，统计其中二进制1的个数
        res = []
        for hour in range(12):
            for minute in range(60):
                if ((bin(hour) + bin(minute)).count("1")) == num:
                    res.append('%d:%02d' % (hour, minute))
        return res


print(Solution().readBinaryWatch(1))
