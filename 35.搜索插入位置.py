#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            for index, i in enumerate(nums):
                if i >= target:
                    count += 1
                    if count > 1:
                        break
                    return index

# @lc code=end

