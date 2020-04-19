#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        if str_x[::-1] == str_x:
           return True
        else:
           return False
# @lc code=end

