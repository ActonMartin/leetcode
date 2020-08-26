#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (61.64%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    65.4K
# Total Submissions: 106K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start


class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a,b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res

    def getRow(self, rowIndex: int) -> List[int]:
        list = self.generate(rowIndex+1)
        return list[rowIndex]

class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1 for _ in range(rowIndex+1)]  # 先生成一个目标行元素的列表
        for i in range(2,rowIndex+1):  # 从第3行开始dp
            for j in range(i-1,0,-1):     # 从后往前，保证O(n)空间
                row[j] = row[j-1]+row[j]
        return row

class Solution:
    def getRow(self, rowIndex):
        res = [1]
        while len(res) <= rowIndex:
            res = [a+b for a,b in zip([0] + res, res+ [0])]
            print('res',res)
        return res
# @lc code=end

