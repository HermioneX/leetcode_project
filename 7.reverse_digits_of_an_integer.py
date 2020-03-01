'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
click to show spoilers.
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)   #x > 0，s=1; x < 0,s=-1
        r = int(`s*x`[::-1])    #先将字符串反转，然后将字符串转换为整型
        return s*r * (r < 2**31)    #r < 2**31为真时返回1,否则返回0;2**31表示2的31次
