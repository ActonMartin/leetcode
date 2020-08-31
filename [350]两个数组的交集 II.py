# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
#  
# 
#  示例 2: 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。 
#  我们可以不考虑输出结果的顺序。 
#  
# 
#  进阶： 
# 
#  
#  如果给定的数组已经排好序呢？你将如何优化你的算法？ 
#  如果 nums1 的大小比 nums2 小很多，哪种方法更优？ 
#  如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 
#  
#  Related Topics 排序 哈希表 双指针 二分查找 
#  👍 384 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
    def intersect(self, nums1, nums2):
        dict_nums1, dict_nums2 = defaultdict(int), defaultdict(int)
        for i in nums1:
            dict_nums1[i] += 1
        for j in nums2:
            dict_nums2[j] += 1
        result = []
        for i in dict_nums1:
            if i in dict_nums2:
                if dict_nums1[i] <= dict_nums2[i]:
                    result += ([i]*(dict_nums1[i]))
                else:
                    result += ([i]*(dict_nums2[i]))
        return result

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    num1 = [4,9,5]
    num2 = [4,4,9,3,5,5]
    jj = Solution().intersect(num1,num2)
    print(jj)
