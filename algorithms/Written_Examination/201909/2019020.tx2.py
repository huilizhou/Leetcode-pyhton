import sys


if __name__ == "__main__":
    def match(x, y):
        l1 = min(abs(x), abs(y))
        m1 = max(abs(x), abs(y))
        l2 = min(abs(x + y), abs(x - y))
        m2 = max(abs(x + y), abs(x - y))
        if l2 <= l1 and m2 >= m1:
            return True
        return False

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    count = 0
    for i in range(len(values)):
        j = i + 1
        for j in range(len(values)):
            x = values[i]
            y = values[j]

            if match(x, y) == True:
                count += 1
                print(x, y)
    print(count)


# 3
# 1 -2 2
# 1 1
