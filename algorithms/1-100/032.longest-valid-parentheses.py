class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法一 通过栈来判断当前位置对应的括号是否符合有效长度
        # 我的想法也是这样，用栈来解决
        # stack = []
        # max_len = 0
        # stack.append(-1)
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if len(stack) == 0:
        #             stack.append(i)
        #         else:
        #             max_len = max(max_len, i - stack[-1])
        # return max_len
        '''
        需要有一个变量start记录有效括号子串的起始下标，max表示最长有效括号的子串，初始值均为0。
        遍历给定字符串中所有的字符
        若当前下标s[i]=="("，则将当前字符下标i入栈，处理下一字符
        若当前字符s[i]==")"，判断当前栈是否为空
            若栈为空，则start=i+1，处理下一字符
            若栈不为空，则出栈，判断栈是否为空
                若为空，则max_len=max(max_len,i-start+1)
                若不为空，则max_len=max(max_len,i-stack[-1])
        '''
        max_len = 0
        start = 0
        stack = []
        for i in range(len(s)):
            # 如果是左括号，则直接入stack
            if s[i] == "(":
                stack.append(i)
            else:
                # 如果stack 里没有元素匹配，说明有效括号已经结束，更新起始的位置
                if len(stack) == 0:
                    start = i + 1
                    continue
                # 如果有匹配
                else:
                    stack.pop()
                    # pop出一个左括号匹配
                    # 如果此时stack没了，
                    if len(stack) == 0:
                        max_len = max(max_len, i - start + 1)
                    # 如果此时还有，则计算与栈顶的索引相减来计算长度
                    else:
                        max_len = max(i - stack[-1], max_len)
        return max_len

        # 动态规划的方法解决
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
