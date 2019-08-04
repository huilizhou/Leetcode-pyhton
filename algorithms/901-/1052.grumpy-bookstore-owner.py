# 爱生气的书店老板
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        # count = 0
        # for i in range(len(customers)):
        #     if grumpy[i] == 0:
        #         count = count + customers[i]
        #         customers[i] = 0
        # max = 0
        # window = 0
        # for i in range(X):
        #     window += customers[i]
        # max = window
        # for j in range(X, len(customers)):
        #     window = window - customers[j - X] + customers[j]
        #     if window > max:
        #         max = window
        # return count + max

        count = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                count += customers[i]
                customers[i] = 0

        window = sum(customers[:X])
        Max = window
        for j in range(X, len(customers)):
            window = window + customers[j] - customers[j - X]
            Max = max(window, Max)
        return count + Max


print(Solution().maxSatisfied(
    [1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
