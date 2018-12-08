# 加一
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
            return digits

        #  人家的解法
        # plus = 1
        # ret = []
        # for d in digits[::-1]:
        #     v = d + plus
        #     if v > 9:
        #         v = v % 10
        #         plus = 1
        #     else:
        #         plus = 0
        #     ret.insert(0, v)
        # if plus == 1:
        #     ret.insert(0, plus)
        # return ret


print(Solution().plusOne([2, 9]))
