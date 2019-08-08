# 前K个高频单词
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # # 我的想法，字典排序
        # dic = {}
        # for i in words:
        #     dic[i] = dic.get(i, 0) + 1
        # return sorted(dic.keys(), key=lambda x: (-dic[x], x))[:k]

        # 人家的写法
        import collections
        import heapq
        c = collections.Counter(words)
        return heapq.nsmallest(k, c, lambda s: [-c[s], s])


print(Solution().topKFrequent(
    ["i", "love", "leetcode", "i", "love", "coding"], 2))
