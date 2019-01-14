# 字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 我的起初想法，超时
        # if not s:
        #     return -1
        # res = []
        # for index, value in enumerate(s):
        #     if s.count(value) == 1:
        #         res.append(index)
        # if not res:
        #     return -1
        # else:
        #     return min(res)

        # 人家的解法一：
        # s = list(s)
        # dict = {}
        # for num in s:
        #     dict[num] = dict.get(num, 0) + 1
        # for i in range(len(s)):
        #     if dict[s[i]] == 1:
        #         return i
        # return -1

        # 人家的解法，和我超时思路类似
        res = []
        for i in set(s):
            if s.find(i) == s.rfind(i):
                res.append(s.rfind(i))
        return min(res) if len(res) > 0 else -1

        # 我的想法
        # dict_1 = {}
        # for i in s:
        #     if i not in dict_1:
        #         dict_1[i] = 0
        #     dict_1[i] += 1
        # for j in dict_1:
        #     if dict_1[j] == 1:
        #         return s.index(j)
        # return - 1


print(Solution().firstUniqChar("loveleetcode"))
