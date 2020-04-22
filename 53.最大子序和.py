#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_, sum_ = nums[0], nums[0]
        for n in nums[1:]:
            sum_ = (sum_ + n) if sum_ >= 0 else n
            max_ = max_ if max_ > sum_ else sum_ #比max快点?
        return max_

# @lc code=end

