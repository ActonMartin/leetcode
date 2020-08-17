#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1 and n%2 == 0:
            n = n//2
        if n == 1:
            return True
        else:
            return False
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n = n / 2
        return n == 1


# @lc code=end

