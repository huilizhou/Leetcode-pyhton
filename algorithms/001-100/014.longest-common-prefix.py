# 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 人家的想法
        # if not strs:
        #     return ""

        # mins = min(strs)
        # maxs = max(strs)
        # s = ""
        # for i in range(min(len(mins), len(maxs))):
        #     if (mins[i] == maxs[i]):
        #         s += mins[i]
        #     else:
        #         break
        # return s

        # 我的想法，先找出列表中长度最短的那个值。
        # 最长公共子缀肯定比最短的还要短。
        # if not strs:
        #     return ""

        # m = len(strs[0])
        # flag = True
        # s = ""

        # for i in range(len(strs)):
        #     m = min(m, len(strs[i]))

        # for j in range(m):
        #     for i in range(len(strs)):
        #         if strs[0][j] != strs[i][j]:
        #             flag = False
        #             break
        #     if flag == True:
        #         s += strs[0][j]
        # return s

        # pythonic的一种解法
        s = " "
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
