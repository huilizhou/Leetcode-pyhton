# -*- coding:utf-8 -*-
# 圆圈中最后剩下的数
'''
约瑟夫问题
n个人(编号从0~(n-1))，从0开始报数，报到(m-1)的退出，剩下的人继续从0开始报数。
我们知道第一个人(编号一定是m%n-1)出列后，剩下的n-1个人组成了一个新的约瑟夫环(以编号为k=m%n的人开始)
k,k+1,k+2,...n-2,n-1,0,1,2,k-2并且从k开始报0。

递推公式为
f[1]=0
f[i]=(f[i-1]+m)%i
'''


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


print(Solution().LastRemaining_Solution(41, 3))

'''
# 约瑟夫问题
# -*- coding: utf-8 -*- 
class Node(object):
	def __init__(self, value):
		self.value = value 
		self.next = None

def create_linkList(n):
	head = Node(1)
	pre = head
	for i in range(2, n+1):
		newNode = Node(i)
		pre.next= newNode
		pre = newNode
	pre.next = head
	return head

n = 5 #总的个数
m = 2 #数的数目
if m == 1: #如果是1的话，特殊处理，直接输出
	print (n)  
else:
	head = create_linkList(n)
	pre = None
	cur = head
	while cur.next != cur: #终止条件是节点的下一个节点指向本身
		for i in range(m-1):
			pre =  cur
			cur = cur.next
		print (cur.value)
		pre.next = cur.next
		cur.next = None
		cur = pre.next
	print (cur.value)
'''
