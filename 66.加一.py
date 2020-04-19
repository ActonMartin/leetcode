#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for index, val in enumerate(digits):
            num += str(val)
        result = int(num) + 1
        ll = []
        for index, val in enumerate(str(result)):
            ll.append(int(val))
        return ll

class Solution:
    """
    这个方法就是从列表从后往前挪动，如果最后一位不是数字9，
    仅仅需要的是对这个数字进行加1的操作就完事了。
    如果遇到的刚刚好是数字9，这下就把这个位置的数字加1，变成数字0
    ，如果恰恰每一位都是数字9，那么就在走到列表的最前面的时候，
    把那个数字改成1，然后在列表后增加一位数字0，这下算是彻底的完事了。
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if int(digits[i]) < 9:
                digits[i] += 1
                return digits
            if i==0:
                digits[i]=1
                digits.append(0)
            else:
                digits[i] = 0
        return digits
# @lc code=end

