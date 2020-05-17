# @before-stub-for-debug-begin
from python3problem168 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution1:
    def convertToTitle(self, n: int) -> str:
        eng= " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result= ""
        while n>0:
            rest=n % 26
            if rest==0:
                rest=26
                n-=1
            n=n//26
            result=eng[rest]+result
        return result

class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n > 0:                # 每次循环 是 每次取模得到数字 的过程
            n -= 1                  # 把 从1开始满27进位 变回 从0开始满26进位
            a, b = n//26, n%26      # 这里b的取值范围是0-25
            s = s + chr(b+65)       # A的ASCII码是65，b+65表示 0-25 和 A-Z 有了一一对应
            n = a
        return s[::-1]              # 最后将 优先获得的低位数字 反转到最后


# @lc code=end

