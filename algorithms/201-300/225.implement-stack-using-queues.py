# 用队列实现栈
# class MyStack:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.l = []

#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: void
#         """
#         self.l.append(x)

#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         return self.l.pop()

#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         return self.l[-1]

#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         return self.l == []


# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()


# 人家的写法
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if not self.stack1:
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop(0))
        else:
            self.stack2.append(x)
            while self.stack1:
                self.stack2.append(self.stack1.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack1.pop(0) if self.stack1 else self.stack2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack1[0] if self.stack1 else self.stack2[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2
