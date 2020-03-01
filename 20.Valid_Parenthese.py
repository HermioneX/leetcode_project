'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true


主要思路：
匹配问题，且观察获得应该是个进栈出栈的问题
'''
#### my solution：
'''
运行时间30多ms，仅高于21.83%
发现了初始化的一个智障问题，修改了一下
发现一种有意思的写法，结果的：not bool(len(sl)) 本质只是想判断sl是不是空的，不如直接写 return s==[]
但是时间复杂度没有算过哪个更好
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strDir = {'(':-1,')':1,'[':-2,']':2,'{':-3,'}':3}
        if s == '':
            return True
        sl = []
        sl.append(s[0])
        for l in s[1:]:
            if (len(sl) == 0 or strDir[l]+strDir[sl[-1]] != 0):
                sl.append(l)

            else:
                sl.pop()
        return not bool(len(sl))
