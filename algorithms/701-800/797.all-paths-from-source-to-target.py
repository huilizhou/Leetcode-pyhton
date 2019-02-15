# 所有可能的路径
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        tar = len(graph) - 1

        def dfs(start, path):
            if start == tar:
                res.append(path)
            for node in graph[start]:
                dfs(node, path + [node])
        dfs(0, [0])
        return res


print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))
