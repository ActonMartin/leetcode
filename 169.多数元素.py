# @before-stub-for-debug-begin
from python3problem169 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
"""
刚开始还在疑惑多数元素如果不止一个可怎么办。后来发现是自己想多了
这种满足要求的多数元素可就只有一个
这一道题目的思想跟136题完全无异
"""
from collections import defaultdict
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for j in hash_table:
            if hash_table[j] > (len(nums)/2):
                res = j
                break
        return res


"""
摩尔投票法(多数投票算法)
"""
class Solution:
    def majorityElement(self, nums):
        count = 0
        res = 0
        for i in nums:
            if count == 0:
                res = i
                count += 1
            else:
                if res == i:
                    count += 1
                else:
                    count -= 1
        return res
# @lc code=end

