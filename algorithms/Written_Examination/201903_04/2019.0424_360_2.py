# 矩阵中的最长递增路径
def longpath(matrix):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    if n == 0:
        return 0
    mem = [[False for i in range(n)]for i in range(m)]

    def dfs(i, j):
        if mem[i][j]:
            return mem[i][j]
        t = 1
        if i > 0 and matrix[i - 1][j] > matrix[i][j]:
            t = max(t, 1 + dfs(i - 1, j))
        if j > 0 and matrix[i][j - 1] > matrix[i][j]:
            t = max(t, 1 + dfs(i, j - 1))
        if i < m - 1 and matrix[i + 1][j] > matrix[i][j]:
            t = max(t, 1 + dfs(i + 1, j))
        if j < n - 1 and matrix[i][j + 1] > matrix[i][j]:
            t = max(t, 1 + dfs(i, j + 1))
        mem[i][j] = t
        return t
    res = 1
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))
    return res


print(longpath([

    [9, 9, 4],

    [6, 6, 8],

    [2, 1, 1]

]))
