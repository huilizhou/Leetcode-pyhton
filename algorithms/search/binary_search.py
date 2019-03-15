'''
二分搜索(binary_search)，也称折半搜索货对数搜索，是一种在有序数组中查找某一特定元素的搜索算法。
搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，
而且根开始一样从中间元素开始比较，如果在某一步骤数组为空，则代表找不到。
这种搜索算法每次比较都使得搜索范围缩小一半。

二分搜索的复杂度是对数时间，进行O(log n)次比较操作。
二分搜索使用常数空间，无论对任何大小的输入数据，算法使用的空间都是一样的。
除非输入数据数量很少，否则二分搜索比线性搜索更快，但数组必须事先被排序。
尽管特定的、为了快速搜索而设计的数据结构更有效（比如哈希表），二分搜索应用面更广。
'''

# while 循环版本


class Solution:
    def binary_search(self, list, key):
        left, right = 0, len(list)
        while left < right:
            mid = (left + right) // 2
            if list[mid] > key:
                right = mid - 1
            elif list[mid] < key:
                left = mid + 1
            else:
                return mid
        return False


print(Solution().binary_search([1, 3, 5, 7, 8, 9], 6))
