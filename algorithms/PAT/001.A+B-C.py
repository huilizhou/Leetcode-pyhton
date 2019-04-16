'''
https://www.nowcoder.com/pat/6/problem/4077
'''
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        if values[0] + values[1] > values[2]:
            print("Case #" + str(i + 1) + ": true")
        else:
            print("Case #" + str(i + 1) + ": false")
