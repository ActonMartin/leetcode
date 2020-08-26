#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (35.28%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    32.6K
# Total Submissions: 92.2K
# Testcase Example:  '[3,2,1]'
#
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
# 
# 示例 1:
# 
# 
# 输入: [3, 2, 1]
# 
# 输出: 1
# 
# 解释: 第三大的数是 1.
# 
# 
# 示例 2:
# 
# 
# 输入: [1, 2]
# 
# 输出: 2
# 
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
# 
# 
# 示例 3:
# 
# 
# 输入: [2, 2, 3, 1]
# 
# 输出: 1
# 
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
# 
# 
#

# @lc code=start
from collections import defaultdict, OrderedDict
class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        count_dict = defaultdict(int)
        for i in nums:
            count_dict[i] += 1
        sorted_dic = sorted(count_dict.items(), key= lambda x: x[0], reverse= True)
        if len(sorted_dic) < 3:
            return sorted_dic[0][0]
        else:
            return sorted_dic[2][0]

class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        # 限定条件一：返回数组中第三大的数
        # 限定条件二：不存在第三大则返回最大的数
        # 限定条件三：算法时间复杂度 O(n)
        nums_set = set(nums)
        if len(nums_set)<3:
            return max(nums_set)
        else:
            nums_set.remove(max(nums_set))
            nums_set.remove(max(nums_set))
            return max(nums_set)



from math import isinf
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        a = b = c = float('-inf')

        for num in nums:
            if num > a:
                c = b
                b = a
                a = num
            elif num > b:
                c = b
                b = num
            elif num > c:
                c = num

        return a if isinf(c) else c

# @lc code=end

