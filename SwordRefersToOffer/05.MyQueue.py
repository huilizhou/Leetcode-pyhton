# -*- coding:utf-8 -*-
# 用两个栈实现队列
'''
栈的特点是先进后出，队列的特点是先进先出。
我们用两个栈正好能把顺序反过来实现类似的队列的操作。

实际上必须做到以下两点。
1. 如果stackPush要往stackPop中压入数据，那么必须一次性把stackPush中的数据全部压入。
2. 如果stackPop中不为空，stackPush绝对不能往stackPop中压入数据。

'''


class Solution:
    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def push(self, node):
        # write code here
        self.stackPush.append(node)

    def pop(self):
        # return xx
        if len(self.stackPop) == 0:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()
