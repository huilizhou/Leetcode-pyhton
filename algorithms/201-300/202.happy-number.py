class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        while result != 1 and result != 4:
            result = 0
            n = str(n)
            for i in n:
                result += int(i) ** 2
            n = result
        if result == 1:
            return True
        return False
