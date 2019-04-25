# KMP 算法
'''
KMP字符串匹配的主函数
若存在字串返回字串在字符串中开始位置的下标，若没有则返回-1。
我理解了阮一峰的讲解
'''


def KMP_algorithm(s, p):
    pnext = gen_pnext(p)
    m = len(s)
    n = len(p)
    i, j = 0, 0
    while i < m and j < n:
        if s[i] == p[j]:
            i += 1
            j += 1
        elif j != 0:
            j = pnext[j - 1]
        else:
            i += 1
    if j == n:
        return i - j
    else:
        return -1


def gen_pnext(p):
    '''
    构造临时数组pnext
    '''
    index, n = 0, len(p)
    pnext = [0] * n
    i = 1
    while i < n:
        if p[i] == p[index]:
            pnext[i] = index + 1
            index += 1
            i += 1
        elif index != 0:
            index = pnext[index - 1]
        else:
            pnext[i] = 0
            i += 1
    return pnext


print(gen_pnext('abcdex'))
print(KMP_algorithm('abcdefgab', 'abcdex'))
