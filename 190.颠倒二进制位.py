# @before-stub-for-debug-begin
from python3problem190 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution1:
    def reverseBits(self, n: int) -> int:
        str_n = str(bin(n)[2:])
        if len(str_n) < 32:
            gap = 32 - len(str_n)
            str_n = '0'*gap + str_n
        print(str_n)
        kk = '0b'
        for i in range(len(str_n)-1, -1, -1):
            kk += str_n[i]
        return int(kk,2)

class Solution:
    def reverseBits(self, n: int) -> int:
        nums=str(bin(n))
        nums='0'*(32-len(nums[2:]))+nums[2:]
        return int(nums[::-1],2)
        
class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


# @lc code=end

