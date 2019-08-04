import sys


def solve(n, nums):
    res = []
    for i in range(n):
        tmp = []
        for j in range(n - i):
            tmp.append(max(nums[j:j + 1 + 1]))
        res.append(min(tmp))
    return res


# a = int(input())
# list = int(input())
# print(solve(a, b))
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    print(solve(n, values))
    # print(solve(6, [1, 3, 2, 4, 6, 5]))
