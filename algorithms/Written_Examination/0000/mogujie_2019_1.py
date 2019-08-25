s = input()
n = int(input())

if n > len(s):
    print(-1)
elif n < 0:
    print(-1)
else:
    i = 0
    while i + n <= len(s):
        print(s[i:i + n])
        i += 1
        pass
