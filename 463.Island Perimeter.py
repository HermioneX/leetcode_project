'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

为了获得黄色边长，两种思路：
1.直接数黄边，凡是海陆相接的或者在地图边沿的都算
2.数陆陆相接，然后陆地数*4-陆陆相接

2 由于二者都是以陆地块为准进行判别，陆陆相接，问题是需要判别是否重复计算。要么用flag，要么只计算两边，如（左、上）
但是网页似乎不能引入numpy，所以求和比较麻烦...而且还要考虑格子较少情况，所以还是选第一种吧
'''
#### my solution：
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def sum_l_u(i,j):
            adjacent = (i - 1, j), (i + 1, j), (i, j - 1),(i, j + 1),
            res = 0
            for x, y in adjacent:
                if x<0 or y<0 or x == len(grid) or y== len(grid[0]) or grid[x][y]==0:
                    res += 1
            return  res

        count = 0
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    count += sum_l_u(i,j)
        return count

## others
def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
