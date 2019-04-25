# KMP模式匹配算法

'''
http://www.ruanyifeng.com/blog/2013/05/Knuth–Morris–Pratt_algorithm.html

参考阮一峰的网络日志
字符串匹配的KMP算法
'''


def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)
                break
        else:
            # return cur
            return True
    # return -1
    return False

# 部分分配表


def partial_table(p):
    '''
    partial_table("ABCDABD")->[0,0,0,0,1,2,0]
    '''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret


print(partial_table("ABCDABD"))
print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
