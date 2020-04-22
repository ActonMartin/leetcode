#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            if (mid * mid) <= x:
                low = mid + 1
            else:
                high = mid -1
            
        return low - 1
# @lc code=end

