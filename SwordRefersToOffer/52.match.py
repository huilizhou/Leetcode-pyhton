# -*- coding:utf-8 -*-
# 正则表达式匹配


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        elif len(s) != 0 and len(pattern) == 0:
            return False
        elif len(s) == 0 and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                return False
        else:
            if len(pattern) > 1 and pattern[1] == "*":
                if s[0] != pattern[0] and pattern[0] != ".":
                    return self.match(s, pattern[2:])
                else:
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s[1:], pattern[1:])
                else:
                    return False


print(Solution().match("aaa", "a.a"))
