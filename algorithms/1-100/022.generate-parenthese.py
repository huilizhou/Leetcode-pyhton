class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 如果左括号还有剩余，则可以放置左括号
        # 如果右括号剩余数大于左括号，则可以放置右括号

        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result

    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(
                result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(
                result, current + ")", left, right - 1)


print(Solution().generateParenthesis(3))
