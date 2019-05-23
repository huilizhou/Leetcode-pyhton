# 困于环中的机器人
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        dx, dy = 0, 1
        for ins in instructions:
            if ins == 'L':
                dx, dy = -dy, dx
            elif ins == 'R':
                dx, dy = dy, -dx
            else:
                x, y = x + dx, y + dy
        return (dx, dy) != (0, 1) or (x, y) == (0, 0)


print(Solution().isRobotBounded("GG"))
