#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution1:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        mid=n//2+1
        g=guess(mid)
        while g:
            if g==-1:
                right=mid-1
                mid=left+(right-left)//2
                g=guess(mid)
            else:
                left=mid+1
                mid=left+(right-left)//2
                g=guess(mid)
        return mid

class Solution:
    def guessNumber(self, n):
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low)//2
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1

# @lc code=end

