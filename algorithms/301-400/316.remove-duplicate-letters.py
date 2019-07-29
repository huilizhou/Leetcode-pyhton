#  去除重复字母
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in s:
            if c not in ans:
                while ans and ord(ans[-1]) > ord(c) and dic[ans[-1]] > 0:
                    ans = ans[:-1]
                ans += c
            dic[c] -= 1
        return ans


print(Solution().removeDuplicateLetters('bcabc'))
