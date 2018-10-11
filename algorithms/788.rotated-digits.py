class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 我的解法，有想法之后，在参考别人基础之上写的。

        count = 0
        for i in range(1, N + 1):
            if '3'in str(i) or '4'in str(i) or '7' in str(i):
                continue
            elif '2'in str(i) or '5' in str(i) or '6' in str(i) or '9' in str(i):
                count += 1
            else:
                continue
        return count

        #  人家的解法
        # invalid, diff = set(['3', '4', '7']), set(['2', '5', '6', '9'])
        # result = 0
        # for i in range(N + 1):
        #     lookup = set(list(str(i)))
        #     if invalid & lookup:
        #         continue
        #     if diff & lookup:
        #         result += 1
        # return result


print(Solution().rotatedDigits(10))
