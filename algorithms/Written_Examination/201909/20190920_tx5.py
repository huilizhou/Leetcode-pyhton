import sys


if __name__ == "__main__":
    # x是否是y的前缀
    def match(x, y):
        if len(x) > len(y):
            return False
        else:
            for i in range(len(x)):
                if x[i] != y[i]:
                    return False
            return True

    res = []
    line1 = sys.stdin.readline().strip()
    m, n = list(map(int, line1.split()))
    for _ in range(m):
        line = sys.stdin.readline().strip()
        res.append(line)
    res.sort()
    for _ in range(n):
        linex = sys.stdin.readline().strip(" ")
        s1, s2 = list(map(str, linex.split()))
        flag = 0
        for i in res:
            if match(s1, i) and not match(s2, i):
                print(i)
                res.remove(i)
                flag = 1
                break
        if flag == 0:
            print(-1)
