# 删除最外层的括号
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = 0
        res = ""
        for c in S:
            if c == "(":
                l += 1
                if l > 1:
                    res += c
            else:
                if l > 1:
                    res += c
                l -= 1
        return res


print(Solution().removeOuterParentheses("(()()"))
