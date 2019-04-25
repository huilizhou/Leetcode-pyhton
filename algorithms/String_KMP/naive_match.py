# 朴素的模式匹配算法
def naive_match(s, p):
    m = len(s)
    n = len(p)
    for i in range(m - n + 1):
        if s[i:i + n] == p:
            return True
    return False


print(naive_match('abc', 'c'))
