class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # longest, start, visited = 0, 0, [False for _ in range(256)]
        # for i, char in enumerate(s):
        #     if visited[ord(char)]:
        #         while char != s[start]:
        #             visited[ord(s[start])] = False
        #             start += 1
        #         start += 1
        #     else:
        #         visited[ord(char)] = True
        #     longest = max(longest, i - start + 1)
        # return longest

        # 使用哈希表
        hash = {}
        max_length = 0
        start = 0
        for i, string in enumerate(s):
            if string in hash and start <= hash[string]:
                start = hash[string] + 1
            else:
                max_length = max(max_length, i - start + 1)
            hash[string] = i
        return max_length
