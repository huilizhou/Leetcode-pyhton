# 逆波兰表达式求值
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 我的想法
        stack = []
        for e in tokens:
            if e == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif e == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif e == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif e == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(e))
        return stack[0]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
