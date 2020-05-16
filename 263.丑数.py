# @before-stub-for-debug-begin
from python3problem263 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num%5 == 0:
            num /= 5
        while num%3 == 0:
            num /= 3
        while num%2 == 0:
            num /=2
        return num == 1

# @lc code=end

