# 最小覆盖子串
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        lens, lent = len(s), len(t)
        if lent == 0 or lens == 0 or lens < lent:
            return ""
        d = defaultdict(int)
        for ch in t:
            d[ch] = d[ch] + 1
        total, start, m = lent, 0, lens + 1
        right, left = 0, 0
        for right in range(lens):
            if d[s[right]] > 0:
                total -= 1
            d[s[right]] -= 1
            while total == 0:
                if right - left + 1 < m:
                    m = right - left + 1
                    start = left
                d[s[left]] += 1
                if d[s[left]] > 0:
                    total += 1
                left += 1
        return s[start:start + m] if m < lens + 1 else ""


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
