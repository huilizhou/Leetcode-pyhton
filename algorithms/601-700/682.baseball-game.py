# 棒球比赛
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)


print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
