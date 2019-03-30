class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 人家的解法，动态规划
        # result = [[False for j in range(len(p) + 1)]
        #           for i in range(len(s) + 1)]

        # result[0][0] = True
        # for i in range(1, len(p) + 1):
        #     if p[i - 1] == "*":
        #         result[0][i] = result[0][i - 1]
        # for i in range(1, len(s) + 1):
        #     result[i][0] = False
        #     for j in range(1, len(p) + 1):
        #         if p[j - 1] != "*":
        #             result[i][j] = result[i - 1][j -
        #                                          1] and(s[i - 1] == p[j - 1] or p[j - 1] == "?")
        #         else:
        #             result[i][j] = result[i][j - 1] or result[i - 1][j]
        # return result[len(s)][len(p)]


if __name__ == "__main__":
    s = "aa"
    p = "a"
    print(Solution().isMatch(s, p))
