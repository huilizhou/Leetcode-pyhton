'''
1.三个同样的字母连在一起，一定是拼写错误，去掉一个的就好了
2.两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好了
3.上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该
优先考虑修复AABB，结果为AABCC

'''


def solve(s):
    n = len(s)
    r = list(s[:min(len(s), 2)])
    for i in range(2, n):
        if s[i] == r[-1] == r[-2]:
            continue
        if s[i] == r[-1] and len(r) > 2 and r[-2] == r[-3]:
            continue
        r.append(s[i])
    return "".join(r)


for test_case in range(int(input())):
    print(solve(input()))
