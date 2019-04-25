# 360安全第一题，计算一组数的最大公约数
def solvers(nums):
    hash = {}
    for i in nums:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    L = list(hash.values())
    smaller = min(L)
    for i in reversed(range(2, smaller + 1)):
        if list(filter(lambda j: j % i != 0, L)) == []:
            return len(nums) // i
    return 0


print(solvers([1, 1, 2, 2, 2]))
