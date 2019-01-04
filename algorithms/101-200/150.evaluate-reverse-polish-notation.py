# 逆波兰表达式求值
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 我的想法
        stack = []
        cal = {"+": lambda x, y: x + y, "-": lambda x, y: x - y,
               "*": lambda x, y: x * y, "/": lambda x, y: int(x / y)}

        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(cal[i](a, b))
        return stack[0]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
