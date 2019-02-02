class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def junge(a, b, s):
            c = a + b
            temp = str(a) + str(b) + str(c)
            if s == temp:
                return True
            elif len(s) < len(temp):
                return False
            if s[:len(temp)] == temp:
                return junge(b, c, s[len(str(a)):])
            else:
                return False

        for i in range(1, len(num) // 2 + 1):
            a = int(num[:i])
            j = 1
            while j + i < (len(num) + i) // 2 + 1:
                b = int(num[i:i + j])
                if junge(a, b, num):
                    return True
                j += 1

        return False


print(Solution().isAdditiveNumber("199100199"))
