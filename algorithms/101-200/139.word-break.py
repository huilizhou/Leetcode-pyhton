# 单词拆分
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0]
        for i in range(len(s) + 1):
            for j in dp:
                if s[j:i] in wordDict:
                    dp.append(i)
                    break
        return dp[-1] == len(s)

        '''
        人家的解法
        动态规划。mark[i]用于表示0~i-1为下标范围的字符串能否被字典拆分
        如果 0 ~ j-1 范围的字符串在字典中，即 mark[j] = True，那么此时：
        如果 j ~ i 范围的字符串也在字典中，则 0 ~ i 范围的字符串可以被字典拆分（拆分为 0 ~ j-1 与 j ~ i），标记 mark[i] = True
        如果 j ~ i 范围的字符串不在字典中，继续循环，判断 mark[j + 1] 与 j+1 ~ i 范围字符的情况

        '''
        # mark = dict()
        # mark[0] = True

        # length = len(s)

        # for i in range(1, length + 1):
        #     for j in range(i):
        #         if j in mark:
        #             if mark[j] == True and (s[j:i] in wordDict):
        #                 mark[i] = True
        #                 break

        # if length in mark:
        #     return mark[length]
        # else:
        #     return False

        # 人家的解法
        # max_len = max([len(word) for word in wordDict]) if wordDict else 0
        # wordMap, n = set(wordDict), len(s)
        # dp = [0 for i in range(n + 1)]
        # dp[0] = 1
        # for i in range(1, n + 1):
        #     j, max_it = 1, min(i, max_len) + 1
        #     while not dp[i] and j < max_it:
        #         dp[i] = dp[i - j] and s[i - j:i] in wordMap
        #         j += 1
        # return dp[n] == 1


print(Solution().wordBreak("Ilovebytedance",
                           ["I", "love", "byte", "bytedance"]))
