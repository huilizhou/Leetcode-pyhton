# -*- coding:utf-8 -*-
# 栈的压入、弹出序列
'''
借用一个辅助的栈，遍历压栈顺序，先将第一个放入栈中，这里是1。
然后判断栈顶元素是不是出栈顺序的第一个元素，这里是4，很显然1不等于4。
所以我们继续压栈，直到相等之后开始出栈。
出栈一个元素，则出栈顺序向后移动一位，直到不相等，这样循环等压栈顺序遍历完成。
如果辅助栈还不为空，如果辅助栈还不为空，说明弹出序列不是栈的弹出顺序。
'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(popV) == 0 or len(popV) != len(pushV):
            return False
        stackData = []
        for i in pushV:
            stackData.append(i)
            while len(stackData) and stackData[-1] == popV[0]:
                stackData.pop()
                popV.pop(0)
        if len(stackData):
            return False
        return True


print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 2, 1]))
