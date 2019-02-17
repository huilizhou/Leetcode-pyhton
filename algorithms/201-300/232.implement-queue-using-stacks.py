# 用栈来实现队列
# 我的想法
# 入栈时数据存入栈stackIn，出栈时数据从stackOut弹出。
# 执行入栈操作时，将数据源源不断的压入栈stackIn;
# 执行出栈操作时，将stackIn的数据一次性全部弹出，存入到stackOut中。
# 当stackOut中的数据为空后，再将新入栈stackIn的数据一次性存入stackOut中即可。


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackIN, self.stackOut = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stackIN.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.stackOut.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stackOut:
            while self.stackIN:
                self.stackOut.append(self.stackIN.pop())
        return self.stackOut[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stackIN and not self.stackOut


# 人家的解法，用一个栈
# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.a = []


#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         self.a.append(x)
#         self.a[0], self.a[1:] = self.a[-1], self.a[:-1]

#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         return self.a.pop()


#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         return self.a[-1]


#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         return len(self.a) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
