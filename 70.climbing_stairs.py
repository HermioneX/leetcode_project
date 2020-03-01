'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

从第三级开始，可以进行如下推断：
如果最后一级跨一步，则方法等于f(2),若最后一级跨两步，则方法等于f(1)，所以为f(1)+f(2)
同理，第四级：
如果最后一级跨一步，则方法等于f(3),若最后一级跨两步，则方法等于f(2)，所以为f(3)+f(2)
..........

第n级，为f(n-1)+f(n-2)
这里就可以看出来这是一个基本的斐波那契亚的递归，相当于求第n项的值

'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=1
        b=1
        for _ in range(n):
            a, b = b, a + b
        return a
