#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# https://leetcode-cn.com/problems/island-perimeter/description/
#
# algorithms
# Easy (67.60%)
# Likes:    235
# Dislikes: 0
# Total Accepted:    22K
# Total Submissions: 32.4K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
# 
# 
# 
# 示例 :
# 
# 输入:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# 输出: 16
# 
# 解释: 它的周长是下面图片中的 16 个黄色的边：
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """ i是行，j是列
        0 1 0 0
        1 1 1 1
        0 1 0 0
        1 1 0 0
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i == 0 or grid[i-1][j] == 0:
                        res += 2
                    if j == 0 or grid[i][j-1] == 0:
                        res += 2
        return res

# @lc code=end

