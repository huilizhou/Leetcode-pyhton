import sys


# def solve(n, q, nums, values):

#     res = []
#     for i in values:
#         count = 0
#         for j in range(len(nums)):
#             if nums[j] >= i:
#                 nums[j] -= 1
#                 count += 1
#         res.append(count)
#     return res


# print(solve(3, 2, [1, 2, 3], [3, 3]))

if __name__ == "__main__":
    values = []
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, q = list(map(int, line1.split()))
    # 读取第二行
    line2 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    nums = list(map(int, line2.split()))

    for i in range(q):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        value = int(line)
        values.append(value)

    # print(solve(n, q, nums, values))
    res = []
    for i in values:
        count = 0
        for j in range(len(nums)):
            if nums[j] >= i:
                nums[j] -= 1
                count += 1
        res.append(count)
    for j in range(len(res)):
        print(res[j])
