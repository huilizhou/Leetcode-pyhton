class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest
