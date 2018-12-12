# 加一
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # for i in range(len(digits) - 1, -1, -1):
        #     if digits[i] < 9:
        #         digits[i] = digits[i] + 1
        #         return digits
        #     else:
        #         digits[i] = 0
        # if digits[0] == 0:
        #     digits.insert(0, 1)
        #     return digits

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

        # 把列表里的数字转换成数字
        # 空间复杂度变大
        nums = 0
        res = []
        for index, num in enumerate(digits):
            nums += num * pow(10, len(digits) - index - 1)
        nums += 1

        for ch in str(nums):
            res.append(int(ch))
        return res


print(Solution().plusOne([2, 9]))
