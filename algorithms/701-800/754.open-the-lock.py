from queue import Queue


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)  # in 操作在set中时间复杂度为O(1)
        if '0000' in deadends:
            return -1

        # 初始化根节点
        q = Queue()
        q.put(('0000', 0))  # (当前节点值，转动步数)

        # 开始循环队列
        while not q.empty():

            # 取出一个节点
            node, step = q.get()

            # 放入周围节点
            for i in range(4):
                for add in (1, -1):
                    cur = node[:i] + str((int(node[i]) + add) %
                                         10) + node[i + 1:]
                    if cur == target:
                        return step + 1
                    if not cur in deadends:
                        q.put((cur, step + 1))
                        deadends.add(cur)  # 避免重复搜索

        return -1


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
