class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return str(int(num1) * int(num2))

        # 人家的解法
        res = 0
        for i in range(len(num2) - 1, -1, -1):
            per_res = 0
            for j in range(len(num1) - 1, -1, -1):
                per_res += int(num2[i]) * int(num1[j]) * \
                    10**(len(num1) - j - 1)

            # print(per_res)
            res += per_res * 10**(len(num2) - i - 1)

        return str(res)


print(Solution().multiply("22", "32"))
