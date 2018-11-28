class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法一 通过栈来判断当前位置对应的括号是否符合有效长度
        # 我的想法也是这样，用栈来解决
        stack = []
        max_len = 0
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

        # 动态规划的方法解决，我不太熟悉
        # dp[i]为到i处最长的有效信号，如果是s[i]为左括号，则dp[i]为0。
        # 因为若字符串是以左括号结束，则不可能是有效的。
        # 若为右括号，则有两种情况
        # 1.其前者s[i-1]为左括号，所以dp[i]=dp[i-2]+2;
        # 2.s[i-1]为右括号且s[i-dp[i-1]-1]为左括号，所以dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
        # 其中i-dp[i-1]-1对应最长括号的起始点

        # a = len(s)
        # if a < 2:
        #     return 0
        # # dp[i]表示刚刚好在s[i]之前(包括是[i]在内)的最长括号长度
        # # 如果s[i]="(",dp[i]=0
        # dp = [0 for _ in range(a)]
        # for i in range(1, a):
        #     # 当前i的对称点的索引
        #     pos = i - 1 - dp[i - 1]
        #     if s[i] == ")" and s[i - 1] == "(" and i - 2 >= 0:
        #         dp[i] = dp[i - 2] + 2
        #     elif s[i] == ")" and pos >= 0 and s[pos] == "(":
        #         dp[i] = dp[i - 1] + 2
        #         if pos - 1 >= 0:
        #             dp[i] += dp[i - dp[i - 1] - 2]
        # return max(dp)


print(Solution().longestValidParentheses(")(()))"))
