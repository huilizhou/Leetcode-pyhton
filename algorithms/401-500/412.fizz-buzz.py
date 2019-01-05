# Fizz Buzz
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 我的解法
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 5 == 0:
                res.append("Buzz")
            elif i % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(i))
        return res


print(Solution().fizzBuzz(15))
