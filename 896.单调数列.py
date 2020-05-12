#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
# https://leetcode-cn.com/problems/monotonic-array/description/
#
# algorithms
# Easy (51.83%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 28.2K
# Testcase Example:  '[1,2,2,3]'
#
# 如果数组是单调递增或单调递减的，那么它是单调的。
# 
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A
# 是单调递减的。
# 
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,2,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：[6,5,4,4]
# 输出：true
# 
# 
# 示例 3：
# 
# 输入：[1,3,2]
# 输出：false
# 
# 
# 示例 4：
# 
# 输入：[1,2,4,5]
# 输出：true
# 
# 
# 示例 5：
# 
# 输入：[1,1,1]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 
# 
#

# @lc code=start
class Solution1:
    def isMonotonic(self, A):
        tag1 = False
        tag2 = False
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                tag1 = True
            elif A[i] > A[i+1]:
                tag2 = True
        if tag1 and tag2:
            return False
        else:
            return True
class Solution2:
    def isMonotonic(self, A):
        sub = 0
        for i in range(1, len(A)):
            if sub == 0:
                sub = A[i] - A[i-1]
            else:
                if sub*(A[i] - A[i-1]) < 0:
                    return False
        return True

class Solution3(object):
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        #知道首尾大小就知道是递增还是递减了
        tail = A[-1]
        head = A[0]
        for i in range(len(A) - 1):
            #递减
            if head > tail and A[i] < A[i+1]:
                return False
            #递增
            elif head < tail and A[i] > A[i+1]:
                return False
            #水平直线
            elif head == tail  and A[i] != A[i+1]:
                return False
                
        return True
        
# @lc code=end

