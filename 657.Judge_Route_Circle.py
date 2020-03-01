'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L(Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
'''
#### my solution：
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = 0
        v = 0
        for step in moves:
            if step == 'U':
                v = v + 1
            elif step == 'D':
                v = v - 1
            elif step == 'L':
                h = h - 1
            elif step == 'R':
                h = h + 1

        return bool(not h and not v)

## others
def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
