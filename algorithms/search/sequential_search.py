'''
顺序查找，又叫线性查找，是最基本的查找技术。
它的查找过程是，从表中第一个记录开始，逐个进行记录的关键字和给定值比较。
若某个元素匹配关键字，则查找成功。若查找到最后一个元素还未匹配关键字，则查找失败。
时间复杂度为O(n)

'''


class Solution:
    def seq_search(self, list, value):
        for i in range(len(list)):
            if list[i] == value:
                return i
        return False


print(Solution().seq_search([2, 3, 1, 4, 5, 8], 3))
