#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sort_list = sorted(nums)
        print(sort_list)
        i = 0
        while i < len(nums):
            if sort_list[i] == i:
                i += 1
            else:
                return i
        return i
# @lc code=end

