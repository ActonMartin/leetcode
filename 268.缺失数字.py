#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        sort_list = sorted(nums)
        print(sort_list)
        i = 0
        while i < len(nums):
            if sort_list[i] == i:
                i += 1
            else:
                return i
        return i

'''
Solution1里面的i小于nums的长度就好，因为在小于的时候，所有的索引都可以取到给出的nums这个
数列的长度，当在这个数列的长度都已经找完后，都是相等的话，那么那个缺少的值就是最后一个值，
在上一次判断相等的时候，索引是已经自增了，在这一次的时候，while这一判断断然是无法通过的，
那么刚好对应在while语句块外面的return i的操作。
'''
class Solution:
    def missingNumber(self, nums):
        set_nums = set(nums)
        for i in range(len(nums)+1):
            if i not in set_nums:
                return i
# @lc code=end

