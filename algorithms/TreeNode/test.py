# items = [1, 10, 7, 4, 5, 9]
# head, *tail = items
# print(head)
# print(tail)


# 1.3 保留最后N个元素
# from collections import deque

# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.appendleft(5)
# q.pop()
# q.popleft()
# print(q)

# # 1.4 查找最大或最小的N个元素
# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
# print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
print(heap)
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heap)
print(heapq.heappop(heap))
print(heap)


# nums = (1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2)
# print(len(nums))
# res = []
# for i in nums:
#     res.append(i)
# print(res)

# 1.6 字典中的键映射多个值
# from collections import defaultdict
# # d = defaultdict(list)
# # d['a'].append(1)
# # d['a'].append(2)
# # d['a'].append(4)
# # print(d)

# d = defaultdict(list)
# for key, value in ((1, 2), (3, 6)):
#     d[key].append(value)

# print(d)

# prices = {'ACME': 45.23, 'AAPL': 612.78,
#           'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

# # min_prices = min(zip(prices.values(), prices.keys()))
# # print(min_prices)
# prices_and_names = list(zip(prices.values(), prices.keys()))
# print(min(prices_and_names))  # OK
# print(max(prices_and_names))


# a = {'x': 1, 'y': 2, 'z': 3}
# b = {'w': 10, 'x': 11, 'y': 2}

# print(a.keys() & b.keys())


# nums = [24, 26, 25, 28, 27, 33, 29, 32, 30, 31]
# import heapq
# heap = list(nums)
# print(heap)
# heapq.heapify(heap)
# print(heap)
# heapq.heappop(heap)
# print(heap)
