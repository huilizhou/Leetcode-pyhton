class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stcak = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stcak:
            self.stcak.append(0)
            self.min = x
        else:
            self.stcak.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.stcak.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        """
        :rtype: int
        """
        x = self.stcak[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# 第二种方式
# class MinStack:
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stcak = []  # 数据栈
#         self.minVal = []  # 最小值栈

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stcak.append(x)  # push元素
#         if len(self.minVal) == 0:
#             self.minVal.append(x)
#         else:
#             if x > self.minVal[-1]:
#                 x = self.minVal[-1]
#             self.minVal.append(x)

#     def pop(self):
#         """
#         :rtype: void
#         """
#         self.minVal.pop()
#         self.stcak.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stcak[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.minVal[-1]
