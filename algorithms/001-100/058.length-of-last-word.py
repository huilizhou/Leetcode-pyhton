# 最后一个单词的长度
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 我的想法
        if len(s.split()) == 0:
            return 0
        else:
            return len(s.split()[-1])

        # 人家的做法
        # data = s.strip().split(' ')
        # return len(data.pop())


print(Solution().lengthOfLastWord("Hello World"))
