# 有问题

# def daguai(n, nums, values):
#     res, v = 0, 0
#     for i in range(n):
#         if nums[i] > nums[i - 1]:
#             res += values[i]
#         for j in range(i):
#             if nums[j] > sum(nums[:i]):
#                 res += values[j]
#                 v = min(v, res)
#     return v


# import sys
# if __name__ == "__main__":
#     n = 4
#     nums = [1, 2, 4, 8]
#     values = [1, 2, 1, 2]

# n = int(sys.stdin.readline().strip())
# line = sys.stdin.readline().strip()
# nums = list(map(int, line.split()))
# line = sys.stdin.readline().strip()
# values = list(map(int, line.split()))
# print(daguai(n, nums, values))
