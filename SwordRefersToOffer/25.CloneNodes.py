# 复杂链表的复制
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)

    # 复制原始链表的每个结点，将复制的结点链接在其原始结点的后面
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next

            pNode.next = pCloned
            pNode = pCloned.next

    # 将复制后的链表中的复制结点的random指针链接到被复制结点random指针后的一个结点
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 拆分链表，将原始链表的结点组成新的链表，复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedHead.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead
