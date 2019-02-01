class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        if n == 0:
            return 0
        max_num = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not (set(words[i]) & set(words[j])):
                    max_num = max(max_num, len(words[i]) * len(words[j]))
        return max_num


print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
