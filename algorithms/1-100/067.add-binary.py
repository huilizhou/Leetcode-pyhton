class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

        # 人家的解法
        # i = len(a) - 1
        # j = len(b) - 1
        # carry = 0
        # result = ""
        # while i >= 0 or j >= 0 or carry:
        #     count = 0
        #     if i >= 0:
        #         if a[i] == '1':
        #             count += 1
        #         i -= 1
        #     if j >= 0:
        #         if b[j] == '1':
        #             count += 1
        #         j -= 1
        #     count += carry
        #     if count == 0:
        #         result += '0'
        #         carry = 0
        #     elif count == 1:
        #         result += '1'
        #         carry = 0
        #     elif count == 2:
        #         result += '0'
        #         carry = 1
        #     else:
        #         result += '1'
        #         carry = 1
        # return result[::-1]


print(Solution().addBinary(a="11", b="1"))
