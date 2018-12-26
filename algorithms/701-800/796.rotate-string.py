# 旋转字符串
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # 我的想法
        if len(A) != len(B):
            return False
        return (B + B).find(A) != -1


print(Solution().rotateString(A='abcde', B='cdeab'))
