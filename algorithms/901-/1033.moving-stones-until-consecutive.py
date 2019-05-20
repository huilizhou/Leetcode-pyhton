# 移动石子直到连续
class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        '''
        先排序求得最大最小距离。若最大最小距离都是1时则无需移动；
        若最小距离为1时，将最远端的石头一步移动到中间石头的旁边就可以连续了；
        最小距离为2时，将最远端石头移到两相邻石头中间则连续；
        最小距离大于2时，将最远端石头移到前面两个石头其中一个的旁边，再把另外一个移过来即可。
        '''
        # L = [a, b, c]
        # L.sort()
        # a = L[1] - L[0]
        # b = L[2] - L[1]
        # if a == 1 and b == 1:
        #     return [0, 0]
        # elif a == 1 and b > 1:
        #     return [1, b - 1]
        # elif b == 1 and a > 1:
        #     return [1, a - 1]
        # elif a == 2 and b > 1:
        #     return[1, b]
        # elif b == 2 and a > 1:
        #     return [1, a]
        # else:
        #     return[2, a + b - 2]

        # 人家的写法
        a, b, c = sorted((a, b, c))
        if b - a == 1 and c - b == 1:
            return [0, 0]
        if b - a <= 2 or c - b <= 2:
            return [1, c - a - 2]
        return[2, c - a - 2]


print(Solution().numMovesStones(a=1, b=2, c=5))
