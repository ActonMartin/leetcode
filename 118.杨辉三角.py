#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (67.07%)
# Likes:    338
# Dislikes: 0
# Total Accepted:    98.7K
# Total Submissions: 147K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a,b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res

kk = Solution().generate(100)
print(kk)
# @lc code=end

