# 递归二分查找
# def binary_search_recursion(lst, val, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if lst[mid] < val:
#         return binary_search_recursion(lst, val, mid + 1, end)
#     if lst[mid] > val:
#         return binary_search_recursion(lst, val, start, mid - 1)
#     return mid


# print(binary_search_recursion([1, 3, 5, 7, 8, 9], 9, 0, 6))


# 循环二分查找
def binary_search_loop(lst, val):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < val:
            start = mid + 1
        elif lst[mid] > val:
            end = min - 1
        else:
            return mid
    return None


print(binary_search_loop([1, 3, 5, 7, 8, 9], 9))


# import bisect
# a = [3, 4, 6, 6.0, 7.0, 7, 8, 8.0, 9]
# bisect.insort_left(a, 3.0)
# # bisect.insort_right(a, 3.0)
# print(a)
# bisect.insort(a, 3.0)
# print(a)
