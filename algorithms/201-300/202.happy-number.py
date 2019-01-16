class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 人家的解法
        # result = 0
        # while result != 1 and result != 4:
        #     result = 0
        #     n = str(n)
        #     for i in n:
        #         result += int(i) ** 2
        #     n = result
        # if result == 1:
        #     return True
        # return False

        # 别人的解法
        lookup = []
        # print(n)
        while n != 1 and n not in lookup:
            lookup.append(n)
            n = self.next(n)
            # print(n)
        return n == 1

    def next(self, n):
        ret = 0
        for ch in str(n):
            ret += int(ch)**2
        return ret


print(Solution().isHappy(20))
