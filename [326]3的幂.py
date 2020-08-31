# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。 
# 
#  示例 1: 
# 
#  输入: 27
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: 0
# 输出: false 
# 
#  示例 3: 
# 
#  输入: 9
# 输出: true 
# 
#  示例 4: 
# 
#  输入: 45
# 输出: false 
# 
#  进阶： 
# 你能不使用循环或者递归来完成本题吗？ 
#  Related Topics 数学 
#  👍 124 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution1:
    """
    stupid method
    执行耗时:1848 ms,击败了5.12% 的Python3用户
    内存消耗:13.8 MB,击败了6.57% 的Python3用户
    """
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        near = int(n**(1/3))+1
        for i in range(near):
            if 3**i == n:
                return True
        return False


class Solution:
    """
    执行耗时:88 ms,击败了84.77% 的Python3用户
    内存消耗:13.8 MB,击败了12.09% 的Python3用户
    """
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
# leetcode submit region end(Prohibit modification and deletion)
