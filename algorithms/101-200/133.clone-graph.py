# 客隆图
# Definition for a Node.


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 深度优先遍历
        visited = {}

        def dfs(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            clone = Node(node.val, [])
            visited[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)
