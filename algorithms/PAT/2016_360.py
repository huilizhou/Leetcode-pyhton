
from collections import defaultdict

num = int(input())
for _ in range(num):
    a, dd = input(), defaultdict(int)
    for i in a:
        dd[i] += 1
    for i in a:
        dd[i] += 1
        if dd[i] == 2:
            print(i)
            break
