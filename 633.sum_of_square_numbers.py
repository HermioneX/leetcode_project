'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False

一个判断平方数的方法：
def is_square(N):
        return int(N**.5)**2 == N
'''

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(m):
            return int(m**.5)**2==m
        return any(is_square(c - a*a)
                for a in xrange(int(c**.5)+1))
