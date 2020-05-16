# @before-stub-for-debug-begin
from python3problem258 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1

# @lc code=end

