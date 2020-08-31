#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        a = str(x)
        if x>=0:
            y = int(a[::-1])#从后向前索引 每次索引一位
        else:
            y = -int(a[:0:-1])#从后向0位索引；但不包括0位每次索引一位
        if -2**31<y<2**31-1:
            return y
        else:
            return 0

class Solution1:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x > 0:
            str_result = self.change(x)
            result = int(str_result)
        if x < 0:
            str_result = self.change(-x)
            result = -int(str_result)
        if -2 ** 31 < result < 2 ** 31 - 1:
            return result
        else:
            return 0

    def change(self, x):
        result = ''
        str_x = str(x)
        for index, value in enumerate(range(len(str_x)-1, -1, -1)):
            if index == 0 and str_x[value] == '0':
                result = ''
            else:
                result += str_x[value]
        return result

# @lc code=end

