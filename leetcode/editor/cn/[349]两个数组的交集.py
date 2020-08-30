# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中的每个元素一定是唯一的。 
#  我们可以不考虑输出结果的顺序。 
#  
#  Related Topics 排序 哈希表 双指针 二分查找 
#  👍 224 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ this solution use more runtime and use more RAM, so this not a  good choice to solve problem"""
        intersection = [i for i in nums1 if i in nums1 and i in nums2]
        insection = set(intersection)
        return intersection


class Solution:
    def intersection(self, nums1, nums2):
        """ this solution could use less runtime,but still use more RAM"""
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        intersection = [i for i in nums1_set if i in nums2_set]
        return intersection
        
# leetcode submit region end(Prohibit modification and deletion)
