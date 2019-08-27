# import sys
# import math
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))

#     for v in values:
#         # 质数
#         for j in range(2, math.sqrt(v) + 1):
#             if v % j == 0:
#                 break
#         else:
