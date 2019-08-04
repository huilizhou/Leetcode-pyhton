import sys


try:
    while True:
        # 读一个值
        line1 = sys.stdin.readline().strip()
        if line1 == '':
            break
        # 读一行值
        line2 = sys.stdin.readline().strip()
        a = int(line1)
        l = list(map(int, line2.split()))
        b = [int(n) for n in line2.split()]
        print(a)
        print(l)
        print(b)
except:
    pass
