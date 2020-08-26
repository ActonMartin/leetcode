#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution1:
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


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else: return mid
        return left
# @lc code=end

