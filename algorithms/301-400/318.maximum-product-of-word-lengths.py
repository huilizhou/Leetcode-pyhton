# 最大单词长度乘积
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 我的想法，比较慢
        # n = len(words)
        # if n == 0:
        #     return 0
        # max_num = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if not (set(words[i]) & set(words[j])):
        #             max_num = max(max_num, len(words[i]) * len(words[j]))
        # return max_num

        # 人家的解法，位操作
        # max = 0
        # bit = [0 for _ in range(len(words))]
        # for i in range(len(words)):
        #     for j in range(len(words[i])):
        #         bit[i] |= 1 << (ord(words[i][j]) - ord("a"))

        # for i in range(len(words)):
        #     for j in range(i + 1, len(words)):
        #         if bit[i] & bit[j]:
        #             continue
        #         else:
        #             if len(words[i]) * len(words[j]) > max:
        #                 max = len(words[i]) * len(words[j])
        # return max

        # 人家的解法
        # if not words:
        #     return 0
        # d = {}
        # for word in words:
        #     mask = 0
        #     for c in word:
        #         mask |= 1 << (ord(c) - 97)
        #     d[mask] = max(d.get(mask, 0), len(word))
        # return max([d[x] * d[y] for y in d for x in d if x & y == 0] or [0])

        # 人家的写法
        from collections import defaultdict
        lookup = defaultdict(int)
        for word in words:
            flag = 0
            for alp in word:
                flag |= 1 << ord(alp) - 97
            lookup[flag] = max(lookup[flag], len(word))
        return max([lookup[x] * lookup[y] for x in lookup for y in lookup if x & y == 0])


print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
