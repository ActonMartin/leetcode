#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
from collections import defaultdict
class Solution1:
    def hammingWeight(self, n: int) -> int:
        binary_num = list(bin(n)[2:])
        hash_table = defaultdict(int)

        for i in binary_num:
            hash_table[i] += 1

        for j in hash_table:
            if j == '1':
                return hash_table[j]
            else:
                return 0

class Solution2:
    def hammingWeight(self, n: int) -> int:
        binary_num = list(bin(n)[2:])
        nn = binary_num.count('1')
        return nn

class Solution:
    def hammingWeight(self, n: int) -> int:
        # 位运算 无符号的整数
        res = 0
        while n>0:
            res += n&1
            n = n>>1
        return res

# @lc code=end

