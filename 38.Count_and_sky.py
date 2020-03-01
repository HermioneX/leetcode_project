'''
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"

这种一步一步的问题，目前来看并没有明显的规律，即某种函数形式，所以考虑写作递推形式
递推过程中主要思路：
1 给出n，要推n-1次，因此一定有个n-1的大循环(循环次数没有用的时候，用_)
2 需要的中间量：字符串容器，单个数字变量，个数变量
3:向后推时，每次连续数字结束，有新的数字出现时，单个数字变量，个数变量均跳动一次，
4 易错点：字符串容器要在数字和个数变量跳动之前变化
'''
#### my solution：
'''
运行时间30多ms，仅高于21.83%
发现了初始化的一个智障问题，修改了一下
发现一种有意思的写法，结果的：not bool(len(sl)) 本质只是想判断sl是不是空的，不如直接写 return s==[]
但是时间复杂度没有算过哪个更好
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(n-1):
            fl,count,ns = s[0],0,""
            for l in s:
                if l == fl:
                    count +=1
                else:
                    ns += str(count) + fl   #总结之前的字符段
                    count = 1
                    fl = l
            ns += str(count) + fl
            s  = ns
        return s
