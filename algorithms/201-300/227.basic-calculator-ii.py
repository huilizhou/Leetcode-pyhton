# 基本计算器
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        op = '+'
        for i, each in enumerate(s):
            if each.isdigit():
                num = num * 10 + int(each)
            if each in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    b = stack.pop()
                    a = num
                    if int(a) * int(b) < 0:
                        stack.append(-(abs(int(b)) // abs(int(a))))
                    else:
                        stack.append(int(b // a))
                num = 0
                op = each
        return sum(stack)


print(Solution().calculate("14-3/2"))
