#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (52.09%)
# Likes:    239
# Dislikes: 0
# Total Accepted:    132.1K
# Total Submissions: 253K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: true
# 
# 示例 2:
# 
# 输入: [1,2,3,4]
# 输出: false
# 
# 示例 3:
# 
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
# 
#

# @lc code=start
class Solution1:
    """
    有一个case会超时
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            counts = nums.count(i)
            if counts > 1:
                return True
        return False

from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums):
        hash_table = defaultdict(int)
        if not nums:
            return False
        for i in nums:
            hash_table[i] += 1
        kk = sorted(hash_table.items(), key=lambda  x: x[1])
        if int(kk[-1][1]) > 1:
            return True
        else:
            return False
        
# @lc code=end

