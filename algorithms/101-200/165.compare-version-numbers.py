# 比较版本号
class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 我的想法
        # v1 = version1.split('.')
        # v2 = version2.split('.')

        # l1 = len(v1)
        # l2 = len(v2)
        # max_length = max(l1, l2)

        # for i in range(max_length):
        #     if i >= l1:
        #         n1 = 0
        #     else:
        #         n1 = int(v1[i])
        #     if i >= l2:
        #         n2 = 0
        #     else:
        #         n2 = int(v2[i])

        #     if n1 > n2:
        #         return 1
        #     if n1 < n2:
        #         return -1
        #     return 0

        # 人家的写法
        ver1 = [int(token) for token in version1.split(".")]
        ver2 = [int(token) for token in version2.split(".")]

        for i in range(max(len(ver1), len(ver2))):
            data1 = ver1[i] if i < len(ver1) else 0
            data2 = ver2[i] if i < len(ver2) else 0
            if data1 > data2:
                return 1
            if data1 < data2:
                return -1
        return 0


print(Solution().compareVersion('1.23', '1.1'))
