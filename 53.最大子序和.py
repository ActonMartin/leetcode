#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
# 在线处理法O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum, ThisSum = nums[0], nums[0]
        for val in nums[1:]:
            ThisSum = (ThisSum + val) if ThisSum >= 0 else val
            MaxSum = MaxSum if MaxSum > ThisSum else ThisSum #比max快点?
        return MaxSum

# @lc code=end

