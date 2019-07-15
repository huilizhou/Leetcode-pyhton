# 单词拆分II
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, map):
        if s in map:
            return map[s]
        if not s:
            return ['']

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            # 递归解决剩余的部分
            # 每一个item都是一种以word开头可能的拆分方案
            for item in self.dfs(s[len(word):], wordDict, map):
                item = word + ('' if item == '' else ' ') + item
                res.append(item)
        map[s] = res
        return res


print(Solution().wordBreak(s="catsanddog", wordDict=[
      "cat", "cats", "and", "sand", "dog"]))
