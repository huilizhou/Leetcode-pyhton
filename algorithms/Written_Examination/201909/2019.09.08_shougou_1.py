# 没有思路
import sys

if __name__ == "__main__":

    line1 = sys.stdin.readline().strip()
    k, n = list(map(int, line1.split()))
    count = n
    for i in range(n):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        m = values[0]
        father = values[1]
        child = values[1:]
        if len(child) > k:
            count += len(child) // k
    print(count)
