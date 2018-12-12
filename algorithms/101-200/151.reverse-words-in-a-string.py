# 翻转字符串里的单词
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(s.strip().split()[::-1])

        # 人家的思路
        # return ' '.join(reversed(s.split()))


print(Solution().reverseWords("the sky is blue"))
