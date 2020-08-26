#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (51.76%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    75.5K
# Total Submissions: 145.6K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 
# 
# 提示：
# 
# 
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n, = len(num1)-1, len(num2)-1
        carry = 0
        res = ''
        while m >= 0 or n >= 0:
            n1 = int(num1[m]) if m >= 0 else 0
            n2 = int(num2[n]) if n >=0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            m -= 1
            n -= 1
        return "1" + res if carry else res

# @lc code=end

