class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count('R') != moves.count('L') or moves.count('U') != moves.count('D'):
            return False
        else:
            return True

        # # 人家的解法
        # return (moves.count('U') == moves.count('D')) and (moves.count('R') == moves.count('L'))
