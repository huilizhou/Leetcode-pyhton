'''
题目描述

世界杯开幕会在球场C举行，球场C的球迷看台可以容纳M*N个球迷。在球迷售票完成后，
现官方想统计此次开幕式一共有多少球队的球迷群体，最大的球迷群体有多少人。

经调研发现，球迷群体在选座时有以下特性：
- 同球队的球迷群体会选择相邻座位，不同球队的球迷群体会选择不相邻的座位。
（注解：相邻包括前后相邻，左右相邻，斜对角相邻）
- 给定一个M*N的二维球场，0代表该位置没有坐人，1代表该位置已有球迷，希望输出球队群体个数P
最大球队群体人数Q

输入描述

第一行，2个数字，M及N,使用英文逗号分割；
接下来M行，每行N的数字，使用英文逗号分割；

输出描述：
一行，2个数字，P及Q，使用英文逗号分割；
其中，P表示球队群体个数，Q表示最大的球队群体人数。

'''
'''
思路：
- dfs搜索联通域
- 原题只搜索4个方向，这里改为搜索8个方向
'''
# 输入处理
M, N = list(map(int, input().split(',')))

book = []
for i in range(M):
    line = list(map(int, input().split(',')))
    book.append(line)


class Solution:
    def __init__(self, pos):
        self.pos = pos
        self.cnt = 0   # 记录当前区域的人数
        self.dp = []   # 保存所有区域的人数，返回其长度，及其中的最大值

    def dfs(self, i, j):
        if 0 <= i <= M and 0 <= j <= N:
            if self.pos[i][j] == 1:
                self.cnt += 1
                self.pos[i][j] = 0   # 遍历过的就置零，避免重复搜索
                # 八个方向搜索
                self.dfs(i - 1, j)
                self.dfs(i + 1, j)
                self.dfs(i, j - 1)
                self.dfs(i, j + 1)
                self.dfs(i - 1, j - 1)
                self.dfs(i + 1, j + 1)
                self.dfs(i + 1, j - 1)
                self.dfs(i - 1, j + 1)

    def solve(self):
        for i in range(M):
            for j in range(N):
                if self.pos[i][j] == 1:
                    self.cnt = 0  # 每找到一个区域就清零人数，重新计数
                    self.dfs(i, j)  # 深度优先搜索每个点
                    if self.cnt > 0:
                        self.dp.append(self.cnt)
        return len(self.dp), max(self.dp)


s = Solution(book)
P, Q = s.solve()
print(str(P) + ',' + str(Q))
