# 单词规律
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # str = str.split(' ')
        # if len(pattern) != len(str):
        #     return False
        # dic = {}
        # for i in range(len(pattern)):
        #     if pattern[i] in dic:
        #         if str[i] != dic[pattern[i]]:
        #             return False
        #     else:
        #         if str[i] in dic.values():
        #             return False
        #         else:
        #             dic[pattern[i]] = str[i]
        # return True

        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        pairs = set(zip(pattern, words))
        return len(pairs) == len(set(words)) == len(set(pattern))


print(Solution().wordPattern("abba", "dog cat cat dog"))
