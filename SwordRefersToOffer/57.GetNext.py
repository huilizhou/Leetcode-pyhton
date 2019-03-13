# -*- coding:utf-8 -*-
# 二叉树的下一个结点
'''
我们以二叉树的中序遍历为例来分析如何找出二叉树的下一个结点
如果一个结点有右子树，那么它的下一个结点就是它的右子树的最左结点。
也就是从右子结点出发一直沿着左子树结点的指针，我们就能找到它的下一个结点。

接着我们分析一下没有右子树的情形，如果结点是它父结点的左子结点，那么它的下一个结点就是它的父结点。

如果一个结点既没有右子树，并且它还是父结点的右子结点，这种情景就比较复杂。
我们可以沿着指向父结点的指针一直向上遍历，直到找到一个是它父结点的左子结点的结点。
如果这样的结点存在，那么这个结点的父结点就是我们要找的下一个结点。
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        # 输入是一个空节点
        if pNode == None:
            return None
        pNext = None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode
        else:
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                if pNode.next:
                    pNext = pNode.next
        return pNext
