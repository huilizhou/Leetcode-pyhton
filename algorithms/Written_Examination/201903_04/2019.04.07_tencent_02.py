import sys


def count(n, A):
    res = 0
    N = int(n)
    a = A
    for i in range(N - 1):
        res += abs(a[i])
        a[i + 1] = a[i] + a[i + 1]
    return res


if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())
    # A = [int(i) for i in sys.stdin.readline().strip().split()]
    n = 5
    A = [5, -4, 1, -3, -1]
    print(count(n, A))
