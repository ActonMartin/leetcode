# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in s:
            num = ord(i) - ord('A') + 1
            ans = ans * 26 + num
        return ans
# @lc code=end

