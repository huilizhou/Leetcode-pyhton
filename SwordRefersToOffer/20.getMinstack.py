# -*- coding:utf-8 -*-
# 包含min函数的栈
'''
使用两个stack，一个为数据栈，一个为辅助栈。数据栈用于存储所有的数据，辅助栈用于存储最小值。
举个例子：
入栈的时候，首先往空的数据栈里压入数字3，显然现在3是最小值，我们也把最小值压入辅助栈。
接下来往数据栈压入数字4.由于4大于之前的最小值，因此我们只要入数据栈，不压入辅助栈。
出栈的时候，当数据栈和辅助栈的栈顶元素相同的时候，辅助栈的栈顶元素出栈。否则，数据栈的栈顶元素出栈。
获得栈顶元素的时候，直接返回数据栈的栈顶元素
栈最小元素，直接返回辅助栈的栈顶元素。


'''

# class Solution:
#     def __init__(self):
#         self.stack = []  # 数据栈
#         self.minVal = []  # 最小值栈

#     def push(self, node):
#         self.stack.append(node)
#         if len(self.minVal) == 0:
#             self.minVal.append(node)
#         else:
#             if node > self.minVal[-1]:
#                 node = self.minVal[-1]
#             self.minVal.append(node)

#     def pop(self):
#         self.minVal.pop()
#         self.stack.pop()

#     def top(self):
#         return self.stack[-1]

#     def min(self):
#         return self.minVal[-1]


class Solution:
    def __init__(self):
        self.Data = []   # 数据栈
        self.minVal = []  # 最小值栈

    def push(self, node):
        if len(self.minVal) == 0:
            self.minVal.append(node)
        else:
            if self.minVal[-1] > node:
                self.minVal.append(node)
        self.Data.append(node)

    def pop(self):
        if self.Data[-1] == self.minVal[-1]:
            self.minVal.pop()
        self.Data.pop()

    def top(self):
        return self.Data[-1]

    def min(self):
        return self.minVal[-1]
