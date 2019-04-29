# 字符串中的单词数
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 人家的解法
        s = s.strip()
        if len(s) == 0:
            return 0
        else:
            sum = 0
            s = s.split(' ')
            for v in s:
                if v != '':
                    sum += 1
            return sum

        # return len(s.split())


print(Solution().countSegments("Hello, my name is John"))
