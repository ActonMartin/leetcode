#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = s.count('A')
        if count_a < 2:
            flag = 0
            i = 0
            while i < len(s):
                if s[i] == 'L':
                    flag += 1
                    i += 1
                else:
                    flag = 0
                    i += 1
                if flag == 3:
                    return False
            return True
        else:
            return False
# @lc code=end

