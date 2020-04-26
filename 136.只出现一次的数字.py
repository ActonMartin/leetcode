#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
from collections import defaultdict
"""
Solution2的方法中使用了defaultdict作为hash表，感觉跟第一种方法差不多类似的啊 
 就是使用了内置的函数，速度测试是快了很多。
"""
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        no_repeat_list = list(set(nums))
        d = dict()
        for i in no_repeat_list:
            d[i] = nums.count(i)
        for j in d:
            if d[j] == 1:
                return j

class Solution2:
    def singleNumber(self, nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for j in hash_table:
            if hash_table[j] == 1:
                return j
# @lc code=end

