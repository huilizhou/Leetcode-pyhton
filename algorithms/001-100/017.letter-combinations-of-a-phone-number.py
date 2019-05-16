# 电话号码的字母组合
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 我的想法
        if not digits:
            return []

        digit2chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                       '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [i for i in digit2chars[digits[0]]]

        # 遍历每一个数字
        # m+n:m和n的不重叠的组合

        for i in digits[1:]:
            res = [m + n for m in res for n in digit2chars[i]]

        return res


print(Solution().letterCombinations('27'))


# # 递归的方法
# class Solution:
#     def listCombinations(self, list_1, list_2):
#         ans = []
#         if len(list_1) == 0:
#             return list_2
#         if len(list_2) == 0:
#             return list_1
#         for c1 in list_1:
#             for c2 in list_2:
#                 ans.append(c1 + c2)
#         return ans

#     def letterCombinations(self, digits):
#         """
#         :type digits:str
#         :rtype: List[str]
#         """
#         ans = []
#         digit2chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#                        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

#         for n in digits:
#             list_1 = list(digit2chars[n])
#             ans = self.listCombinations(ans, list_1)
#         return ans


# print(Solution().letterCombinations('27'))
