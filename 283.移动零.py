#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (61.94%)
# Likes:    704
# Dislikes: 0
# Total Accepted:    196.8K
# Total Submissions: 316.9K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#

# @lc code=start
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        cout_zero = nums.count(0)
        for i in range(cout_zero):
            nums.remove(0)
        for i in range(cout_zero):
            nums.append(0)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0 
        for i in range(len(nums)):
            idx = i-zero_num
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                zero_num+=1

# @lc code=end

