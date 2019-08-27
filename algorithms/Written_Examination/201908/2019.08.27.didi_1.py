# import sys

# if __name__ == "__main__":
#     line1 = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     m, n = list(map(int, line1.split()))

#     for i in range(1, n):
#         m += pow(m, (1 / pow(2, i)))
#     print(m)


# s = input()
# if "+" in s:
#     m=s.index('+')
#     n=s.index('=')
#     a=int(s[:m].strip())
#     b=int(s[m:n].strip())
#     return (-b/a)
# if '- ' in s:
#     m=s.index('-')
#     n=s.index('=')
#     a=int(s[:m].strip())
#     b=int(s[m:n].strip())
#     return (b/a)


# s = input()
def solve(s):
    x = s.index('x')
    n = s.index('=')
    if "+" in s:
        m = s.index('+')
        a = int(s[:x].strip())
        b = int(s[m + 1:n].strip())
        return 'x=' + str(round((-b / a), 1))
    elif '-' in s:
        m = s.index('-')
        a = int(s[:x].strip())
        b = int(s[m + 1:n].strip())
        return 'x=' + str(round((b / a), 1))


s = "5x- 10=0"
print(solve(s))
