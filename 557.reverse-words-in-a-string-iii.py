class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if s == '':
        #     return ''

        # ret = []
        # for word in s.split():
        #     ret.append(word[::-1])
        # return ' '.join(ret)

        # 别人的解法
        reversed_words = [word[::-1] for word in s.split(' ')]
        return ' '.join(reversed_words)


print(Solution().reverseWords("ab bc cd e"))
