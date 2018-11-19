class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
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


print(Solution().lengthOfLongestSubstring(""))
