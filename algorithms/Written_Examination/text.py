import sys


# # def solve(n, k):
# #     res = []
# #     for x in range(n + 1):
# #         for y in range(1, n + 1):
# #             if x % y >= k:
# #                 res.append((x, y))
# #     return len(res)


# # print(solve(5, 2))

# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     values = list(map(int, line.split()))
#     n, k = values[0], values[1]
#     for i in range(k):
#         nums = list(map(int, line.split()))
3
#     # print(solve(n, k))
#     print(n, k, nums)


def solve(n, nums):
    L_1 = nums.count('L')
    R_1 = nums.count('R')
    if L_1 > R_1:
        if (L_1 - R_1) % 4 == 0:
            return "N"
        elif (L_1 - R_1) % 4 == 1:
            return "W"
        elif (L_1 - R_1) % 4 == 2:
            return "S"
        else:
            return "E"
    elif L_1 < R_1:
        if (R_1 - L_1) % 4 == 0:
            return "N"
        elif (R_1 - L_1) % 4 == 1:
            return "E"
        elif (R_1 - L_1) % 4 == 2:
            return "S"
        else:
            return "W"
    else:
        return "N"


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    n = int(line1)
    line2 = sys.stdin.readline().strip()
    nums = str(line2)

    print(solve(n, nums))
