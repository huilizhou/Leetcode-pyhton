import sys


def solver(level, score, k):
    m = list(zip(level, score))


if __name__ == "__main__":
    level = []
    score = []
    line1 = sys.stdin.readline().strip()
    n, k = list(map(int, line1.split()))
    for _ in range(n):
        line = sys.stdin.readline().strip()
        l, s = list(map(int, line.split()))
        level.append(l)
        score.append(s)

    print(level, score)
