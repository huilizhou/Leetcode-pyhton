# 使括号有效的最少添加
class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        cur_left = 0
        cur_right = 0
        for item in S:
            if item == "(":
                cur_left += 1
            else:
                if cur_left >= 1:
                    cur_left -= 1
                else:
                    cur_right += 1
        return cur_left + cur_right


print(Solution().minAddToMakeValid("())"))
