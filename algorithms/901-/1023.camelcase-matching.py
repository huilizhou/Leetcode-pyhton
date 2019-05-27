class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
    #     p = pattern
    #     return [self.singleMatch(q, p) for q in queries]

    # def singleMatch(self, query, pattern):
    #     idx = 0
    #     l = len(pattern)
    #     for i in query:
    #         if idx < l and i == pattern[idx]:
    #             idx += 1
    #         elif i <= "Z" and i >= "A":
    #             return False
    #     return idx == len(pattern)

        '''
        双指针法，q指向query的每个元素，p指向pattern的每个元素
        如果当前位都匹配上了，p、q都前进一步，
        如果没有匹配上，而且q还是大写，说明不对，
        如果没匹配上，q是小写，说明这一位是插入的小写字母，q+1即可，
        说明p已经匹配完了，而q还有很多的字母，就判断一下q中的剩下的字母是不是全为小写，
        如果不是，则不对；如是，代表这一个query是对的。
        '''
        def check(s):
            if not pattern:
                return True
            i = 0
            for j in range(len(s)):
                if s[j] == pattern[i]:
                    i += 1
                    if i == len(pattern):
                        return s[j + 1:] == s[j + 1:].lower()
                else:
                    if s[j] == s[j].upper():
                        return False
        res = [True if check(q) else False for q in queries]
        return res


print(Solution().camelMatch(
    ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB"))
