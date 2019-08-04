# def solve(n, k):
#     return k + 2


# import sys
# for line in sys.stdin:
#     a = line.split()
#     n = int(a[0])
#     k = int(a[1])
#     print(solve(n, k))


if __name__ == '__main__':
    m, k = map(int, input().split())
    times = 0
    for i in range(k):
        if m <= 2:
            break
        m = (m // 2) + 1 if m & 1 else m // 2
        times += 1
    print(times + m)
