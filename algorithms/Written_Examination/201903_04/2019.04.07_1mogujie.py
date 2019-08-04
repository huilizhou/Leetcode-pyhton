def solve(s, n):
    if len(s) < n or n < 0:
        return -1
    res = []
    for i in range(0, len(s) - n + 1):
        res.append(s[i:n + i])
    return " ".join(res)


import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    print(solve(s, n))
    # s = '12345678'
    # n = 1
    # print(solve(s, n))
